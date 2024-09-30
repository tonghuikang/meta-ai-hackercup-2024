import glob
import os
import pandas as pd
import hashlib

from worker import problem_name_to_problem_code
from functools import cache

def get_current_status(contest_folder):

    folders = glob.glob(f"./{contest_folder}/*/")  # only select folders

    problem_names = [os.path.basename(os.path.normpath(folder)) for folder in folders]
    problem_mapping = {problem_name_to_problem_code(problem_name): problem_name for problem_name in problem_names}

    problem_names

    # Get all files in execution_full_out
    files = glob.glob(f"./execution_*/*/*")  # get all files, e.g., 'fall_in_line' and '000'

    # Extract execution type, problem name, and file ID
    file_info = [
        (
            os.path.basename(os.path.dirname(os.path.dirname(file))),
            os.path.basename(os.path.dirname(file)),
            os.path.splitext(os.path.basename(file))[0]
        ) for file in files
    ]

    # Create a DataFrame from file_info and files
    df = pd.DataFrame(file_info, columns=['execution_type', 'problem_code', 'solution_id'])
    df["problem_name"] = df["problem_code"].map(problem_mapping)
    df['filepath'] = files

    # Pivot the DataFrame to have execution types as separate columns
    df_grouped = df.pivot(
        index=['problem_code', 'solution_id', 'problem_name'], 
        columns='execution_type', 
        values='filepath'
    ).reset_index()

    # Rename columns to include '_filepath'
    df_grouped.columns = ['problem_code', 'solution_id', 'problem_name'] + [
        f"{col}_filepath" for col in df_grouped.columns if col not in [
            'problem_code', 'solution_id', 'problem_name'
        ]
    ]

    # Function to read file content
    @cache
    def read_file(problem_name, filename):
        filepath = os.path.join('practice', problem_name, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return f.read()[:10000]
        return "Not available"

    # Add 'statement', 'sample_in', 'sample_out' columns
    df_grouped['statement'] = df_grouped['problem_name'].apply(lambda x: read_file(x, 'statement.txt'))
    df_grouped['sample_in'] = df_grouped['problem_name'].apply(lambda x: read_file(x, 'sample_in.txt'))
    df_grouped['sample_out'] = df_grouped['problem_name'].apply(lambda x: read_file(x, 'sample_out.txt'))
    df_grouped['full_in'] = df_grouped['problem_name'].apply(lambda x: read_file(x, 'full_in.txt'))

    # Function to read file content from a given filepath
    def read_file_content(filepath):
        if filepath and os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return f.read()
        return None

    # Replace 'execution_code_filepath' with the actual code content
    df_grouped['execution_code'] = df_grouped['execution_code_filepath'].apply(read_file_content)

    # Replace 'execution_sample_out_filepath' with the actual sample output content
    df_grouped['execution_sample_out'] = df_grouped['execution_sample_out_filepath'].apply(read_file_content)

    # Replace 'execution_full_out_filepath' with the actual full output content
    df_grouped['execution_full_out'] = df_grouped['execution_full_out_filepath'].apply(read_file_content)

    # Optionally, drop the original filepath columns if they are no longer needed
    df_grouped = df_grouped.drop(columns=['execution_code_filepath', 'execution_full_out_filepath', 'execution_sample_out_filepath'])

    # Aggregate to problem
    aggregated_df = df_grouped.groupby(
        [
            'problem_code', 'problem_name', 'statement', 'sample_in', 'sample_out', 'full_in'
        ]
    ).agg(list).reset_index()

    # Compute MD5 hash of concatenated execution fields
    aggregated_df["hash"] = aggregated_df.apply(
        lambda row: hashlib.md5(
            (str(row["execution_code"]) + 
            str(row["execution_sample_out"]) + 
            str(row["execution_full_out"])
            ).encode('utf-8')
        ).hexdigest()[:8],
        axis=1
    )

    # Read hashes from files
    with open('hash_analyzed', 'r') as f:
        hash_analyzed = set(line.strip() for line in f)

    with open('hash_analyzing', 'r') as f:
        hash_analyzing = set(line.strip() for line in f)

    # Define a function to determine the status based on hash
    def determine_status(row):
        if row['hash'] in hash_analyzed:
            return 'analyzed'
        elif row['hash'] in hash_analyzing:
            return 'analyzing'
        else:
            return 'not_analyzed'

    # Apply the function to create the 'status' column
    aggregated_df['status'] = aggregated_df.apply(determine_status, axis=1)        

    return df_grouped, aggregated_df


prompt = """
You will choose the best solution among the presented solutions.

This is the problem statement.

{statement}

This is the sample input.

{sample_in}

This is an expected sample output.

{sample_out}

This is the full input (which may be truncated).

{full_in}

These are the solutions, with their code and the execution outputs.

{solutions_string}

Select the best solution by returning their number, e.g. The best solution is <index>004</index>.

Write a brief description.
"""


solution_string = """
<solution>
This is solution number {solution_id}

This is the code of the solution

{execution_code}

When executed on the sample input, this is the output

{execution_sample_out}

When executed on the full input, this is the output

{execution_full_out}

</solution>
"""


from openai import OpenAI
client = OpenAI()

def call_openai(prompt):
    completion = client.chat.completions.create(
        model="o1-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content


import re

def extract_index_id(text):
    # Use regex to find content within <index> and </index>
    match = re.search(r'<index>(\d+)</index>', text)
    if match:
        return match.group(1)
    return None


import datetime

def process_row(row):
    timestring = datetime.datetime.now().strftime("%M%S")

    solutions_string = "\n\n".join(
        solution_string.format(
            solution_id = solution_id,
            execution_code = execution_code,
            execution_sample_out = execution_sample_out,
            execution_full_out = execution_full_out,
        ) for solution_id, execution_code, execution_sample_out, execution_full_out in zip(
            row["solution_id"],
            row["execution_code"],
            row["execution_sample_out"],
            row["execution_full_out"][:2000],
        )
    )

    with open('./hash_analyzing', 'a') as f:
        f.write(row["hash"] + "\n")

    judgment_instructions = prompt.format(
        statement = row["statement"],
        sample_in = row["sample_in"],
        sample_out = row["sample_out"],
        full_in = row["full_in"][:2000],
        solutions_string = solutions_string,
    )

    openai_judgment = call_openai(judgment_instructions)

    selected_solution_id = extract_index_id(openai_judgment)

    problem_code = row["problem_code"]

    # Define the source file paths for the code and output
    code_src = f"execution_code/{problem_code}/{selected_solution_id}.py"
    output_src = f"execution_full_out/{problem_code}/{selected_solution_id}.txt"

    code_dst = f"code/{problem_code}_{timestring}_{selected_solution_id}.py"
    output_dst = f"output/{problem_code}_{timestring}_{selected_solution_id}.txt"

    os.makedirs(f'code', exist_ok=True)
    os.makedirs(f'output', exist_ok=True)

    import shutil

    if os.path.exists(code_src):
        shutil.copy(code_src, code_dst)

    if os.path.exists(output_src):
        shutil.copy(output_src, output_dst)

    with open('./hash_analyzed', 'a') as f:
        f.write(row["hash"] + "\n")


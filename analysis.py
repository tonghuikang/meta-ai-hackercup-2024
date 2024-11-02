import glob
import os
import pandas as pd
import hashlib
import shutil
import datetime

from worker import problem_name_to_problem_code
from functools import cache
from typing import Any


def save_submission(problem_code, solution_id, is_correct=False):

    os.makedirs(f'evaluation_artifacts/execution_sample_out/{problem_code}', exist_ok=True)
    os.makedirs(f'evaluation_artifacts/execution_response/{problem_code}', exist_ok=True)
    os.makedirs(f'evaluation_artifacts/execution_full_out/{problem_code}', exist_ok=True)
    os.makedirs(f'evaluation_artifacts/execution_code/{problem_code}', exist_ok=True)

    datetime_string = datetime.datetime.now().strftime("%d-%H%M")
    for filepath in glob.glob(f"execution_*/{problem_code}/{solution_id}.*"):
        new_solution_id = datetime_string + "-" + solution_id
        if is_correct:
            new_solution_id += "-correct"
        new_filepath = "evaluation_artifacts/" + filepath.replace(solution_id, new_solution_id)
        shutil.copy(filepath, new_filepath)


def get_current_status(contest_folder, evaluation=False):
    if evaluation is True:
        contest_folder = "evaluation_problems"
        artifact_filepath_wildcards = "./evaluation_artifacts/execution_*/*/*"
    else:
        artifact_filepath_wildcards = "./execution_*/*/*"

    folders = glob.glob(f"./{contest_folder}/*/")  # only select folders

    # Get all files in execution_full_out
    files = glob.glob(artifact_filepath_wildcards)  # get all files, e.g., 'fall_in_line' and '000'

    # Extract execution type, problem name, and file ID
    file_info = [
        (
            os.path.basename(os.path.dirname(os.path.dirname(file))),
            os.path.basename(os.path.dirname(file)),
            os.path.splitext(os.path.basename(file))[0]
        ) for file in files
    ]

    if file_info == []:
        return pd.DataFrame(), pd.DataFrame()

    problem_names = [os.path.basename(os.path.normpath(folder)) for folder in folders]
    problem_mapping = {problem_name_to_problem_code(problem_name): problem_name for problem_name in problem_names}

    # Create a DataFrame from file_info and files
    df = pd.DataFrame(file_info, columns=['execution_type', 'problem_code', 'solution_id'])
    df["problem_name"] = df["problem_code"].map(problem_mapping)
    df['filepath'] = files
    df['filepath'] = df['filepath'].astype(str)

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

    if 'execution_response_filepath' not in df_grouped.columns:
        df_grouped['execution_response_filepath'] = None

    if 'execution_code_filepath' not in df_grouped.columns:
        df_grouped['execution_code_filepath'] = None

    if 'execution_sample_out_filepath' not in df_grouped.columns:
        df_grouped['execution_sample_out_filepath'] = None

    if 'execution_full_out_filepath' not in df_grouped.columns:
        df_grouped['execution_full_out_filepath'] = None

    # Function to read file content
    @cache
    def read_file(problem_name, filename):
        filepath = os.path.join(contest_folder, problem_name, filename)
        if filepath and type(filepath) == str and os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return f.read()
        return "Not available"

    # Add 'statement', 'sample_in', 'sample_out' columns
    df_grouped['statement'] = df_grouped['problem_name'].apply(lambda x: read_file(x, 'statement.txt'))
    df_grouped['sample_in'] = df_grouped['problem_name'].apply(lambda x: read_file(x, 'sample_in.txt'))
    df_grouped['sample_out'] = df_grouped['problem_name'].apply(lambda x: read_file(x, 'sample_out.txt'))
    df_grouped['full_in'] = df_grouped['problem_name'].apply(lambda x: read_file(x, 'full_in.txt'))

    # Function to read file content from a given filepath
    def read_file_content(filepath):
        if filepath and type(filepath) == str and os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return f.read()
        return None

    # Replace 'execution_code_filepath' with the actual code content
    df_grouped['execution_response'] = df_grouped['execution_response_filepath'].apply(read_file_content)

    # Replace 'execution_code_filepath' with the actual code content
    df_grouped['execution_code'] = df_grouped['execution_code_filepath'].apply(read_file_content)

    # Replace 'execution_sample_out_filepath' with the actual sample output content
    df_grouped['execution_sample_out'] = df_grouped['execution_sample_out_filepath'].apply(read_file_content)

    # Replace 'execution_full_out_filepath' with the actual full output content
    df_grouped['execution_full_out'] = df_grouped['execution_full_out_filepath'].apply(read_file_content)

    # Optionally, drop the original filepath columns if they are no longer needed
    df_grouped = df_grouped.drop(
        columns=[
            'execution_response_filepath',
            'execution_code_filepath',
            'execution_full_out_filepath',
            'execution_sample_out_filepath'
        ]
    )

    def extract_max_case_string_from_input(input_text):
        # assume the first line is input
        try:
            num_cases = int(input_text.split("\n")[0])
            return f"Case #{num_cases}"
        except:
            return ""

    df_grouped['case_string'] = df_grouped['full_in'].apply(extract_max_case_string_from_input)
    df_grouped['case_string_found'] = df_grouped.apply(
        lambda row: bool(row["execution_full_out"]) and row["case_string"] in row["execution_full_out"], axis=1
    )
    df_grouped['sample_out_found'] = df_grouped.apply(
        lambda row: bool(row["execution_sample_out"]) and row["sample_out"].strip() in row["execution_sample_out"], axis=1
    )

    # Subset to aggregate grouping by
    df_subset_to_aggregate = df_grouped[
        (~(df_grouped["execution_sample_out"] == ""))
        & (~(df_grouped["execution_full_out"] == ""))
        & (~(df_grouped["execution_sample_out"].isna()))
        & (~(df_grouped["execution_full_out"].isna()))
    ]
    df_subset_to_aggregate = df_subset_to_aggregate[
        (~(df_subset_to_aggregate["execution_sample_out"].str.contains("An error happened during execution:")))
        & (~(df_subset_to_aggregate["execution_full_out"].str.contains("An error happened during execution:")))
        & (df_subset_to_aggregate.apply(lambda row: row["case_string"] in row["execution_full_out"], axis=1))
    ]

    if len(df_subset_to_aggregate) == 0:
        return df_grouped, pd.DataFrame()

    # Aggregate to problem
    aggregated_df = df_subset_to_aggregate.groupby(
        [
            'problem_code',
            'problem_name',
            'statement',
            'sample_in',
            'sample_out',
            'full_in',
        ]
    ).agg(list).reset_index()

    # Compute MD5 hash of concatenated execution fields
    aggregated_df["hash"] = aggregated_df.apply(
        lambda row: hashlib.md5(
            (
                str(row["execution_code"]) +
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

    timestring = datetime.datetime.now().strftime("%M%S")
    aggregated_df['timestring'] = timestring

    return df_grouped, aggregated_df


analysis_prompt = """
You will choose the fully correct solution among the presented solutions.

The fully correct solution is a solution that
- is correct on the sample input
- is most likely fully correct on the full input, without any flaws

Note that it is possible that multiple solutions could be correct.

This is the problem statement.

{statement}

This is the sample input.

{sample_in}

This is an expected output for the sample input.

{sample_out}

This is the full input (may be truncated).

{full_in}

These are the solutions, with their code and the execution outputs.

{solutions_string}

Reply in the following steps
- For each solution
    - Analyze whether does it a correct output for the sample input
    - Analyze whether does it have an obviously wrong output for the full input
- Compare and contrast the algorithms and identify wrong algorithms
- Present the best solution in this format: The best solution is <index>004</index> (and the reasoning)
""".strip()


solution_string = """
<solution>
This is solution id <index>{hashed_id}</index>

This is a presented solution

{execution_response}

When the Python code was executed on the sample input, this is the output (may be truncated)

{execution_sample_out}

When the Python code was executed on the full input, this is the output (may be truncated)

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


def call_openai(prompt):
    # Backup call
    import anthropic
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text


import re

def extract_index_id(text):
    # Use regex to find content within <index> and </index>
    match = re.search(r'<index>([\w\-]+)</index>', text)
    if match:
        return match.group(1)
    return None


def truncate(text, length):
    assert length >= 100
    if len(text) <= length:
        return text
    return text[:2*length // 3] + f" <truncated, the total length was {len(text)}> " + text[-length // 3:]


import datetime
import random

def select_solution(solutions_dict: dict[str, Any]):
    # solutions_dict contains
    # solution_id: str
    # statement: str
    # sample_in: str
    # sample_out: str
    # full_in: str
    # problem_code: str
    # timestring: str
    # execution_response: list[str]
    # execution_sample_out: list[str]
    # execution_full_out: list[str]

    solution_ids = list(solutions_dict["solution_id"])
    random.shuffle(solution_ids)
    solution_id_to_hashed_id = {}
    hashed_id_to_solution_id = {}
    for i, solution_id in enumerate(solution_ids):
        hashed_id = f"{i:03}"
        solution_id_to_hashed_id[solution_id] = hashed_id
        hashed_id_to_solution_id[hashed_id] = solution_id

    solutions_dict["should_retain"] = [
        True for _ in solutions_dict["solution_id"]
    ]
    if any(solutions_dict["sample_out_found"]):
        solutions_dict["should_retain"] = solutions_dict["sample_out_found"]        

    solutions_string = "\n\n".join(
        solution_string.format(
            hashed_id = solution_id_to_hashed_id[solution_id],
            execution_response = truncate(execution_response, 10000),
            execution_sample_out = truncate(execution_sample_out, 2000),
            execution_full_out = truncate(execution_full_out, 2000),
        ) for solution_id, execution_response, execution_sample_out, execution_full_out, should_retain in zip(
            solutions_dict["solution_id"],
            solutions_dict["execution_response"],
            solutions_dict["execution_sample_out"],
            solutions_dict["execution_full_out"],
            solutions_dict["should_retain"],
        ) if should_retain is True
    )

    with open('./hash_analyzing', 'a') as f:
        f.write(solutions_dict["hash"] + "\n")

    judgment_instructions = analysis_prompt.format(
        statement = truncate(solutions_dict["statement"], 40000),
        sample_in = truncate(solutions_dict["sample_in"], 10000),
        sample_out = truncate(solutions_dict["sample_out"], 10000),
        full_in = truncate(solutions_dict["full_in"], 10000),
        solutions_string = solutions_string,
    )

    judgment_instructions = truncate(judgment_instructions, 200_000)

    openai_judgment = call_openai(judgment_instructions)

    problem_code = solutions_dict["problem_code"]
    timestring = solutions_dict["timestring"]

    selected_hashed_id = extract_index_id(openai_judgment)
    if selected_hashed_id is None:
        print(f"Did not select solution for {problem_code}, forcing any solution.")
        selected_hashed_id = "000"
        # return openai_judgment, None
    selected_solution_id = hashed_id_to_solution_id[selected_hashed_id]

    # Define the source file paths for the code and output
    response_src = f"execution_response/{problem_code}/{selected_solution_id}.md"
    code_src = f"execution_code/{problem_code}/{selected_solution_id}.py"
    output_src = f"execution_full_out/{problem_code}/{selected_solution_id}.txt"

    response_dst = f"response/{problem_code}_{timestring}_{selected_solution_id}.md"
    code_dst = f"source/{problem_code}.py"
    output_dst = f"output/{problem_code}.txt"
    code_history_dst = f"source_history/{problem_code}_{timestring}_{selected_solution_id}.py"
    output_history_dst = f"output_history/{problem_code}_{timestring}_{selected_solution_id}.txt"
    judgement_dst = f"logs/judgement/{problem_code}_{timestring}_{selected_solution_id}.txt"

    os.makedirs(f'response', exist_ok=True)
    os.makedirs(f'output', exist_ok=True)
    os.makedirs(f'source', exist_ok=True)
    os.makedirs(f'output_history', exist_ok=True)
    os.makedirs(f'source_history', exist_ok=True)
    os.makedirs(f'logs/judgement', exist_ok=True)

    import shutil

    if os.path.exists(response_src):
        shutil.copy(response_src, response_dst)

    if os.path.exists(code_src):
        shutil.copy(code_src, code_dst)

    if os.path.exists(output_src):
        shutil.copy(output_src, output_dst)

    if os.path.exists(code_src):
        shutil.copy(code_src, code_history_dst)

    if os.path.exists(output_src):
        shutil.copy(output_src, output_history_dst)

    with open('./hash_analyzed', 'a') as f:
        f.write(solutions_dict["hash"] + "\n")

    with open(judgement_dst, 'w') as f:
        f.write(openai_judgment)

    print(f"Selected solution {selected_solution_id} for {problem_code}")
    return openai_judgment, selected_solution_id
import re
import os
from textwrap import dedent

import modal

from openai import OpenAI
client = OpenAI()


def problem_name_to_problem_code(problem_name: str) -> str:
    problem_code = problem_name.lower().replace(" ", "_").replace("(", "").replace(")", "")
    return problem_code


def get_first_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content


def extract_python_code(response_string):
    pattern = r'```python\s*(.*?)\s*```'
    matches = re.findall(pattern, response_string, re.DOTALL)
    python_code = '\n\n'.join(matches)
    return python_code


def solve(contest_folder, password, problem_name, solution_id):

    problem_code = problem_name_to_problem_code(problem_name)

    os.makedirs(f'execution_sample_out/{problem_code}', exist_ok=True)
    os.makedirs(f'execution_full_out/{problem_code}', exist_ok=True)
    os.makedirs(f'execution_code/{problem_code}', exist_ok=True)

    with open(f"{contest_folder}/{problem_name}/statement.txt") as f:
        statement = f.read()
    with open(f"{contest_folder}/{problem_name}/sample_in.txt") as f:
        sample_in = f.read()
    with open(f"{contest_folder}/{problem_name}/sample_out.txt") as f:
        sample_out = f.read()
    with open(f"{contest_folder}/{problem_name}/full_in.txt") as f:
        full_in = f.read()

    prompt = dedent("""
    Write Python code to solve this problem

    {statement}

    This is the sample input

    {sample_in}

    This is the sample output

    {sample_out}

    The Python code, when executed, will take standard input and prints to standard output.

    Put the Python code within ```python and ```
    """).format(statement=statement, sample_in=sample_in, sample_out=sample_out)

    response = get_first_response(prompt)
    python_code = extract_python_code(response)
    with open(f"execution_code/{problem_code}/{solution_id}.py", "w") as f:
        f.write(python_code)

    execute_code = modal.Function.lookup("hackercup", "execute_code")

    sample_executed_output, sample_executed_error = execute_code.remote(python_code, sample_in)
    if sample_executed_error:
        sample_executed_output += "Error:\n" + sample_executed_error
    with open(f"execution_sample_out/{problem_code}/{solution_id}.txt", "w") as f:
        f.write(sample_executed_output)

    full_executed_output, full_executed_error = execute_code.remote(python_code, full_in)
    if sample_executed_error:
        full_executed_output += "Error:\n" + full_executed_error
    with open(f"execution_full_out/{problem_code}/{solution_id}.txt", "w") as f:
        f.write(full_executed_output)

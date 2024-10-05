import re
import os
from textwrap import dedent

import modal

from openai import OpenAI
client = OpenAI()


def problem_name_to_problem_code(problem_name: str) -> str:
    problem_code = problem_name.lower().replace(" ", "_").replace("(", "").replace(")", "")
    return problem_code


def get_first_response(prompt, model="o1-mini"):
    completion = client.chat.completions.create(
        # model="gpt-4o-mini",
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content


## Backup call
# import anthropic
# client = anthropic.Anthropic()
# message = client.messages.create(
#     model="claude-3-5-sonnet-20240620",
#     max_tokens=2048,
#     messages=[
#         {"role": "user", "content": "Hello, Claude"}
#     ]
# )
# print(message.content[0].text)


def extract_python_code(response_string):
    pattern = r'```python\s*(.*?)\s*```'
    matches = re.findall(pattern, response_string, re.DOTALL)
    python_code = '\n\n'.join(matches)
    return python_code


generation_prompt = """
Solve this problem with Python code

{statement}

This is the sample input

{sample_in}

This is the sample output

{sample_out}

The Python code, when executed, will take standard input and prints to standard output.

Write key findings when solving this problem.

Then, put the Python code within

```python

and

```
""".strip()


def solve(contest_folder, password, problem_name, solution_id):

    problem_code = problem_name_to_problem_code(problem_name)

    os.makedirs(f'execution_response/{problem_code}', exist_ok=True)
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

    prompt = generation_prompt.format(statement=statement, sample_in=sample_in, sample_out=sample_out)

    model = "o1-mini"
    if solution_id == "001" or solution_id == "005":
        model = "o1-preview"
    response = get_first_response(prompt, model=model)
    with open(f"execution_response/{problem_code}/{solution_id}.md", "w") as f:
        f.write(response)

    python_code = extract_python_code(response)
    with open(f"execution_code/{problem_code}/{solution_id}.py", "w") as f:
        f.write(python_code)

    execute_code = modal.Function.lookup("hackercup2", "execute_code")

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

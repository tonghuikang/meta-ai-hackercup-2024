"""

Helper function to execute Python code

modal deploy function_exec.py
modal app stop hackercup && modal deploy function_exec.py
"""

import subprocess
import tempfile
import os

from modal import App, Image

image = Image.debian_slim().pip_install(
    "scipy",
).copy_local_file("practice.zip")
# TODO also upload encrypted content materials


app = App("hackercup3")


@app.function(image=image, timeout=500, container_idle_timeout=1200)
def execute_code(code_str, input_str) -> tuple[str, str]:
    with tempfile.NamedTemporaryFile('w+', suffix='.py', delete=False) as tmp_file:
        tmp_file.write(code_str)
        tmp_file_path = tmp_file.name

    try:
        result = subprocess.run(
            ['python', '-u', tmp_file_path],
            input=input_str,
            text=True,
            capture_output=True,
            timeout=450  # Set a timeout to prevent infinite execution
        )
        if result.stderr:
            return result.stdout, result.stderr
        return result.stdout, result.stderr

    except subprocess.TimeoutExpired as e:
        return e.stdout.decode() if e.stdout else "", "Code execution timed out."
    finally:
        os.remove(tmp_file_path)
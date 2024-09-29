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
    "fastapi-poe==0.0.23",
    "huggingface-hub==0.16.4",
    "ipython",
    "scipy",
    "matplotlib",
    "scikit-learn",
    "pandas==1.3.2",
    "ortools",
    "torch",
    "torchvision",
    "tensorflow",
    "spacy",
    "transformers",
    "opencv-python-headless",
    "nltk",
    "openai",
    "requests",
    "beautifulsoup4",
    "newspaper3k",
    "feedparser",
    "sympy",
    "tensorflow",
    "cartopy",
    "wordcloud",
    "gensim",
    "keras",
    "librosa",
    "XlsxWriter",
    "docx2txt",
    "markdownify",
    "pdfminer.six",
    "Pillow",
    "opencv-python",
    "sortedcontainers",
    "intervaltree",
    "geopandas",
    "basemap",
    "tiktoken",
    "basemap-data-hires",
    "yfinance",
    "dill",
).copy_local_file("practice.zip")
# TODO also upload encrypted content materials


app = App("hackercup")


@app.function(image=image, timeout=30, container_idle_timeout=1200)
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
            timeout=5  # Set a timeout to prevent infinite execution
        )
        if result.stderr:
            return result.stdout, result.stderr
        return result.stdout, result.stderr

    except subprocess.TimeoutExpired as e:
        return e.stdout.decode() if e.stdout else "", "Error: Code execution timed out."
    finally:
        os.remove(tmp_file_path)
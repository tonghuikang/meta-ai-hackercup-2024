# Meta Hackercup AI track participation

https://www.facebook.com/codingcompetitions/hacker-cup/2024/final-round/scoreboard?track=AI_CLOSED_TRACK

Automated system for solving Meta Hacker Cup competitive programming problems using LLMs.

## How It Works

1. Extracts encrypted contest data (7-Zip with password)
2. Generates 40 parallel Python solutions per problem using OpenAI o1-mini/o1-preview
3. Executes solutions remotely via Modal.com against sample and full test inputs
4. Uses LLM judge to select best solution from all attempts
5. Saves selected solution to `source/` and execution output to `output/`

## Key Files

- `execution.ipynb` - Main orchestration (extract data, generate solutions)
- `monitoring.ipynb` - Real-time progress dashboard
- `worker.py` - Solution generation via OpenAI API
- `analysis.py` - Solution evaluation and selection
- `evaluation.ipynb` - Historical performance analysis

## Directory Structure

- `execution_*/` - Current run artifacts (code, outputs, responses)
- `evaluation_artifacts/` - Historical timestamped runs
- `source/` - Best selected solutions
- `output/` - Contest submission outputs
- `logs/judgement/` - LLM judge decisions

## Requirements

Environment variables:
- `OPENAI_API_KEY` - Primary LLM for generation/judging
- Modal.com account - Remote code execution

## Monitoring

- Live: `monitoring.ipynb` ([nbviewer](https://nbviewer.org/github/tonghuikang/meta-ai-hackercup-2024/blob/master/monitoring.ipynb))
- Remote execution: Modal.com dashboard

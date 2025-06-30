# Ollama Response Consistency Checker

This script performs 1,000 deterministic completions using the `phi4-mini-reasoning:latest` model via Ollama Python SDK and checks all responses for consistency.

## Prerequisites

- [Ollama](https://ollama.ai) installed and daemon running  
- Pulled model:  
  ```bash
  ollama pull phi4-mini-reasoning:latest
````

* Python 3.8+
* Virtual environment (recommended)

## Setup

```bash
python3 -m venv .venv
# On WSL / macOS / Linux:
source .venv/bin/activate
pip install -U ollama
```

## Usage

Rename your script to `test.py`. Activate the venv and run:

```bash
source .venv/bin/activate
python test.py
```

Expected output:

* `All 1000 responses are identical.`
  or
* A list/count of unique responses

## How It Works

1. Uses `chat()` from Ollama Python SDK with `options={"temperature": 0.0}` for deterministic output.
2. Repeats a simple prompt 1,000 times, storing each response.
3. Checks whether all entries are identical.

## Extending

* Switch to a different model
* Test with `generate()` for completion-style behavior
* Adjust prompt or run count to meet your needs

## License

Unlicense

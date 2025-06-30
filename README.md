# Ollama Response Consistency Checker

Runs 1,000 deterministic queries using Ollama’s `phi4-mini-reasoning:latest` model and verifies that all responses are identical.

## 📋 Table of Contents

* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Usage](#usage)
* [How it works](#how-it-works)
* [Customization](#customization)
* [Contributing](#contributing)
* [License](#license)

---

## Overview

This script (`test.py`) confirms the deterministic behavior of local Ollama models by repeatedly sending the same prompt (1,000 times) and comparing the outputs for consistency.

---

## Prerequisites

* Ollama installed and running

  ```bash
  ollama pull phi4-mini-reasoning:latest
  ```
* Python 3.8+ installed with `venv` module
* Recommended OS: Linux, macOS, WSL, or other Unix-like

---

## Setup

1. Create and activate virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -U ollama
   ```

---

## Usage

1. Ensure your script is named `test.py` in the project root.
2. Run the consistency check:

   ```bash
   source .venv/bin/activate
   python test.py
   ```

Output is either:

* `All 1000 responses are identical.`, or
* `Responses differ: X unique outputs.`

---

## How it works

* Uses `chat()` from the Ollama Python SDK with `options={"temperature": 0.0}` for fully deterministic output
* Loops 1,000 times, saves each response to a list
* Compares list entries to ensure uniformity

---

## Customization

* Change the model by modifying `model_name` in `test.py`
* Swap to `generate()` for completion-based models
* Modify run count, prompt, or add additional metrics (e.g. timing)

---

## Contributing

Contributions welcome! To report issues or suggest improvements:

* Fork the repo
* Add tests or examples
* Submit a PR

---

## License

Unlicense

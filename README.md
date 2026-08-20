# playwrightPython

Minimal test automation framework using **Python + Playwright**.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run tests

```bash
pytest
```

## Project structure

- `framework/browser.py`: central Playwright bootstrap helper
- `tests/test_framework_setup.py`: smoke test validating framework wiring

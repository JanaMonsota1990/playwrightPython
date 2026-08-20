# playwrightPython

Minimal test automation framework using **Python + Playwright**.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
playwright install
```

## Run tests

```bash
pytest
```

## Project structure

- `framework/browser.py`: central Playwright bootstrap helper
- `tests/test_framework_setup.py`: smoke test validating framework wiring

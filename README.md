## quiz

Simple Python project scaffold created in `src/` with tests in `tests/`.

### Structure

- `src/` – application code
- `src/main.py` – example entry point
- `tests/` – test suite using `pytest`
- `requirements.txt` – Python dependencies

### Setup

1. **Create and activate a virtual environment** (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

### Running the app

From the project root:

```bash
python -m src.main
```

You should see:

```text
Hello from quiz!
```

### Running tests

From the project root:

```bash
pytest
```


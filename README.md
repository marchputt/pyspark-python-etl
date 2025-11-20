# simplepyetl

Boilerplate ETL project using PySpark

## Installation

```bash
pip install -e .
```

## Development Setup

1. Create virtual environment
2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
3. Install package in editable mode:
   ```bash
   pip install -e .
   ```

## Usage

```python
from simplepyetl import split_first_last_name
```

## Testing

Run tests:
```bash
python -m unittest discover -s tests
```

## GitHub Actions

Automated unit testing runs on push and pull requests via `.github/workflows/test_unittest.yaml`.

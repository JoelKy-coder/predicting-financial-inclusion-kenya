# Contributing

Contributions should preserve the project goal: a clear, reproducible, evidence-based machine learning case study using the official FinAccess 2024 Household Survey.

## Development

1. Create a virtual environment.
2. Install dependencies with `python -m pip install -r requirements.txt`.
3. Place the raw workbook in `data/raw/`.
4. Run `pytest` before opening a pull request.
5. Format Python code with `black` and `isort`.

## Data

Do not commit raw survey files, generated model binaries, or large report artifacts. Document how to reproduce them instead.

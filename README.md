# Predicting Barriers to Financial Inclusion Among Rural Youth in Kenya

This repository is an end-to-end machine learning classification case study using the official FinAccess 2024 Household Survey. The project predicts whether rural youth aged 18-35 are financially excluded and translates the analysis into practical recommendations for policymakers and financial-service providers.

## Background

Kenya is a global leader in mobile money and digital financial services, yet exclusion remains an issue for some rural youth. This project uses survey evidence to examine how demographics, education, employment, and digital access relate to exclusion from formal and informal financial services.

## Problem Statement

Build a reproducible binary classification workflow that predicts financial exclusion among rural Kenyan youth and identifies the most important barriers associated with exclusion.

Target variable:

- `0`: financially included
- `1`: financially excluded

The target is created from the survey field `Overall_Access_fnl`, where records marked `excluded` are treated as financially excluded.

## Dataset

Source: FinAccess Kenya Reports and Datasets  
https://finaccess.knbs.or.ke/reports-and-datasets

Expected local file:

```text
data/raw/2024_Finaccess_Publicdata.xlsx
```

The raw workbook is intentionally ignored by Git because it is large. Download it from the official FinAccess site and place it in `data/raw/` before running the pipeline.

## Repository Structure

```text
.github/workflows/        CI configuration
data/raw/                 Local raw survey files, ignored by Git
data/processed/           Reproducible processed outputs
docs/                     Methodology and project notes
models/                   Saved model pipeline artifacts
notebooks/                Guided case-study notebooks
reports/figures/          Generated visualizations
reports/tables/           Data dictionaries, metrics, and metadata
src/                      Reusable Python modules
tests/                    Pytest suite
```

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Usage

Train and compare models on a reproducible sample:

```bash
python -m src.train --sample-size 2000
```

Run against the full workbook:

```bash
python -m src.train --sample-size 0
```

Run tests:

```bash
pytest
```

## Machine Learning Workflow

1. Inspect the FinAccess workbook and variable metadata.
2. Filter to rural respondents aged 18-35.
3. Create the binary financial-exclusion target.
4. Engineer interpretable demographic, employment, and digital-access features.
5. Prevent leakage by excluding direct financial-service access indicators from predictors.
6. Train baseline, Logistic Regression, Decision Tree, Random Forest, and tuned Random Forest models.
7. Compare models using accuracy, precision, recall, F1, and ROC AUC.
8. Save the best model pipeline and reproducible report tables.

## Results

Generated results are saved to:

- `reports/tables/model_comparison.csv`
- `reports/tables/training_metadata.json`
- `models/best_model.joblib`

Because the raw dataset is not committed, metrics should be regenerated locally after the workbook is added.

## Policy Recommendations

Recommendations should be interpreted from regenerated results. The project is designed to evaluate whether barriers such as limited education, unstable income sources, weak mobile ownership, limited internet access, and geographic location are associated with exclusion.

## Limitations

The analysis is based on cross-sectional survey data, so it identifies associations rather than causal effects. Results also depend on survey measurement quality, missing data patterns, and the representativeness of rural youth responses in the public dataset.

## References

- FinAccess Kenya Reports and Datasets
- Central Bank of Kenya
- Kenya National Bureau of Statistics
- Financial Sector Deepening Kenya
- Microsoft ML-For-Beginners
- Scikit-learn, Pandas, NumPy, and Matplotlib documentation

## License

MIT License

## Author

JoelKy-coder

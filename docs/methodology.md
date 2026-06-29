# Methodology

## Population

The analysis focuses on respondents who meet both conditions:

- `A08 == "Rural"`
- `A18` between 18 and 35 inclusive

## Target Definition

The binary target `financially_excluded` is derived from `Overall_Access_fnl`.

- `1`: `Overall_Access_fnl` equals `excluded`
- `0`: all other access categories

This uses an existing FinAccess access-strand summary rather than inventing a target from unrelated survey fields.

## Leakage Control

Direct financial access and usage indicators are kept for inspection but excluded from model predictors. Excluded fields include `Access_fnl`, `formal_access_fnl`, `mobile_money_access`, `mobile_money_access_primary`, and `Overall_Access_fnl`.

## Predictor Groups

Predictors are selected from demographic, socioeconomic, and digital-access fields:

- County
- Sex
- Education
- Age
- Employment/income-source flags
- Mobile phone ownership
- Internet access
- Mobile network quality
- Ability to use apps for services

## Models

The project compares:

- Dummy baseline
- Logistic Regression
- Decision Tree
- Random Forest
- Tuned Random Forest

The preferred model is selected by F1 score because the positive class is financial exclusion and false negatives can matter for targeting interventions.

# Reflection

This project turns a large public survey workbook into a reproducible machine learning case study. The main engineering challenge is balancing portfolio-quality analysis with practical reproducibility: the workbook is too large for normal GitHub storage, so the repository documents the data source and keeps raw files local.

The main modeling challenge is leakage. FinAccess includes many direct financial-access fields. Those fields are useful for defining and understanding the target, but using them as predictors would overstate model performance. The implemented pipeline therefore focuses predictors on demographics, education, employment, and digital-access factors.

Future work should run the pipeline on the full workbook, expand interpretation with permutation importance or SHAP, and add an interactive dashboard for county-level exploration.

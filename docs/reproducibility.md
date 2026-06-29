# Reproducibility Guide

1. Clone the repository.
2. Create a Python environment.
3. Install dependencies from `requirements.txt`.
4. Download `2024_Finaccess_Publicdata.xlsx` from the official FinAccess site.
5. Place the workbook in `data/raw/`.
6. Run `python -m src.train --sample-size 2000` for a fast reproducible pass.
7. Run `python -m src.train --sample-size 0` for the full workbook.
8. Review generated outputs in `reports/tables/`, `reports/figures/`, and `models/`.

Random seed `42` is used for train-test splitting and model training where supported.

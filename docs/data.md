# Data Notes

The raw FinAccess 2024 workbook is not committed to this repository because it is large and should be downloaded from the official source.

## Required File

```text
data/raw/2024_Finaccess_Publicdata.xlsx
```

## Source

FinAccess Kenya Reports and Datasets  
https://finaccess.knbs.or.ke/reports-and-datasets

## Metadata

The workbook contains:

- `2024_Finaccess_Publicdata`: public survey records
- `Variables`: variable names, source types, value-label references, and descriptions
- `Values`: label definitions

The project code reads the survey sheet and uses the metadata sheet to generate `reports/tables/data_dictionary.csv`.

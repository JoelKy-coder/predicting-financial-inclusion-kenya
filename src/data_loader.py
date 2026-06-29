"""Data loading and metadata helpers for the FinAccess 2024 workbook."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.utils import RAW_DATA_PATH

SURVEY_SHEET = "2024_Finaccess_Publicdata"
VARIABLES_SHEET = "Variables"

MODEL_COLUMNS = [
    "county",
    "A08",
    "A18",
    "Age",
    "Sex",
    "A20",
    "Education",
    "B3A__1",
    "B3A__2",
    "B3A__3",
    "B3A__4",
    "B3A__5",
    "B3A__6",
    "B3A__7",
    "B3A__8",
    "B3A__9",
    "B3A__10",
    "B3A__11",
    "B3A__98",
    "B3A__99",
    "S1",
    "S2__1",
    "S6",
    "S7_5",
    "mobile_money_access",
    "mobile_money_access_primary",
    "formal_access_fnl",
    "Access_fnl",
    "Overall_Access_fnl",
    "indWeight",
]


def require_workbook(path: Path = RAW_DATA_PATH) -> Path:
    """Return the workbook path or raise a clear setup error."""
    if not path.exists():
        raise FileNotFoundError(
            "FinAccess workbook not found. Download 2024_Finaccess_Publicdata.xlsx "
            f"from the official FinAccess site and place it at {path}."
        )
    return path


def load_survey_data(
    path: Path = RAW_DATA_PATH,
    columns: list[str] | None = None,
    nrows: int | None = None,
) -> pd.DataFrame:
    """Load selected survey columns from the FinAccess Excel workbook."""
    workbook = require_workbook(path)
    selected_columns = columns or MODEL_COLUMNS
    return pd.read_excel(
        workbook,
        sheet_name=SURVEY_SHEET,
        usecols=lambda column: column in selected_columns,
        nrows=nrows,
    )


def load_variable_metadata(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the variable-label metadata sheet from the workbook."""
    workbook = require_workbook(path)
    return pd.read_excel(workbook, sheet_name=VARIABLES_SHEET)


def build_data_dictionary(
    columns: list[str], path: Path = RAW_DATA_PATH
) -> pd.DataFrame:
    """Create a compact data dictionary for selected variables."""
    metadata = load_variable_metadata(path)
    dictionary = metadata.loc[
        metadata["name"].isin(columns), ["name", "type", "varlab"]
    ].copy()
    dictionary = dictionary.rename(
        columns={"name": "variable", "type": "source_type", "varlab": "description"}
    )
    dictionary["role"] = dictionary["variable"].map(
        lambda value: "Target" if value == "Overall_Access_fnl" else "Predictor"
    )
    return dictionary.sort_values("variable").reset_index(drop=True)

"""Feature engineering for rural youth financial exclusion modeling."""

from __future__ import annotations

import numpy as np
import pandas as pd

EMPLOYMENT_COLUMNS = {
    "farming": "B3A__1",
    "regular_employment": "B3A__2",
    "casual_work": "B3A__3",
    "self_employment": "B3A__4",
    "family_remittance": "B3A__9",
}

LEAKAGE_COLUMNS = {
    "mobile_money_access",
    "mobile_money_access_primary",
    "formal_access_fnl",
    "Access_fnl",
    "Overall_Access_fnl",
    "indWeight",
}


def filter_rural_youth(data: pd.DataFrame) -> pd.DataFrame:
    """Keep rural respondents aged 18 to 35, matching the project population."""
    filtered = data.loc[
        data["A08"].astype(str).str.lower().eq("rural")
        & data["A18"].between(18, 35, inclusive="both")
    ].copy()
    return filtered.reset_index(drop=True)


def create_financial_exclusion_target(data: pd.DataFrame) -> pd.DataFrame:
    """Create binary target: 1 for financially excluded, 0 otherwise."""
    if "Overall_Access_fnl" not in data.columns:
        raise KeyError("Overall_Access_fnl is required to create the target variable.")
    transformed = data.copy()
    transformed["financially_excluded"] = (
        transformed["Overall_Access_fnl"].astype(str).str.lower().str.strip()
        == "excluded"
    ).astype(int)
    return transformed


def create_employment_category(row: pd.Series) -> str:
    """Summarize multi-select income-source flags into one interpretable category."""
    if row.get("B3A__2", 0) == 1:
        return "regular_employment"
    if row.get("B3A__4", 0) == 1:
        return "self_employment"
    if row.get("B3A__3", 0) == 1:
        return "casual_work"
    if row.get("B3A__1", 0) == 1:
        return "farming"
    if row.get("B3A__9", 0) == 1:
        return "family_remittance"
    return "other_or_no_income_source"


def engineer_features(data: pd.DataFrame) -> pd.DataFrame:
    """Create modeling features from observed survey variables."""
    engineered = data.copy()
    engineered["age_years"] = pd.to_numeric(engineered["A18"], errors="coerce")
    engineered["age_group_youth"] = pd.cut(
        engineered["age_years"],
        bins=[17, 25, 30, 35],
        labels=["18-25", "26-30", "31-35"],
        include_lowest=True,
    ).astype("object")
    engineered["employment_category"] = engineered.apply(
        create_employment_category, axis=1
    )
    engineered["internet_access"] = np.where(
        pd.to_numeric(engineered["S2__1"], errors="coerce").eq(1), "yes", "no"
    )
    engineered["owns_private_mobile"] = np.where(
        engineered["S1"].astype(str).str.contains("only I use", case=False, na=False),
        "yes",
        "no",
    )
    engineered["digital_access_score"] = (
        engineered["internet_access"].eq("yes").astype(int)
        + engineered["owns_private_mobile"].eq("yes").astype(int)
        + engineered["S7_5"]
        .astype(str)
        .str.contains("ease|manage", case=False, na=False)
        .astype(int)
    )
    return engineered


def prepare_model_frame(data: pd.DataFrame) -> pd.DataFrame:
    """Apply project-specific filtering, target creation, and feature engineering."""
    rural_youth = filter_rural_youth(data)
    with_target = create_financial_exclusion_target(rural_youth)
    return engineer_features(with_target)


def get_model_features(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Return leakage-aware predictors and target for supervised learning."""
    target = data["financially_excluded"].astype(int)
    feature_columns = [
        "county",
        "Sex",
        "Education",
        "A20",
        "age_years",
        "age_group_youth",
        "employment_category",
        "internet_access",
        "owns_private_mobile",
        "S6",
        "S7_5",
        "digital_access_score",
    ]
    predictors = data[feature_columns].copy()
    return predictors, target

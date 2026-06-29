"""Tests for project-specific feature engineering."""

import pandas as pd

from src.feature_engineering import (
    create_financial_exclusion_target,
    filter_rural_youth,
    get_model_features,
    prepare_model_frame,
)


def sample_frame() -> pd.DataFrame:
    """Create a small survey-like frame for deterministic tests."""
    return pd.DataFrame(
        {
            "county": ["A", "B", "C"],
            "A08": ["Rural", "Urban", "Rural"],
            "A18": [22, 28, 40],
            "Age": ["18-25", "26-35", "36-45"],
            "Sex": ["Female", "Male", "Female"],
            "A20": ["Primary completed", "Secondary completed", "None"],
            "Education": ["Primary", "Secondary", "Other"],
            "B3A__1": [1, 0, 0],
            "B3A__2": [0, 1, 0],
            "B3A__3": [0, 0, 0],
            "B3A__4": [0, 0, 1],
            "B3A__5": [0, 0, 0],
            "B3A__6": [0, 0, 0],
            "B3A__7": [0, 0, 0],
            "B3A__8": [0, 0, 0],
            "B3A__9": [0, 0, 0],
            "B3A__10": [0, 0, 0],
            "B3A__11": [0, 0, 0],
            "B3A__98": [0, 0, 0],
            "B3A__99": [0, 0, 0],
            "S1": ["I own a mobile that only I use", "No phone", "No phone"],
            "S2__1": [1, 0, 0],
            "S6": ["Strong", "Weak", "Okay"],
            "S7_5": ["I can manage with ease", "I have no idea", "I can manage"],
            "mobile_money_access": ["Yes", "No", "No"],
            "mobile_money_access_primary": ["Yes", "No", "No"],
            "formal_access_fnl": ["No", "Yes", "No"],
            "Access_fnl": ["Excluded", "Formal Prudential", "Excluded"],
            "Overall_Access_fnl": ["excluded", "formal only", "excluded"],
            "indWeight": [1.0, 1.0, 1.0],
        }
    )


def test_filter_rural_youth_keeps_only_rural_18_to_35() -> None:
    filtered = filter_rural_youth(sample_frame())
    assert len(filtered) == 1
    assert filtered.loc[0, "A08"] == "Rural"
    assert filtered.loc[0, "A18"] == 22


def test_target_creation_marks_excluded_as_positive_class() -> None:
    transformed = create_financial_exclusion_target(sample_frame())
    assert transformed["financially_excluded"].tolist() == [1, 0, 1]


def test_prepare_model_frame_creates_expected_features() -> None:
    prepared = prepare_model_frame(sample_frame())
    assert "digital_access_score" in prepared.columns
    assert "employment_category" in prepared.columns
    assert prepared.loc[0, "financially_excluded"] == 1


def test_get_model_features_excludes_target_and_leakage_columns() -> None:
    prepared = prepare_model_frame(sample_frame())
    predictors, target = get_model_features(prepared)
    assert "Overall_Access_fnl" not in predictors.columns
    assert "mobile_money_access" not in predictors.columns
    assert target.name == "financially_excluded"

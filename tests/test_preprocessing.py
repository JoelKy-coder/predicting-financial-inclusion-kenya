"""Tests for preprocessing pipeline construction."""

import pandas as pd

from src.preprocessing import build_preprocessor, split_feature_types


def test_split_feature_types_identifies_numeric_and_categorical() -> None:
    frame = pd.DataFrame({"age": [20, 21], "county": ["A", "B"]})
    numeric_features, categorical_features = split_feature_types(frame)
    assert numeric_features == ["age"]
    assert categorical_features == ["county"]


def test_build_preprocessor_fits_mixed_data() -> None:
    frame = pd.DataFrame({"age": [20, None, 23], "county": ["A", "B", None]})
    preprocessor = build_preprocessor(frame)
    transformed = preprocessor.fit_transform(frame)
    assert transformed.shape[0] == 3

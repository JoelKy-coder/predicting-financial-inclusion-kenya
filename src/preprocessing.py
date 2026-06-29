"""Preprocessing pipeline builders for mixed survey data."""

from __future__ import annotations

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def split_feature_types(data: pd.DataFrame) -> tuple[list[str], list[str]]:
    """Identify numeric and categorical feature columns."""
    numeric_features = data.select_dtypes(include=["number"]).columns.tolist()
    categorical_features = [
        column for column in data.columns if column not in numeric_features
    ]
    return numeric_features, categorical_features


def build_preprocessor(data: pd.DataFrame) -> ColumnTransformer:
    """Build preprocessing that imputes, scales, and one-hot encodes predictors."""
    numeric_features, categorical_features = split_feature_types(data)
    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
        ]
    )
    return ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, numeric_features),
            ("categorical", categorical_pipeline, categorical_features),
        ]
    )

"""Evaluation and reporting utilities for trained models."""

from __future__ import annotations

import joblib
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay

from src.feature_engineering import get_model_features
from src.utils import FIGURES_DIR, MODELS_DIR


def load_best_model(path=MODELS_DIR / "best_model.joblib"):
    """Load the persisted best model pipeline."""
    return joblib.load(path)


def save_evaluation_plots(model, model_frame: pd.DataFrame) -> None:
    """Save confusion matrix and ROC plots for the provided model frame."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    predictors, target = get_model_features(model_frame)
    ConfusionMatrixDisplay.from_estimator(model, predictors, target)
    RocCurveDisplay.from_estimator(model, predictors, target)

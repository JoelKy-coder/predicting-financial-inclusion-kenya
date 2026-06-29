"""Prediction helpers for hypothetical rural-youth profiles."""

from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd

from src.utils import MODELS_DIR


def load_model(model_path: Path = MODELS_DIR / "best_model.joblib"):
    """Load a saved sklearn pipeline."""
    if not model_path.exists():
        raise FileNotFoundError("Run `python -m src.train` before making predictions.")
    return joblib.load(model_path)


def predict_exclusion(
    profile: dict, model_path: Path = MODELS_DIR / "best_model.joblib"
) -> dict:
    """Predict financial exclusion status and probability for one profile."""
    model = load_model(model_path)
    frame = pd.DataFrame([profile])
    probability = float(model.predict_proba(frame)[0, 1])
    prediction = int(model.predict(frame)[0])
    return {
        "financially_excluded": prediction,
        "exclusion_probability": probability,
    }

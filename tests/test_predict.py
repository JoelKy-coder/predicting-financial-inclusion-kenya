"""Tests for prediction helper error handling."""

from pathlib import Path

import pytest

from src.predict import load_model


def test_load_model_raises_clear_error_for_missing_artifact() -> None:
    with pytest.raises(FileNotFoundError, match="Run `python -m src.train`"):
        load_model(Path("missing.joblib"))

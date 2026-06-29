"""Shared utilities for paths, reproducibility, and file output."""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any

import numpy as np

RANDOM_STATE = 42
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_PATH = DATA_DIR / "raw" / "2024_Finaccess_Publicdata.xlsx"
PROCESSED_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"
TABLES_DIR = PROJECT_ROOT / "reports" / "tables"


def set_random_seed(seed: int = RANDOM_STATE) -> None:
    """Set random seeds used by Python and NumPy."""
    random.seed(seed)
    np.random.seed(seed)


def ensure_directories() -> None:
    """Create output directories used by scripts."""
    for directory in [PROCESSED_DIR, MODELS_DIR, FIGURES_DIR, TABLES_DIR]:
        directory.mkdir(parents=True, exist_ok=True)


def write_json(payload: dict[str, Any], path: Path) -> None:
    """Write a JSON file with stable formatting."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

"""Visualization helpers used by notebooks and reports."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_bar_chart(
    series: pd.Series,
    title: str,
    xlabel: str,
    ylabel: str,
    output_path: Path,
) -> None:
    """Save a sorted bar chart from a Pandas Series."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    ax = series.sort_values().plot(kind="barh", figsize=(8, 5))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(output_path, dpi=160)
    plt.close()

"""Train and compare classification models for financial exclusion."""

from __future__ import annotations

import argparse
import json

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier

from src.data_loader import MODEL_COLUMNS, build_data_dictionary, load_survey_data
from src.feature_engineering import get_model_features, prepare_model_frame
from src.preprocessing import build_preprocessor
from src.utils import MODELS_DIR, PROCESSED_DIR, TABLES_DIR, ensure_directories


def evaluate_predictions(y_true, y_pred, y_score=None) -> dict[str, float]:
    """Compute classification metrics with exclusion as the positive class."""
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
    }
    if y_score is not None and len(set(y_true)) > 1:
        metrics["roc_auc"] = roc_auc_score(y_true, y_score)
    return metrics


def build_model_pipelines(x_train: pd.DataFrame) -> dict[str, Pipeline]:
    """Create baseline and candidate model pipelines."""
    preprocessor = build_preprocessor(x_train)
    return {
        "dummy": Pipeline(
            [
                ("preprocess", preprocessor),
                ("model", DummyClassifier(strategy="most_frequent")),
            ]
        ),
        "logistic_regression": Pipeline(
            [
                ("preprocess", preprocessor),
                (
                    "model",
                    LogisticRegression(
                        max_iter=1000,
                        class_weight="balanced",
                        random_state=42,
                    ),
                ),
            ]
        ),
        "decision_tree": Pipeline(
            [
                ("preprocess", preprocessor),
                (
                    "model",
                    DecisionTreeClassifier(
                        max_depth=5,
                        min_samples_leaf=20,
                        class_weight="balanced",
                        random_state=42,
                    ),
                ),
            ]
        ),
        "random_forest": Pipeline(
            [
                ("preprocess", preprocessor),
                (
                    "model",
                    RandomForestClassifier(
                        n_estimators=120,
                        max_depth=8,
                        min_samples_leaf=10,
                        class_weight="balanced",
                        random_state=42,
                        n_jobs=1,
                    ),
                ),
            ]
        ),
    }


def tune_random_forest(x_train: pd.DataFrame, y_train: pd.Series) -> GridSearchCV:
    """Tune a Random Forest with a compact reproducible grid."""
    pipeline = build_model_pipelines(x_train)["random_forest"]
    grid = {
        "model__n_estimators": [100, 150],
        "model__max_depth": [6, 10],
        "model__min_samples_leaf": [5, 15],
    }
    search = GridSearchCV(
        pipeline,
        param_grid=grid,
        scoring="f1",
        cv=StratifiedKFold(n_splits=3, shuffle=True, random_state=42),
        n_jobs=1,
    )
    search.fit(x_train, y_train)
    return search


def save_feature_importance(
    model: Pipeline,
    output_csv=TABLES_DIR / "feature_importance.csv",
    output_png=TABLES_DIR.parent / "figures" / "feature_importance.png",
) -> pd.DataFrame:
    """Save feature importance or absolute coefficients for the selected model."""
    estimator = model.named_steps["model"]
    feature_names = model.named_steps["preprocess"].get_feature_names_out()
    if hasattr(estimator, "feature_importances_"):
        importance_values = estimator.feature_importances_
    elif hasattr(estimator, "coef_"):
        importance_values = abs(estimator.coef_[0])
    else:
        return pd.DataFrame()

    importance = pd.DataFrame(
        {"feature": feature_names, "importance": importance_values}
    ).sort_values("importance", ascending=False)
    importance.to_csv(output_csv, index=False)

    top_features = importance.head(15).sort_values("importance")
    axis = top_features.plot(
        kind="barh",
        x="feature",
        y="importance",
        legend=False,
        figsize=(9, 6),
        title="Top Model Features",
    )
    axis.set_xlabel("Importance")
    axis.set_ylabel("Feature")
    plt.tight_layout()
    plt.savefig(output_png, dpi=160)
    plt.close()
    return importance


def train_project(sample_size: int | None = 2000) -> dict[str, object]:
    """Run the end-to-end training workflow and persist outputs."""
    ensure_directories()
    raw_data = load_survey_data(columns=MODEL_COLUMNS, nrows=sample_size)
    model_frame = prepare_model_frame(raw_data)
    predictors, target = get_model_features(model_frame)
    x_train, x_test, y_train, y_test = train_test_split(
        predictors,
        target,
        test_size=0.2,
        random_state=42,
        stratify=target,
    )

    model_rows = []
    fitted_models = {}
    for name, pipeline in build_model_pipelines(x_train).items():
        pipeline.fit(x_train, y_train)
        predictions = pipeline.predict(x_test)
        scores = (
            pipeline.predict_proba(x_test)[:, 1]
            if hasattr(pipeline.named_steps["model"], "predict_proba")
            else None
        )
        fitted_models[name] = pipeline
        row = {"model": name}
        row.update(evaluate_predictions(y_test, predictions, scores))
        model_rows.append(row)

    tuned_search = tune_random_forest(x_train, y_train)
    tuned_model = tuned_search.best_estimator_
    tuned_predictions = tuned_model.predict(x_test)
    tuned_scores = tuned_model.predict_proba(x_test)[:, 1]
    tuned_row = {"model": "random_forest_tuned"}
    tuned_row.update(evaluate_predictions(y_test, tuned_predictions, tuned_scores))
    model_rows.append(tuned_row)
    fitted_models["random_forest_tuned"] = tuned_model

    comparison = pd.DataFrame(model_rows).sort_values("f1", ascending=False)
    best_model_name = str(comparison.iloc[0]["model"])
    best_model = fitted_models[best_model_name]

    model_frame.to_csv(PROCESSED_DIR / "rural_youth_model_frame.csv", index=False)
    comparison.to_csv(TABLES_DIR / "model_comparison.csv", index=False)
    build_data_dictionary(MODEL_COLUMNS).to_csv(
        TABLES_DIR / "data_dictionary.csv", index=False
    )
    joblib.dump(best_model, MODELS_DIR / "best_model.joblib")
    save_feature_importance(best_model)

    metadata = {
        "sample_size": sample_size,
        "rows_after_rural_youth_filter": int(len(model_frame)),
        "target_distribution": target.value_counts().to_dict(),
        "best_model": best_model_name,
        "best_params": getattr(tuned_search, "best_params_", {}),
        "feature_columns": predictors.columns.tolist(),
    }
    (TABLES_DIR / "training_metadata.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )
    return {"comparison": comparison, "metadata": metadata}


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sample-size",
        type=int,
        default=2000,
        help="Rows to read from the large workbook. Use 0 for the full file.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    requested_sample_size = None if args.sample_size == 0 else args.sample_size
    result = train_project(sample_size=requested_sample_size)
    print(result["comparison"].to_string(index=False))

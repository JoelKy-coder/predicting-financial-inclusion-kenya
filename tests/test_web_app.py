"""Tests for the lightweight web prediction app."""

import app as app_module
from app import app, build_profile_from_form, create_prediction_response


def test_build_profile_from_form_casts_numeric_values() -> None:
    form_data = {
        "county": "Kisumu",
        "sex": "Female",
        "education": "Secondary",
        "a20": "Secondary completed",
        "age_years": "24",
        "age_group_youth": "18-25",
        "employment_category": "self_employment",
        "internet_access": "yes",
        "owns_private_mobile": "yes",
        "s6": "Strong",
        "s7_5": "I can manage",
        "digital_access_score": "3",
    }

    profile = build_profile_from_form(form_data)

    assert profile["age_years"] == 24
    assert profile["digital_access_score"] == 3
    assert profile["county"] == "Kisumu"


def test_create_prediction_response_returns_prediction_summary() -> None:
    response = create_prediction_response(
        {
            "county": "Kisumu",
            "Sex": "Female",
            "Education": "Secondary",
            "A20": "Secondary completed",
            "age_years": 24,
            "age_group_youth": "18-25",
            "employment_category": "self_employment",
            "internet_access": "yes",
            "owns_private_mobile": "yes",
            "S6": "Strong",
            "S7_5": "I can manage",
            "digital_access_score": 3,
        }
    )

    assert set(response) == {
        "financially_excluded",
        "exclusion_probability",
        "label",
        "css_class",
    }
    assert response["label"] in {"Financially excluded", "Not financially excluded"}


def test_build_profile_from_form_handles_invalid_numeric_input() -> None:
    profile = build_profile_from_form({"age_years": "not-a-number", "digital_access_score": "oops"})

    assert profile["age_years"] == 0
    assert profile["digital_access_score"] == 0


def test_health_endpoint_returns_status() -> None:
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_create_prediction_response_handles_model_failure(monkeypatch) -> None:
    def raise_error(_profile):
        raise FileNotFoundError("Model artifact is missing")

    monkeypatch.setattr(app_module, "predict_exclusion", raise_error)
    response = create_prediction_response({"age_years": 24})

    assert response["financially_excluded"] is None
    assert response["exclusion_probability"] is None
    assert response["error"] == "Model artifact is missing"

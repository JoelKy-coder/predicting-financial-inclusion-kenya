"""A lightweight web app for predicting financial exclusion risk."""

from __future__ import annotations

from typing import Any

from flask import Flask, jsonify, render_template_string, request

from src.predict import predict_exclusion

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>Financial Inclusion Predictor</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 780px; margin: 2rem auto; padding: 1rem; line-height: 1.5; background: #f8fafc; color: #0f172a; }
    .card { background: white; padding: 1.4rem; border-radius: 12px; box-shadow: 0 8px 30px rgba(15, 23, 42, 0.08); }
    form { display: grid; gap: 0.8rem; }
    label { font-weight: 600; }
    input, select { padding: 0.6rem; font-size: 1rem; border: 1px solid #cbd5e1; border-radius: 6px; }
    button { padding: 0.7rem 1rem; font-size: 1rem; cursor: pointer; background: #2563eb; color: white; border: none; border-radius: 6px; }
    .result { margin-top: 1.2rem; padding: 1rem; border-radius: 8px; background: #f5f7fb; }
    .danger { color: #b42318; font-weight: 700; }
    .safe { color: #067647; font-weight: 700; }
    .hint { color: #475569; font-size: 0.95rem; }
  </style>
</head>
<body>
  <div class=\"card\">
  <h1>Financial Inclusion Predictor</h1>
  <p class=\"hint\">Estimate whether a rural youth profile is likely to be financially excluded.</p>
  <form method=\"post\" action=\"/predict\">
    <label>County</label>
    <input name=\"county\" value=\"Kisumu\" required>

    <label>Sex</label>
    <select name=\"sex\">
      <option value=\"Female\">Female</option>
      <option value=\"Male\">Male</option>
    </select>

    <label>Education</label>
    <select name=\"education\">
      <option value=\"Primary\">Primary</option>
      <option value=\"Secondary\">Secondary</option>
      <option value=\"Tertiary\">Tertiary</option>
    </select>

    <label>A20</label>
    <input name=\"a20\" value=\"Secondary completed\" required>

    <label>Age</label>
    <input name=\"age_years\" type=\"number\" value=\"24\" required>

    <label>Age Group</label>
    <select name=\"age_group_youth\">
      <option value=\"18-25\">18-25</option>
      <option value=\"26-30\">26-30</option>
      <option value=\"31-35\">31-35</option>
    </select>

    <label>Employment Category</label>
    <select name=\"employment_category\">
      <option value=\"self_employment\">Self employment</option>
      <option value=\"regular_employment\">Regular employment</option>
      <option value=\"casual_work\">Casual work</option>
      <option value=\"farming\">Farming</option>
      <option value=\"family_remittance\">Family remittance</option>
      <option value=\"other_or_no_income_source\">Other / no income source</option>
    </select>

    <label>Internet Access</label>
    <select name=\"internet_access\">
      <option value=\"yes\">Yes</option>
      <option value=\"no\">No</option>
    </select>

    <label>Owns Private Mobile</label>
    <select name=\"owns_private_mobile\">
      <option value=\"yes\">Yes</option>
      <option value=\"no\">No</option>
    </select>

    <label>S6</label>
    <input name=\"s6\" value=\"Strong\" required>

    <label>S7_5</label>
    <input name=\"s7_5\" value=\"I can manage\" required>

    <label>Digital Access Score</label>
    <input name=\"digital_access_score\" type=\"number\" value=\"3\" required>

    <button type=\"submit\">Predict</button>
  </form>
  {% if result %}
  <div class=\"result\">
    <h2>Prediction</h2>
    <p class=\"{{ result['css_class'] }}\">{{ result['label'] }}</p>
    <p>Probability of financial exclusion: {{ \"%.2f\"|format(result['exclusion_probability']) }}</p>
  </div>
  {% endif %}
  </div>
</body>
</html>
"""


def _coerce_int(value: Any, default: int = 0) -> int:
    """Safely parse an integer from user input."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def build_profile_from_form(form_data: dict[str, Any]) -> dict[str, Any]:
    """Convert form values into the profile structure expected by the trained model."""
    return {
        "county": form_data.get("county", ""),
        "Sex": form_data.get("sex", ""),
        "Education": form_data.get("education", ""),
        "A20": form_data.get("a20", ""),
        "age_years": _coerce_int(form_data.get("age_years")),
        "age_group_youth": form_data.get("age_group_youth", ""),
        "employment_category": form_data.get("employment_category", ""),
        "internet_access": form_data.get("internet_access", ""),
        "owns_private_mobile": form_data.get("owns_private_mobile", ""),
        "S6": form_data.get("s6", ""),
        "S7_5": form_data.get("s7_5", ""),
        "digital_access_score": _coerce_int(form_data.get("digital_access_score")),
    }


def create_prediction_response(profile: dict[str, Any]) -> dict[str, Any]:
    """Create a user-friendly prediction response for the web UI."""
    try:
        prediction = predict_exclusion(profile)
    except FileNotFoundError as exc:
        return {
            "financially_excluded": None,
            "exclusion_probability": None,
            "label": "Prediction unavailable",
            "css_class": "danger",
            "error": str(exc),
        }

    label = "Financially excluded" if prediction["financially_excluded"] else "Not financially excluded"
    css_class = "danger" if prediction["financially_excluded"] else "safe"
    return {
        "financially_excluded": prediction["financially_excluded"],
        "exclusion_probability": prediction["exclusion_probability"],
        "label": label,
        "css_class": css_class,
    }


@app.route("/", methods=["GET"])
def index() -> str:
    return render_template_string(HTML_TEMPLATE, result=None)


@app.route("/health", methods=["GET"])
def health() -> Any:
    return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def predict() -> str:
    profile = build_profile_from_form(request.form.to_dict())
    result = create_prediction_response(profile)
    return render_template_string(HTML_TEMPLATE, result=result)


@app.route("/api/predict", methods=["POST"])
def api_predict() -> Any:
    profile = build_profile_from_form(request.get_json(silent=True) or {})
    return jsonify(create_prediction_response(profile))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

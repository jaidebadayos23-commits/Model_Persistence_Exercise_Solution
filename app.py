from flask import Flask, request, jsonify
import joblib
from pathlib import Path

app = Flask(__name__)

@app.route("/")
def home():
    return "Student Performance Prediction API is running!"

MODEL_PATH = Path(__file__).with_name("student_pass_model.joblib")
model = joblib.load(MODEL_PATH)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Send a JSON object with study_hours and attendance_percentage."}), 400

    if "study_hours" not in data or "attendance_percentage" not in data:
        return jsonify({"error": "Both study_hours and attendance_percentage are required."}), 400

    try:
        study_hours = float(data["study_hours"])
        attendance = float(data["attendance_percentage"])
    except (TypeError, ValueError):
        return jsonify({"error": "study_hours and attendance_percentage must be numbers."}), 400

    if study_hours < 0:
        return jsonify({"error": "study_hours cannot be negative."}), 400

    if not 0 <= attendance <= 100:
        return jsonify({"error": "attendance_percentage must be between 0 and 100."}), 400

    # The current model uses only study_hours. Attendance is validated and returned,
    # but does not affect the prediction unless the model is retrained with both features.
    prediction_value = int(model.predict([[study_hours]])[0])
    prediction = "Pass" if prediction_value == 1 else "Fail"

    return jsonify({
        "study_hours": study_hours,
        "attendance_percentage": attendance,
        "prediction": prediction,
        "note": "Prediction currently uses study_hours only; attendance does not influence it."
    })


if __name__ == "__main__":
    app.run(debug=True)

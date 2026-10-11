from pathlib import Path
import joblib
import streamlit as st

MODEL_PATH = Path(__file__).with_name("student_pass_model.joblib")
model = joblib.load(MODEL_PATH)

st.title("Student Performance Prediction")
st.write("Enter a student's name and study hours to predict the result.")

student_name = st.text_input("Student name")
study_hours = st.number_input("Study hours", min_value=0.0, max_value=24.0, value=3.0, step=0.5)

if st.button("Predict"):
    if not student_name.strip():
        st.warning("Please enter the student's name.")
    else:
        prediction_value = int(model.predict([[study_hours]])[0])
        result = "Pass" if prediction_value == 1 else "Fail"

        st.subheader(f"Prediction for {student_name.strip()}")
        st.success(f"Predicted result: {result}" if result == "Pass" else f"Predicted result: {result}")

        st.caption(
            "How it was generated: the app sent the entered study hours to the saved "
            "machine-learning model, which learned patterns from its training data."
        )

        # Bonus chart: compare the entered study hours with the predicted class.
        st.subheader("Study Hours and Predicted Class")
        st.bar_chart({"Study hours": [study_hours]})
        st.write(f"Predicted class: **{result}**")

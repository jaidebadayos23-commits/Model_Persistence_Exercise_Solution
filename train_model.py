# Train and save the student pass/fail model.
# Replace the sample data below with the original dataset from your class project if provided.

import joblib
from sklearn.linear_model import LogisticRegression

# Sample data: study hours and exam result (0 = Fail, 1 = Pass)
X = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

# Exercise 1: save the trained model with a different filename.
model_filename = "student_pass_model.joblib"
joblib.dump(model, model_filename)
print(f"Model saved as {model_filename}")

# Load the saved model and make three predictions without retraining.
loaded_model = joblib.load(model_filename)

for study_hours in [2, 5, 8]:
    prediction = loaded_model.predict([[study_hours]])[0]
    result = "Pass" if prediction == 1 else "Fail"
    print(f"Study hours: {study_hours} -> Prediction: {result}")

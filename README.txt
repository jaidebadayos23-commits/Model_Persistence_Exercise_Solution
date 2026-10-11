MODEL PERSISTENCE AND BASIC DEPLOYMENT — EXERCISE SOLUTION

Files:
- train_model.py: trains a sample model, saves it as student_pass_model.joblib,
  loads it again, and makes three predictions.
- app.py: Flask API that accepts study_hours and attendance_percentage,
  validates attendance from 0 to 100, and returns JSON.
- streamlit_app.py: Streamlit interface with student name, study-hours input,
  Predict button, result, explanation, and a simple bonus chart.
- requirements.txt: Python packages.
- .gitignore: excludes virtual environments, cache files, Streamlit secrets/config,
  and the generated model file from Git.

IMPORTANT:
Only the three uploaded reference files were available; no original train_model.py,
dataset, app.py, or Streamlit starter file was provided. Therefore, train_model.py
uses a SMALL SAMPLE DATASET for demonstration. If your instructor gave your group
an original dataset or starter code, replace the sample data/model logic with that
material before submitting.

SETUP:
1. Open a terminal in this folder.
2. Install packages:
   pip install -r requirements.txt
3. Train and save the model:
   python train_model.py

RUN THE FLASK API:
4. Start the API:
   python app.py
5. In Postman, choose POST and use:
   http://127.0.0.1:5000/predict
   Select Body > raw > JSON and send:
   {
     "study_hours": 5,
     "attendance_percentage": 90
   }
   Or use Windows Command Prompt:
   curl.exe -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"study_hours\":5,\"attendance_percentage\":90}"

RUN STREAMLIT:
6. Open another terminal in the same folder:
   streamlit run streamlit_app.py

EXPLANATION FOR EXERCISE 1:
The model does not need to be trained again for each prediction because joblib.dump()
saves the trained model to a file and joblib.load() restores the learned model.
The loaded model can predict new inputs directly. Retraining is only needed when
you want to update the model with new or changed training data/features.

EXERCISE 2 NOTE:
The API accepts and validates attendance_percentage, but the provided model is
trained using study_hours only. Attendance is returned in the JSON response but
does not influence the prediction until the model is trained using both features.

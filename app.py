import streamlit as st
import pickle
import numpy as np
from utils import marks_to_gpa, give_suggestions

# Load model
model = pickle.load(open("model/model.pkl", "rb"))

st.set_page_config(page_title="Student Performance Predictor")

st.title("🎓 Student Performance Predictor & Advisor")

st.write("Enter your academic details below:")

# Inputs
study_hours = st.slider("Study Hours per Day", 0.0, 10.0, 2.0)
attendance = st.slider("Attendance (%)", 0, 100, 70)
assignments = st.slider("Assignment Score", 0, 100, 60)
previous_gpa = st.slider("Previous GPA", 0.0, 10.0, 7.0)

# Prediction
if st.button("Predict Performance"):

    input_data = np.array([[study_hours, attendance, assignments, previous_gpa]])
    
    predicted_marks = model.predict(input_data)[0]
    predicted_marks = round(predicted_marks, 2)

    gpa, grade = marks_to_gpa(predicted_marks)

    suggestions = give_suggestions(attendance, study_hours, assignments, predicted_marks)

    st.subheader("📊 Results")
    st.write(f"Predicted Marks: {predicted_marks}")
    st.write(f"Grade: {grade}")
    st.write(f"Estimated GPA: {gpa}")

    st.subheader("💡 Suggestions")
    for s in suggestions:
        st.write(f"- {s}")

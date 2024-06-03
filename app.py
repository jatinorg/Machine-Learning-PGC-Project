import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the model from the file
model = joblib.load('salary_prediction_model.pkl')

# Title
st.title("Salary Prediction App")

# Input fields
college = st.selectbox("College", ["Tier1", "Tier2", "Tier3"])
city = st.selectbox("City", ["Metro", "Non-Metro"])
previous_ctc = st.number_input("Previous CTC")
previous_job_change = st.number_input("Previous Job Change")
graduation_marks = st.number_input("Graduation Marks")
exp_month = st.number_input("Experience (Months)")
role_manager = st.selectbox("Role", ["Manager", "Executive"])

# Encode categorical inputs
college_map = {"Tier1": 1, "Tier2": 2, "Tier3": 3}
city_map = {"Metro": 1, "Non-Metro": 0}
role_manager_map = {"Manager": 1, "Executive": 0}

college_encoded = college_map[college]
city_encoded = city_map[city]
role_manager_encoded = role_manager_map[role_manager]

# Create a dataframe for the inputs
input_data = pd.DataFrame({
    'College': [college_encoded],
    'City': [city_encoded],
    'Previous CTC': [previous_ctc],
    'Previous job change': [previous_job_change],
    'Graduation Marks': [graduation_marks],
    'EXP (Month)': [exp_month],
    'Role_Manager': [role_manager_encoded]
})

# Predict the CTC
if st.button("Predict CTC"):
    prediction = model.predict(input_data)
    st.write(f"Predicted CTC: {prediction[0]:.2f}")

import streamlit as st
import pandas as pd
import joblib

model = joblib.load("KNN_HEART.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

st.title("Heart Stroke Prediction")

st.markdown(
    '<p style="color: white; font-size: 20px; font-weight: 900;">'
    'Provide the following details to check your heart stroke risk:'
    '</p>',
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
        background-color: #1f1f2e;  /* lighter than pure black */
        color: white;
        font-weight: bold;
    }

    .stApp {
        background-color: #1f1f2e;
    }

    div[data-testid="stSidebar"] {
        background-color: #2a2a3d;
        color: white;
    }

    .block-container {
        padding-top: 2rem;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #33ffcc !important;
        font-weight: bold;
    }

    .stButton>button {
        background-color: #33ffcc;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #00e6b8;
        color: black;
    }

    label, .css-1d391kg, .css-10trblm, .css-qrbaxs, .css-1cpxqw2, .css-1n543e5 {
        color: white !important;
        font-weight: bold !important;
    }

    .css-1wa3eu0-option {
        font-weight: bold;
        color: white;
    }

    .css-1wa3eu0-option:hover {
        background-color: #33ffcc;
        color: black;
    }

    .css-qrbaxs input {
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)






age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    # Add missing columns and reorder
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0  

    input_df = input_df[expected_columns]

    # Scale and predict
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

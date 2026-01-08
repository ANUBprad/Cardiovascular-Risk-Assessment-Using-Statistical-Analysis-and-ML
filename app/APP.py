import streamlit as st
import pandas as pd
import joblib

# ---------------------------------
# Load model
# ---------------------------------
model = joblib.load(r"C:\Users\ANUBHAV\OneDrive\Apps\Cardiovascular_Risk_Assessment_Using_Statistical_Analysis_and_ML\models\logistic_regression.pkl")
expected_features = model.feature_names_in_

st.set_page_config(
    page_title="Cardiovascular Risk Assessment",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Cardiovascular Risk Assessment")
st.write("Estimate your **10-year cardiovascular disease risk**")

st.markdown("---")

# ---------------------------------
# USER-FRIENDLY INPUTS
# ---------------------------------
age = st.slider("Age (years)", 30, 80, 50)
gender = st.selectbox("Gender", ["Female", "Male"])
male = 1 if gender == "Male" else 0

smoker = st.selectbox("Do you smoke?", ["No", "Yes"])
cigs_per_week = (
    st.slider("Cigarettes per week", 0, 140, 14)
    if smoker == "Yes" else 0
)

currentSmoker = 1 if smoker == "Yes" else 0
cigsPerDay = cigs_per_week / 7

bp_meds = st.selectbox("On blood pressure medication?", ["No", "Yes"])
BPMeds = 1 if bp_meds == "Yes" else 0

hypertension = st.selectbox("Diagnosed with hypertension?", ["No", "Yes"])
prevalentHyp = 1 if hypertension == "Yes" else 0

diabetes_ui = st.selectbox("Diabetes?", ["No", "Yes"])
diabetes = 1 if diabetes_ui == "Yes" else 0

st.markdown("---")

totChol = st.slider("Total Cholesterol (mg/dL)", 100, 400, 200)
sysBP = st.slider("Systolic BP (mmHg)", 90, 200, 120)
diaBP = st.slider("Diastolic BP (mmHg)", 60, 120, 80)
BMI = st.slider("BMI", 15.0, 45.0, 24.0)
heartRate = st.slider("Heart Rate (bpm)", 50, 120, 75)
glucose = st.slider("Glucose (mg/dL)", 40, 400, 80)

# ---------------------------------
# Build FULL feature row
# ---------------------------------
input_data = pd.DataFrame(0, index=[0], columns=expected_features)

input_data["age"] = age
input_data["male"] = male
input_data["currentSmoker"] = currentSmoker
input_data["cigsPerDay"] = cigsPerDay
input_data["BPMeds"] = BPMeds
input_data["prevalentHyp"] = prevalentHyp
input_data["diabetes"] = diabetes
input_data["totChol"] = totChol
input_data["sysBP"] = sysBP
input_data["diaBP"] = diaBP
input_data["BMI"] = BMI
input_data["heartRate"] = heartRate
input_data["glucose"] = glucose

# Education → default median (removes confusion)
if "education" in input_data.columns:
    input_data["education"] = 2

# Age group encoding
if age <= 40:
    pass
elif age <= 55 and "age_group_Middle" in input_data.columns:
    input_data["age_group_Middle"] = 1
elif age > 55 and "age_group_Senior" in input_data.columns:
    input_data["age_group_Senior"] = 1

# Interaction
if "age_chol_interaction" in input_data.columns:
    input_data["age_chol_interaction"] = age * totChol

# ---------------------------------
# Prediction
# ---------------------------------
if st.button("🔍 Predict Risk"):
    prob = model.predict_proba(input_data)[0][1]

    if prob < 0.3:
        risk, color = "🟢 Low Risk", "green"
    elif prob < 0.6:
        risk, color = "🟡 Medium Risk", "orange"
    else:
        risk, color = "🔴 High Risk", "red"

    st.markdown("---")
    st.subheader("📊 Result")

    st.markdown(
        f"""
        **Risk Category:** <span style="color:{color}; font-size:18px">{risk}</span><br>
        **Estimated Probability:** **{prob:.2%}**
        """,
        unsafe_allow_html=True
    )

    st.info(
        "This is a screening tool. High-risk individuals should consult a healthcare professional."
    )

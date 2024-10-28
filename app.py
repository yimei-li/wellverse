import streamlit as st

# Title and header for the app
st.title("Health Risk & Anti-Aging Prediction")

# Sidebar for parameter input
st.sidebar.header("Environment Factors")
time_of_year = st.sidebar.slider("Time of Year", 1, 12, 6)
prevalence = st.sidebar.slider("Local Disease Prevalence (%)", 0, 100, 20)
transmission_rate = st.sidebar.slider("Transmission Rate", 0.0, 10.0, 2.0)
population_density = st.sidebar.slider("Population Density (per sq km)", 0, 10000, 1000)
income_level = st.sidebar.slider("Income Level", 0, 100000, 50000)

st.sidebar.header("Lifestyle Factors")
diet_quality = st.sidebar.slider("Diet Quality (1-10)", 1, 10, 5)
exercise = st.sidebar.slider("Exercise (hours per week)", 0, 20, 5)
sleep_quality = st.sidebar.slider("Sleep Quality (1-10)", 1, 10, 7)
stress_level = st.sidebar.slider("Stress Level (1-10)", 1, 10, 5)

st.sidebar.header("Health Metrics")
age = st.sidebar.slider("Age", 0, 100, 30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
heart_rate = st.sidebar.slider("Heart Rate (bpm)", 40, 120, 70)
blood_pressure = st.sidebar.slider("Blood Pressure (mm Hg)", 80, 180, 120)
klrd1_expression = st.sidebar.slider("KLRD1 Gene Expression", 0.0, 10.0, 5.0)

st.sidebar.header("Genetics and Immunity")
immune_strength = st.sidebar.slider("Immune System Strength (1-10)", 1, 10, 7)
genetic_predisposition = st.sidebar.slider("Genetic Predisposition to Diseases (1-10)", 1, 10, 5)

# Mockup predictions (replace with model integration)
import random
def predict():
    return {
        "Anti-Aging Score": f"{random.uniform(60, 100):.1f}%",
        "Skin Health Score": f"{random.uniform(50, 100):.1f}%",
        "Sleep Quality Score": f"{random.uniform(50, 100):.1f}%",
        "Cancer Risk": f"{random.uniform(1, 20):.1f}%",
        "Flu Risk (Monthly)": f"{random.uniform(1, 20):.1f}%",
        "COVID-19 Risk (Monthly)": f"{random.uniform(1, 20):.1f}%",
        "Lyme Disease Risk (Monthly)": f"{random.uniform(1, 20):.1f}%"
    }

# Display predictions
st.subheader("Prediction Results")
predictions = predict()

for key, value in predictions.items():
    st.metric(label=key, value=value)

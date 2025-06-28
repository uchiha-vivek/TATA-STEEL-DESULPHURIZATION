import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("final_model.pkl", "rb") as file:
    model = pickle.load(file)


st.set_page_config(
    page_title="TATA Steel - ADS Prediction",
    page_icon="🧪",   
    layout="centered"
)
st.title("TATA STEEL VOCATIONAL PROJECT")
st.subheader('Desulpharization Model overview')

st.markdown("Enter the input parameters to predict final sulfur content:")

# Input fields
hm_wt = st.number_input("Hot Metal Weight (tons)", min_value=30.0, max_value=250.0, value=160.0)
hm_temp = st.number_input("Hot Metal Temperature (°C)", min_value=1100.0, max_value=1700.0, value=1350.0)
hm_s = st.number_input("Initial Sulfur Content (%)", min_value=0.01, max_value=0.1, value=0.03)
act_mg = st.number_input("Actual Magnesium Used (kg)", min_value=5.0, max_value=200.0, value=60.0)
act_lime = st.number_input("Actual Lime Used (kg)", min_value=50.0, max_value=1500.0, value=280.0)

# Prediction trigger
if st.button("🔍 Predict Final Sulfur (ADS)"):
    input_features = np.array([[hm_wt, hm_temp, hm_s, act_mg, act_lime]])
    ads_prediction = model.predict(input_features)[0]

    st.success(f"Predicted ADS: **{ads_prediction:.5f}%**")

    if ads_prediction <= 0.012:
        st.markdown("✅ **Success:** Final sulfur meets the Aim S threshold (≤ 0.012%)")
    else:
        st.markdown("❌ **Warning:** Final sulfur **exceeds** the Aim S threshold (0.012%)")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Created by - <b>Vivek Sharma (NIT Jamshedpur) </b></p>", unsafe_allow_html=True)
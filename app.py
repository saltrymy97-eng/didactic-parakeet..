import streamlit as st
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="AquaFlow AI", layout="wide")

# Main Title
st.title("🌊 Smart Water & Energy Management System")
st.markdown("---")

# --- Sidebar Inputs ---
st.sidebar.header("📊 Live System Inputs")
solar_input = st.sidebar.slider("Solar Production (kWh)", 0, 1000, 500)
water_demand = st.sidebar.slider("Water Demand (m3)", 0, 800, 400)

# --- Logic Layer (The Accountant) ---
DIESEL_FACTOR = 2.68  
CARBON_PRICE = 20     

liters_saved = solar_input / 5
carbon_saved = (liters_saved * DIESEL_FACTOR) / 1000 
green_assets = carbon_saved * CARBON_PRICE

# --- Visual Display ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Daily Diesel Saved", f"{liters_saved:.1f} L")
with col2:
    st.metric("CO2 Reduced", f"{carbon_saved:.4f} Ton")
with col3:
    st.metric("Green Assets Value", f"${green_assets:.2f}")

# --- AI Prediction Simulation ---
st.subheader("🔮 Predictive Consumption Simulation (AI)")
chart_data = pd.DataFrame(
    np.random.randn(24, 2) / [10, 10] + [solar_input/10, water_demand/10],
    columns=['Solar Forecast', 'Demand Forecast']
)
st.line_chart(chart_data)

# --- System Status ---
st.subheader("⚙️ Pump Operational Status")
if solar_input > (water_demand * 0.8):
    st.success("Operating 100% on Solar Energy ✅")
else:
    st.warning("Hybrid Mode Activated (Solar + Grid) 🔋")


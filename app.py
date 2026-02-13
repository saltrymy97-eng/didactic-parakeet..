import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="AquaFlow AI Pro", layout="wide")

# Custom CSS for a professional look
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("🌊 AquaFlow AI: Smart Water Management v2.0")
st.write("Advanced system for water and energy management - Engineering & Accounting Vision")

# --- Sidebar: Technical Parameters ---
st.sidebar.header("⚙️ Technical Parameters")
solar_power = st.sidebar.slider("Solar Power Output (kW)", 0.0, 50.0, 15.0)
pump_efficiency = st.sidebar.select_slider("Pump Efficiency (%)", options=[40, 50, 60, 70, 80, 90], value=70)
head_height = st.sidebar.number_input("Total Head Height (Meters)", value=50)

# --- Logic: Engineering & Accounting ---
# 1. Engineering Calculation: Flow Rate (m3/h) = (Power * Efficiency) / (Gravity * Head)
gravity = 9.81
efficiency_decimal = pump_efficiency / 100
flow_rate = (solar_power * 1000 * efficiency_decimal) / (gravity * head_height) if head_height > 0 else 0

# 2. Accounting Calculation: Carbon Credits
DIESEL_FACTOR = 2.68  # kg CO2 per liter
LITERS_PER_KWH = 0.25 # Diesel saved per kWh
carbon_saved_kg = solar_power * 8 * LITERS_PER_KWH * DIESEL_FACTOR # assuming 8 hours sun
green_asset_value = (carbon_saved_kg / 1000) * 25 # $25 per ton

# --- Dashboard Layout ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Flow Rate", f"{flow_rate:.2f} m³/h", "Real-time")
col2.metric("Daily CO2 Saved", f"{carbon_saved_kg:.1f} kg")
col3.metric("Green Asset Value", f"${green_asset_value:.2f}")
col4.metric("Pump Status", "Active" if solar_power > 2 else "Standby", delta_color="normal")

# --- Advanced Visualization ---
st.markdown("### 📈 System Performance & Predictive Analysis")
tab1, tab2 = st.tabs(["Performance Simulation", "Future Forecast"])

with tab1:
    # Simulating Flow vs Power
    power_range = np.linspace(0, 50, 20)
    flow_range = (power_range * 1000 * efficiency_decimal) / (gravity * head_height)
    df_perf = pd.DataFrame({'Power (kW)': power_range, 'Flow Rate (m3/h)': flow_range})
    st.line_chart(df_perf.set_index('Power (kW)'))

with tab2:
    # AI Predictive Demand
    future_dates = pd.date_range(start='today', periods=24, freq='H')
    forecast_data = pd.DataFrame({
        'Time': future_dates,
        'Predicted Demand': np.random.uniform(5, 15, 24),
        'Solar Availability': np.sin(np.linspace(0, 3.14, 24)) * 20
    })
    st.area_chart(forecast_data.set_index('Time'))

st.info(f"💡 Smart Control: The pump is currently operating at {pump_efficiency}% efficiency to maximize diesel savings.")

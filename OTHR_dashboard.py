import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import os
from OTHR_coverage_model import OTHRParameters, calculate_detection_probability

# Set page config
st.set_page_config(page_title="Arctic OTHR Analysis Dashboard", layout="wide")

st.title("Arctic OTHR Parametric Modeling Dashboard")
st.markdown("**UNCLASSIFIED // PUBLIC RELEASE**")

# Load existing data
@st.cache_data
def load_csv(path):
    return pd.read_csv(path, comment='#')

cost_df = load_csv("OTHR_Cost_Model.csv")
risk_df = load_csv("OTHR_Risk_Register.csv")
schedule_baseline = load_csv("OTHR_Schedule_Model.csv")
schedule_accel = load_csv("OTHR_Schedule_Accelerated.csv")

# Sidebar for common parameters
st.sidebar.header("Global Parameters")
num_sites = st.sidebar.slider("Number of Sites", 1, 5, 3)
arctic_multiplier = st.sidebar.slider("Arctic Multiplier (Site Prep)", 1.0, 5.0, 2.5, 0.1)
use_accel = st.sidebar.toggle("Use Accelerated SchedulePath", value=False)

# Layout: 3 Columns for high-level metrics
m1, m2, m3 = st.columns(3)

# Calculate dynamic cost based on parameters
base_total = cost_df.groupby('Category')['Subtotal ($M)'].sum().sum()
# Simple parametric adjustment logic for dashboard demo
dynamic_cost = 1735.3 + (num_sites - 3) * 550 + (arctic_multiplier - 2.5) * 150
if use_accel: dynamic_cost += 150

m1.metric("Est. Acquisition Cost", f"${dynamic_cost:,.1f}M", f"{(dynamic_cost-1735.3):.1f}M vs Baseline")
foc_months = 84 if use_accel else 121
m2.metric("Program Duration (FOC)", f"{foc_months} Months", f"{foc_months - 121} mo vs Baseline")
critical_risks = len(risk_df[risk_df['Priority'] == 'Critical'])
m3.metric("Critical Risks", critical_risks, "3 New (Accel Path)" if use_accel else None)

# Tabs for detailed analysis
tab1, tab2, tab3, tab4 = st.tabs(["Coverage & Performance", "Cost Model", "Schedule", "Risk Register"])

with tab1:
    st.header("Coverage Visualization")
    if os.path.exists("OTHR_Coverage_Map.png"):
        st.image("OTHR_Coverage_Map.png", caption="Baseline Coverage Map (Static Output)")
    else:
        st.warning("Run OTHR_coverage_model.py to generate latest map.")
    
    st.header("Detection Performance")
    target_type = st.selectbox("Select Target Profile", ["Large Commercial Aircraft", "Generic Cruise Missile"])
    dist = st.slider("Detection Range (km)", 500, 3000, 1500)
    
    params = OTHRParameters()
    pd_clear = calculate_detection_probability(params, target_type, dist, 'clear')
    pd_aurora = calculate_detection_probability(params, target_type, dist, 'auroral')
    
    c1, c2 = st.columns(2)
    c1.write(f"**Pd (Clear):** {pd_clear:.2f}")
    c2.write(f"**Pd (Auroral):** {pd_aurora:.2f}")

with tab2:
    st.header("Detailed Cost Breakdown (Parametric)")
    st.dataframe(cost_df, use_container_width=True)

with tab3:
    st.header("Program Schedule")
    sched_to_show = schedule_accel if use_accel else schedule_baseline
    st.dataframe(sched_to_show, use_container_width=True)

with tab4:
    st.header("Risk Distribution")
    fig, ax = plt.subplots()
    risk_counts = risk_df['Priority'].value_counts()
    ax.pie(risk_counts, labels=risk_counts.index, autopct='%1.1f%%', colors=['red', 'orange', 'yellow', 'green'])
    st.pyplot(fig)
    
    st.header("Critical Mitigations")
    st.table(risk_df[risk_df['Priority'] == 'Critical'][['Risk ID', 'Risk Description', 'Mitigation Strategy']])

st.sidebar.markdown("---")
st.sidebar.info("This dashboard is a prototype. In a production environment, it would dynamically trigger the Python coverage models and write to a database.")

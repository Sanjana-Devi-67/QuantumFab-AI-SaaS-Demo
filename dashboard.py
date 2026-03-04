import streamlit as st
import requests

st.title("QuantumFab AI - Semiconductor Analysis")

st.subheader("Enter Process Parameters")

temperature = st.slider("Temperature", 0.0, 1.0, 0.5)
voltage = st.slider("Voltage", 0.0, 1.0, 0.5)
pressure = st.slider("Pressure", 0.0, 1.0, 0.5)
alignment = st.slider("Alignment", 0.0, 1.0, 0.5)
humidity = st.slider("Humidity", 0.0, 1.0, 0.5)

if st.button("Analyze"):

    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        json={
            "temperature": temperature,
            "voltage": voltage,
            "pressure": pressure,
            "alignment": alignment,
            "humidity": humidity
        }
    )

    result = response.json()

    st.subheader("AI Results")
    st.write("Defect Prediction:", result["Defect_Prediction"])
    st.write("Defect Probability:", round(result["Defect_Probability"], 2))
    st.write("Anomaly Score:", round(result["Anomaly_Score"], 2))

    st.subheader("Quantum Optimization")
    st.write("Optimal Configuration:", result["Quantum_Optimization"]["solution"])
    st.write("Minimum Cost:", result["Quantum_Optimization"]["minimum_cost"])

# ---------------------------------------------------
# Project Overview Section
# ---------------------------------------------------

st.markdown("---")
st.header("Project Overview")

st.write("""
This prototype demonstrates a hybrid AI and Quantum computing approach for semiconductor manufacturing analysis.

The system takes basic process parameters such as temperature, voltage, pressure, alignment, and humidity. 
These parameters represent manufacturing conditions that can influence whether a semiconductor chip becomes defective.

The AI layer analyzes these inputs to estimate the probability of defects and detect unusual manufacturing patterns.
For defect prediction we use **XGBoost**, which is well suited for tabular industrial data and can capture complex relationships between process variables.

An **Isolation Forest model** is used for anomaly detection. This helps identify unusual parameter combinations that may indicate potential process issues or machine drift.

To demonstrate the role of quantum computing, we include a **QAOA-based optimization step using Qiskit**. 
This simulates how quantum algorithms could help solve constrained optimization problems in semiconductor manufacturing, 
such as selecting the most efficient configuration under cost or resource constraints.

Together, this prototype shows how AI can be used for predictive analysis while quantum computing can assist with optimization, 
forming the basis of a scalable Semiconductor SaaS platform.
""")
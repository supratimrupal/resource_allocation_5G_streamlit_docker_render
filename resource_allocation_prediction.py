import streamlit as st
import numpy as np
import pickle

# Load the trained model, label encoder, and scaler
loaded_model = pickle.load(open('saved_model_misc/resource_allocation_optimization_5G.sav', 'rb'))
label_encoder = pickle.load(open('saved_model_misc/App_type_label_encoder.pkl', 'rb'))
scaler = pickle.load(open('saved_model_misc/RA_5G_scaler.pkl', 'rb'))

# Streamlit UI
st.title("5G Resource Allocation Prediction")

# User Input Fields (without Resource_Allocation)
application_type = st.selectbox("Select Application Type", ['Video_Call', 'Voice_Call', 'Streaming', 'Emergency_Service','Online_Gaming', 'Background_Download', 'Web_Browsing','IoT_Temperature', 'Video_Streaming', 'File_Download', 'VoIP_Call'])
signal_strength = st.number_input("Enter Signal Strength (dBm)", value=-80)
latency_in_ms = st.number_input("Enter Latency (ms)", min_value=0, value=30)
required_bandwidth = st.number_input("Enter Required Bandwidth (Kbps)", min_value=0.001, value=1024.0)
allocated_bandwidth = st.number_input("Enter Allocated Bandwidth (Kbps)", min_value=0.001, value=1024.0)


bandwidth_utilization = allocated_bandwidth / required_bandwidth 


application_type_encoded = label_encoder.transform([application_type])[0]


input_data_processed = np.array([[application_type_encoded, signal_strength, latency_in_ms, bandwidth_utilization]])


input_data_scaled = scaler.transform(input_data_processed)


if st.button("Predict Resource Allocation"):
    prediction = loaded_model.predict(input_data_scaled)
    st.success(f"Predicted Resource Allocation: {prediction[0]:.2f}%")

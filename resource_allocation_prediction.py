import streamlit as st
import numpy as np
import pickle


loaded_model = pickle.load(open('saved_model_misc/resource_allocation_optimization_5G.sav','rb'))
label_encoder =  pickle.load(open('saved_model_misc/App_type_label_encoder.pkl','rb'))
scaler =  pickle.load(open('saved_model_misc/RA_5G_scaler.pkl','rb'))


st.title("5G Resource Allocation Prediction")


application_type = st.selectbox("Select Application Type", ['Video_Call', 'Voice_Call', 'Streaming', 'Emergency_Service','Online_Gaming', 'Background_Download', 'Web_Browsing','IoT_Temperature', 'Video_Streaming', 'File_Download', 'VoIP_Call'])
signal_strength = st.number_input ("Enter Signal Strength (dBm)" , value=-80)
latency = st.number_input ("Enter Latency (ms)" , min_value=0, value=30)
required_bandwidth = st.number_input("Enter Required Bandwidth (Kbps)" ,min_value=0.001, value=1024.0)
allocated_bandwidth = st.number_input("Enter Allocated Bandwidth (Kbps)", min_value=0.001 , value=1024.0)


bandwidth_utilization = allocated_bandwidth / required_bandwidth 


application_type = label_encoder.transform([application_type])[0]


input_5G_data = np.array([[application_type, signal_strength, latency ,bandwidth_utilization]])


input_5G_data_scaled = scaler.transform(input_5G_data)


if st.button("Predict Resource Allocation"):
    prediction = loaded_model.predict(input_5G_data_scaled)
    st.success("Predicted Resource Allocation: " + str(round(prediction[0], 2)) + "%")

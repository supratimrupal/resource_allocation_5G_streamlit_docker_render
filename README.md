5G Resource Allocation Prediction

Random Forest Regressor

site link: (https://resource-allocation-5g-streamlit-docker.onrender.com/)
**************************************************

Multiple_Disease_Prediction_web_app
Anaconda Environments --> MachineLearning --> Open Terminal

for local run:
streamlit run resource_allocation_prediction.py

***********************************

pip install -r requirements.txt

Dockerfile:

FROM python:3.9
COPY . resource_allocation_optimization_5G_webapp/
WORKDIR resource_allocation_optimization_5G_webapp/
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD streamlit run resource_allocation_prediction.py

*********************************************************

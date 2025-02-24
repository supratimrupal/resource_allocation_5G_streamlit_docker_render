'Multiple Disease Prediction System' 

['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction']

Classifications Model Used : 
Diabetes Prediction - SVM 
Heart Disease Prediction - Logistic Regression
Parkinsons Prediction - SVM

site link: https://docker-multiple-disease-pred-model.onrender.com
**************************************************

Multiple_Disease_Prediction_web_app
Anaconda Environments --> MachineLearning --> Open Terminal

for local run:
streamlit run multiple_disease_prediction_web_app.py

***********************************

pip install -r requirements.txt

Dockerfile:

FROM python:3.9
COPY . multiple_disease_prediction_web_app/
WORKDIR multiple_disease_prediction_web_app/
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD streamlit run multiple_disease_prediction_web_app.py

*********************************************************

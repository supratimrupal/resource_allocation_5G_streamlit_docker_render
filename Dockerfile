FROM python:3.9
COPY . resource_allocation_optimization_5G_webapp/
WORKDIR resource_allocation_optimization_5G_webapp/
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD streamlit run resource_allocation_prediction.py

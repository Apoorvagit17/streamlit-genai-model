import streamlit as st
import requests

# Set up the title and description
st.title('Plant Disease Detection and Prevention')
st.write('This app detects plant diseases and provides preventive measures.')

# Function to make a request to your ML model API
def get_preventive_measures(disease_name):
    # Assuming your model API is hosted at this endpoint
    url = 'http://192.168.1.9:8083/predict'  # Replace with your actual endpoint
    response = requests.post(url, json={'disease': disease_name})
    
    if response.status_code == 200:
        data = response.json()
        return data.get('preventive_measures', 'No preventive measures found.')
    else:
        return 'Error in fetching data from the model API.'

# User input for the disease name
disease_name = st.text_input('Enter the plant disease name:')

if st.button('Get Preventive Measures'):
    if disease_name:
        # Fetch preventive measures
        preventive_measures = get_preventive_measures(disease_name)
        st.subheader('Preventive Measures:')
        st.write(preventive_measures)
    else:
        st.write('Please enter a disease name.')

import streamlit as st
import requests

# Streamlit App Configuration
st.set_page_config(page_title="Crop Disease Prevention", page_icon="🌾", layout="centered")

# Title
st.title("Crop Disease Prevention Assistant")

# Input: Crop Disease Name
disease_name = st.text_input("Enter the crop disease name:", "")

# Define a function to call the LLaMA API
def get_preventive_measures(disease_name):
    # Replace with your actual LLaMA API endpoint and API key
    api_url = "https://api.llama-api/chat/completions.com"  # Replace with your actual LLaMA API endpoint
    api_key = "llx-pJJGjdBTutJBLgR3tqIFBIQohVZr2nlSAZ2iSga3hFV62IQX"  # Replace with your actual API key

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"  # Common way to include an API key
    }

    payload = {
        "prompt": f"What are some preventive measures or first aid that a farmer can do for {disease_name}?",
        "max_tokens": 100  # Adjust max_tokens based on how much text you want
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data.get("text", "No preventive measures found.")
    except requests.RequestException as e:
        st.error(f"Error: {e}")
        return "Could not fetch data from the API. Please try again later."

# Submit button
if st.button("Get Preventive Measures"):
    if disease_name:
        st.write(f"Fetching preventive measures for *{disease_name}*...")
        preventive_measures = get_preventive_measures(disease_name)
        st.write("### Preventive Measures:")
        st.write(preventive_measures)
    else:
        st.warning("Please enter a crop disease name.")

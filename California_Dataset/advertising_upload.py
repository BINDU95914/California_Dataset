import streamlit as st
import pickle as pk
import numpy as np

# Streamlit App
st.title("Advertising Prediction")

# Input fields for features
Tv = st.number_input("Enter TV advertising budget:", min_value=0.0, format="%.2f")
Radio = st.number_input("Enter Radio advertising budget:", min_value=0.0, format="%.2f")
Newspaper = st.number_input("Enter Newspaper advertising budget:", min_value=0.0, format="%.2f")

# File uploader for model
uploaded_file = st.file_uploader("Upload the trained model file (Pickle format):", type=['pkl'])

# Load model and make prediction when the button is clicked
if st.button('Predict'):
    if uploaded_file is not None:
        try:
            # Load the uploaded model
            model = pk.load(uploaded_file)
            
            # Prepare input for prediction
            input_data = np.array([[Tv, Radio, Newspaper]])
            
            # Make prediction
            ans = model.predict(input_data)
            
            # Display the result
            st.success(f"Predicted sales: {ans[0]:.2f}")
        except Exception as e:
            st.error(f"Error loading model or making prediction: {str(e)}")
    else:
        st.error("Please upload a model file before predicting.")

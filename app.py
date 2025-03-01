import streamlit as st
import pandas as pd
import pickle
import numpy as np


# Load the dataset
df = pd.read_csv(r'./datasets/legit_sample (1).csv')
processed_data = pd.read_csv(r'./datasets/legit_sample_vectors.csv')

# # Load the trained XGBoost model
# with open('./saved_models/XGboost_wildfire_pred_model (1).sav', 'rb') as file:
model = pickle.load(r'./saved_models/XGboost_wildfire_pred_model (1).sav')

# Streamlit app title
st.title('LA wildfire Prediction App')

# Display the dataset
st.subheader('Test Dataset')
st.dataframe(df)  # Display the dataset in a table

# Allow users to select a row
st.subheader('Select a Row for Prediction')
row_index = st.number_input('Enter the row index (0 to {})'.format(len(df) - 1), min_value=0, max_value=len(df) - 1, value=0)

# Get the selected row's features
selected_row = df.iloc[row_index]
st.write('Selected Row Features:')
st.write(selected_row)

# Make a prediction
if st.button(' Predict '):
    
    input_data = processed_data.iloc[row_index]
    input_data = np.array(input_data)
    prediction = model.predict([input_data])
    
    # Display the prediction
    st.success(f'Predicted Chance of wildfire: {prediction[0] *100:.2f}%')







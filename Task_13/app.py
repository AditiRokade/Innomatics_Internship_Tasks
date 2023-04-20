import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the laptop dataset
laptop_data = pd.read_csv('E:\Innomatics_internship\Tasks\Task_13\laptop_details.csv')

# Clean and preprocess the data
# (omitted for brevity)

# Select relevant features for modeling
features = ['RAM', 'HDD', 'Processor', 'OS', 'Price']

# Build a simple linear regression model
model = LinearRegression()
model.fit(laptop_data[features[:-1]], laptop_data[features[-1]])

# Build the Streamlit app
st.title("Tesla Laptop Price Estimator")
st.sidebar.title("Features")

# Add input widgets for each feature
ram_size = st.sidebar.number_input("RAM Size (GB)", min_value=2, max_value=64, value=8)
hdd_size = st.sidebar.number_input("HDD Size (GB)", min_value=128, max_value=8192, value=512)
processor = st.sidebar.selectbox("Processor", options=laptop_data['Processor'].unique())
os_type = st.sidebar.selectbox("Operating System", options=laptop_data['OS'].unique())

# Predict the price based on the selected features
input_features = pd.DataFrame([[ram_size, hdd_size, processor, os_type]], columns=features[:-1])
price = model.predict(input_features)[0]

# Display the predicted price
st.subheader(f"Predicted Laptop Price: Rs. {price:,.0f}")

# Provide recommendations on pricing strategy
st.subheader("Pricing Strategy Recommendations")
st.write("Based on the analysis of the laptop market data, here are some recommendations for Tesla Laptop:")

# (add pricing recommendations based on the analysis of the dataset)

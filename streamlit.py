import streamlit as st
import pickle
import numpy as np

# Define the app layout
st.title("Iris Species Prediction")
st.write("Enter the following features to predict the Iris species:")

# Add input widgets for the user to enter feature values
sepal_length = st.number_input("Enter the Sepal Length:")
sepal_width = st.number_input("Enter the Sepal Width:")
petal_length = st.number_input("Enter the Petal Length:")
petal_width = st.number_input("Enter the Petal Width:")
def predict_species():
    # Create a numpy array from the input values
    new_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Use the trained classifier to make a prediction
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    predicted_class = model.predict(new_data)[0]

    st.write("Prediction", f"The predicted species is {predicted_class}")

if st.button("Predict Species"):
    predict_species()
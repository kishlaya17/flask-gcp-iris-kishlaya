import streamlit as st
import requests

st.set_page_config(page_title="Iris ML Predictor", page_icon="🌸")

st.title("🌸 Iris Flower Classification App")
st.write("Predict Iris species using a Logistic Regression model deployed via Flask API.")

st.sidebar.header("Input Features")

sepal_length = st.sidebar.slider("Sepal Length", 4.0, 8.0, 5.1)
sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.5, 3.5)
petal_length = st.sidebar.slider("Petal Length", 1.0, 7.0, 1.4)
petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 0.2)

if st.button("Predict"):
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    response = requests.post("http://127.0.0.1:5050/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['prediction']}")
        st.info(f"Confidence: {result['confidence']}")
    else:
        st.error("Error connecting to API.")

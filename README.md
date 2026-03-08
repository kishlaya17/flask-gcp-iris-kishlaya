# 🚀 Flask + Google Cloud Run – Iris ML Deployment (Custom Implementation)

This project demonstrates a complete end-to-end MLOps workflow where a machine learning model is trained, containerized, built in Google Cloud, deployed to Cloud Run, and integrated with a Streamlit frontend.

This implementation is customized and not identical to the base lab template.

---

## 📌 Project Overview

The application exposes a REST API that predicts Iris flower species using a trained Logistic Regression model.

The API is deployed on **Google Cloud Run** and publicly accessible over HTTPS.  
A **Streamlit frontend** connects to the deployed API for interactive predictions.

---

## 🧠 Model Details

- Algorithm: Logistic Regression  
- Dataset: Iris Dataset  
- Accuracy Achieved: ~96–97%  
- Model Serialization: `pickle`  

The model is trained locally and saved as:
model/model.pkl

---

## 🏗 Project Structure

flask-gcp-iris-kishlaya/
│
├── app/
│ ├── main.py # Flask API entry point
│ ├── predict.py # Prediction logic
│ └── train.py # Model training script
│
├── model/
│ └── model.pkl # Trained model
│
├── streamlit_app.py # Frontend UI
├── requirements.txt # Dependencies
├── Dockerfile # Container configuration
└── README.md

---

## ⚙️ How the Pipeline Works

### 1️⃣ Train Model Locally
python3 app/train.py

This generates and saves the trained model.

---

### 2️⃣ Test API Locally
python -m app.main

Test with:
python test_api.py

---

### 3️⃣ Docker Containerization

Build image:
docker build -t iris-ml-app .

Run locally:
docker run -p 5050:5050 iris-ml-app

---

### 4️⃣ Build Image in Google Cloud
gcloud builds submit --tag gcr.io/<PROJECT_ID>/iris-app

This builds and pushes the container to Google Container Registry.

---

### 5️⃣ Deploy to Cloud Run
gcloud run deploy iris-app
--image gcr.io/<PROJECT_ID>/iris-app
--platform managed
--region us-central1
--allow-unauthenticated
--port 5050

---

## 🌍 Live Deployment URL
https://iris-app-144529166192.us-central1.run.app

---

## 🎨 Streamlit Frontend

The frontend connects directly to the deployed Cloud Run API.

Run locally:
streamlit run streamlit_app.py
---

## 🔐 Cloud Services Used

- Google Cloud Build  
- Google Artifact Registry  
- Google Cloud Run  
- Cloud Storage  
- Compute Engine API  

Billing was configured to allow container deployment under free-tier limits.

---

## 🧩 Custom Enhancements Added

Compared to the base lab:

- Custom project structure (separated app/ directory)
- Modified serving port (5050)
- IAM permission configuration for Cloud Build
- Production deployment on Cloud Run
- Streamlit integration with live endpoint
- Clean and optimized Dockerfile

---

## 📦 Technologies Used

- Python  
- Flask  
- Scikit-learn  
- Docker  
- Google Cloud Platform  
- Streamlit  

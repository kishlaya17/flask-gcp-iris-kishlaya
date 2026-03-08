```markdown
# 🚀 Flask + GCP Iris ML Deployment (Custom Implementation)

This project demonstrates an end-to-end MLOps pipeline where a machine learning model is:

- Trained locally
- Containerized using Docker
- Built using Google Cloud Build
- Deployed to Google Cloud Run
- Integrated with a Streamlit frontend

This implementation is customized and not identical to the base lab template.

---

# 📌 Project Overview

This application exposes a REST API that predicts Iris flower species using a trained Logistic Regression model.

The deployed API is publicly accessible via Google Cloud Run and connected to a Streamlit frontend.

---

# 🧠 Model Details

- Algorithm: Logistic Regression
- Dataset: Iris Dataset (custom training script used)
- Evaluation Metric: Accuracy
- Achieved Accuracy: ~96–97%
- Model serialized using: `pickle`

---

# 🏗 Project Structure

```

flask-gcp-iris-kishlaya/
│
├── app/
│   ├── main.py          # Flask API
│   ├── predict.py       # Prediction logic
│   └── train.py         # Model training script
│
├── model/
│   └── model.pkl        # Trained model
│
├── streamlit_app.py     # Frontend UI
├── requirements.txt     # Dependencies
├── Dockerfile           # Container config
└── README.md

```

---

# ⚙️ How It Works

### 1️⃣ Model Training
The model is trained locally using:

```

python3 app/train.py

```

The trained model is saved as:

```

model/model.pkl

```

---

### 2️⃣ Local API Testing

Run Flask API locally:

```

python -m app.main

```

Test using:

```

python test_api.py

```

---

### 3️⃣ Docker Containerization

Build Docker image locally:

```

docker build -t iris-ml-app .

```

Run container:

```

docker run -p 5050:5050 iris-ml-app

```

---

### 4️⃣ Cloud Build (Container Build in GCP)

```

gcloud builds submit --tag gcr.io/<PROJECT_ID>/iris-app

```

This uploads the source and builds the container image in Google Cloud.

---

### 5️⃣ Cloud Run Deployment

```

gcloud run deploy iris-app 
--image gcr.io/<PROJECT_ID>/iris-app 
--platform managed 
--region us-central1 
--allow-unauthenticated 
--port 5050

```

---

# 🌍 Live Deployment URL

```

[https://iris-app-144529166192.us-central1.run.app](https://iris-app-144529166192.us-central1.run.app)

```

Example API request:

```

POST /predict

````

Sample JSON body:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
````

Response:

```json
{
  "prediction": "setosa",
  "confidence": 0.97
}
```

---

# 🎨 Streamlit Frontend

The Streamlit UI connects directly to the deployed Cloud Run backend.

Run locally:

```
streamlit run streamlit_app.py
```

---

# 🔐 Cloud Configuration

The following services were enabled:

* Cloud Build
* Artifact Registry
* Cloud Run
* Cloud Storage
* Compute Engine API

Billing was configured to allow container deployment.

---

# 🧩 Custom Enhancements Added

Compared to the base lab template:

* Custom project naming structure
* Modified deployment port configuration (5050)
* Structured project directory (app/ separation)
* Explicit IAM permission configuration
* Streamlit integration with live Cloud Run endpoint
* Clean Dockerfile optimized for production

---

# 📦 Technologies Used

* Python
* Flask
* Scikit-learn
* Docker
* Google Cloud Build
* Google Cloud Run
* Streamlit

```

import joblib
import numpy as np

# Load trained model
model = joblib.load("model/model.pkl")

# Iris target names
class_names = ["setosa", "versicolor", "virginica"]


def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)

    confidence = float(np.max(probabilities))
    predicted_label = class_names[prediction]

    return predicted_label, confidence

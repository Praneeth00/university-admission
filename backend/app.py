from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)

# Allow requests from your GitHub Pages domain
CORS(app, origins=["https://praneeth00.github.io"])

# Load trained model and scaler
model = joblib.load("models/admission_model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([[data["gre"], data["toefl"], data["university"],
                          data["sop"], data["lor"], data["cgpa"], data["research"]]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    
    return jsonify({"admission_chance": round(float(prediction[0]) * 100, 2)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

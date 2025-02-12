import joblib
import numpy as np

# Load trained model and scaler
model = joblib.load("models/admission_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Example user input
user_input = np.array([[320, 110, 4, 4.5, 4.5, 9.0, 1]])

# Scale input
user_input_scaled = scaler.transform(user_input)

# Make prediction
prediction = model.predict(user_input_scaled)

print(f"Predicted Admission Chance: {prediction[0] * 100:.2f}%")

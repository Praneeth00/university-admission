import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv("data/admission_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Define features and target variable
features = ["GRE Score", "TOEFL Score", "University Rating", "SOP", "LOR", "CGPA", "Research"]
target = "Chance of Admit"

X = df[features]
y = df[target]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model and scaler
joblib.dump(model, "models/admission_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("✅ Model training complete and saved.")

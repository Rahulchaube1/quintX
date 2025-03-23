import joblib
import pandas as pd

# Load model
model = joblib.load("models/k8s_model.pkl")

# Sample new data
new_data = pd.DataFrame([[0.5, 0.7, 0.2]], columns=["CPU", "Memory", "Disk"])

# Predict
prediction = model.predict(new_data)
print("🔮 Prediction:", prediction)

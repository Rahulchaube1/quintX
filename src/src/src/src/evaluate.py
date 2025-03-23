import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data/k8s_metrics.csv")

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Load model
model = joblib.load("models/k8s_model.pkl")

# Evaluate
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)

print(f"📊 Model Accuracy: {accuracy * 100:.2f}%")

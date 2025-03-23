import joblib
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load dataset
df = pd.read_csv("data/k8s_metrics.csv")

# Assuming some preprocessing here
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save model
joblib.dump(model, "models/k8s_model.pkl")
print("✅ Model trained and saved!")

import os
import subprocess

# Ensure 'data' directory exists
os.makedirs("data", exist_ok=True)

def collect_k8s_logs():
    try:
        logs = subprocess.run(["kubectl", "logs", "--all-namespaces"], capture_output=True, text=True)
        with open("data/k8s_logs.txt", "w") as f:
            f.write(logs.stdout)
        print("✅ Logs collected successfully!")
    except Exception as e:
        print(f"❌ Error collecting logs: {e}")

def collect_k8s_metrics():
    try:
        metrics = subprocess.run(["kubectl", "top", "pods", "--all-namespaces"], capture_output=True, text=True)
        with open("data/k8s_metrics.csv", "w") as f:
            f.write(metrics.stdout)
        print("✅ Metrics collected successfully!")
    except Exception as e:
        print(f"❌ Error collecting metrics: {e}")

collect_k8s_logs()
collect_k8s_metrics()

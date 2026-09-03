"""
AI / ML Landslide Susceptibility & Trigger Model
Owned by: Member 3
Dataset: Synthetic / Kaggle Historical Landslide Data
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

def generate_synthetic_data(samples=1000):
    """
    Simulates geological and weather parameters:
    - rainfall_mm: 0 to 300 mm
    - slope_deg: 0 to 60 degrees
    - soil_moisture_pct: 10% to 100%
    - elevation_m: 200m to 4000m
    """
    np.random.seed(42)
    rainfall = np.random.uniform(10, 300, samples)
    slope = np.random.uniform(5, 60, samples)
    soil_moisture = np.random.uniform(20, 100, samples)
    elevation = np.random.uniform(300, 3500, samples)

    # Ground truth formula: high rainfall + steep slope + high moisture = landslide
    risk_score = (rainfall * 0.4) + (slope * 0.4) + (soil_moisture * 0.2)
    labels = (risk_score > 65).astype(int)  # 1 = Landslide, 0 = Stable

    X = np.column_stack((rainfall, slope, soil_moisture, elevation))
    return X, labels

def train_and_save():
    print("🧠 [Member 3] Training Landslide Prediction Model...")
    X, y = generate_synthetic_data(2000)

    clf = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)
    clf.fit(X, y)

    # Save model for Member 2's backend
    model_filename = "landslide_model.pkl"
    with open(model_filename, "wb") as f:
        pickle.dump(clf, f)

    print(f"✅ Model trained and saved as '{model_filename}'! Ready for Member 2 to integrate.")

if __name__ == "__main__":
    train_and_save()

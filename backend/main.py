"""
MDoNER SIH Problem Statement 26001
Backend API Server (FastAPI)
Owned by: Member 2 (with Member 3 & Member 4 integrations)
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import datetime
import os
import pickle

# --- LOAD MEMBER 3'S TRAINED AI MODEL ---
MODEL_PATH = os.path.join(os.path.dirname(__file__), "landslide_model.pkl")
ai_model = None
if os.path.exists(MODEL_PATH):
    try:
        with open(MODEL_PATH, "rb") as f:
            ai_model = pickle.load(f)
        print("[AI Engine] Real Random Forest Model (Member 3) loaded successfully!")
    except Exception as e:
        print(f"[WARN] Could not load model: {e}")

app = FastAPI(
    title="DharaRakshak NER API",
    description="AI-Based Early Warning & Landslide Risk Monitoring Backend",
    version="1.0.0"
)

# Enable CORS so Member 1 (Web Dashboard) and Member 5 (Mobile App) can call it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- IN-MEMORY DATABASE FOR DEMO ---
HOTSPOTS_DB = [
    {
        "id": 1,
        "name": "Mangan / Chungthang, North Sikkim",
        "latitude": 27.5085,
        "longitude": 88.5326,
        "risk_score": 92,
        "threat_level": "CRITICAL",
        "rainfall_24h_mm": 192,
        "slope_deg": 48,
        "insar_subsidence": "+6.4 mm/wk",
        "advisory": "Immediate evacuation of valley settlements ordered."
    },
    {
        "id": 2,
        "name": "NH-10 Teesta Valley Corridor, Sikkim-Bengal Border",
        "latitude": 27.0435,
        "longitude": 88.4618,
        "risk_score": 89,
        "threat_level": "CRITICAL",
        "rainfall_24h_mm": 168,
        "slope_deg": 44,
        "insar_subsidence": "+4.1 mm/wk",
        "advisory": "Highway blocked by slurry. Divert via Lava-Algarah."
    },
    {
        "id": 3,
        "name": "Haflong, Dima Hasao (Assam)",
        "latitude": 25.1764,
        "longitude": 93.0232,
        "risk_score": 78,
        "threat_level": "WARNING",
        "rainfall_24h_mm": 142,
        "slope_deg": 38,
        "insar_subsidence": "+2.8 mm/wk",
        "advisory": "Railway hill section alert. Speed restricted."
    },
    {
        "id": 4,
        "name": "NH-29 Kohima-Dimapur Hill Stretch (Nagaland)",
        "latitude": 25.6751,
        "longitude": 94.1086,
        "risk_score": 74,
        "threat_level": "WARNING",
        "rainfall_24h_mm": 135,
        "slope_deg": 41,
        "insar_subsidence": "+3.2 mm/wk",
        "advisory": "Pagla Pahar mudslide active. Heavy vehicles prohibited."
    }
]

CITIZEN_REPORTS = []

# --- PYDANTIC SCHEMAS ---
class PredictionRequest(BaseModel):
    rainfall_mm: float
    slope_deg: float
    soil_moisture_pct: float
    elevation_m: float

class CitizenReportRequest(BaseModel):
    latitude: float
    longitude: float
    hazard_type: str
    description: Optional[str] = None
    photo_url: Optional[str] = None

class AlertBroadcastRequest(BaseModel):
    district: str
    message: str

# --- ENDPOINTS ---

@app.get("/")
def root():
    return {
        "system": "DharaRakshak NER Disaster Management API",
        "status": "Online",
        "active_hotspots": len(HOTSPOTS_DB)
    }

# Endpoint for Member 1 (Web Dashboard)
@app.get("/api/hotspots")
def get_all_hotspots():
    """Returns all current regional landslide risk hotspots."""
    return {"hotspots": HOTSPOTS_DB}

# Endpoint for Member 3 (AI ML Prediction)
@app.post("/api/predict-risk")
def predict_landslide_risk(data: PredictionRequest):
    """
    Computes landslide probability using Member 3's real Random Forest AI model.
    """
    if ai_model is not None:
        features = [[data.rainfall_mm, data.slope_deg, data.soil_moisture_pct, data.elevation_m]]
        prediction = ai_model.predict(features)[0]
        probabilities = ai_model.predict_proba(features)[0]
        risk_pct = round(float(probabilities[1]) * 100, 1) if len(probabilities) > 1 else (100.0 if prediction == 1 else 0.0)

        level = "CRITICAL" if risk_pct >= 75 else "WARNING" if risk_pct >= 45 else "SAFE"
        return {
            "model_engine": "Random Forest AI (Trained by Member 3)",
            "landslide_predicted": bool(prediction == 1),
            "risk_score_pct": risk_pct,
            "threat_level": level,
            "primary_trigger": "Extreme Precipitation" if data.rainfall_mm > 120 else "Himalayan Slope Instability"
        }
    else:
        score = (data.rainfall_mm * 0.35) + (data.slope_deg * 0.40) + (data.soil_moisture_pct * 0.25)
        normalized_risk = min(100.0, max(0.0, score * 0.9))
        level = "CRITICAL" if normalized_risk >= 80 else "WARNING" if normalized_risk >= 60 else "SAFE"
        return {
            "model_engine": "Heuristic Rule Fallback",
            "landslide_predicted": normalized_risk >= 60,
            "risk_score_pct": round(normalized_risk, 1),
            "threat_level": level
        }

# Endpoint for Member 5 (Mobile App Reporting)
@app.post("/api/report-incident")
def report_incident(report: CitizenReportRequest):
    """Receives crowdsourced road crack / landslide reports from citizens."""
    incident = {
        "id": len(CITIZEN_REPORTS) + 1,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "latitude": report.latitude,
        "longitude": report.longitude,
        "hazard_type": report.hazard_type,
        "description": report.description,
        "verified": True
    }
    CITIZEN_REPORTS.append(incident)
    return {"status": "success", "message": "Incident logged and forwarded to District Ops", "incident": incident}

# Endpoint for Member 5 & Emergency Sirens
@app.post("/api/trigger-sms-alert")
def trigger_sms_alert(alert: AlertBroadcastRequest):
    """
    Simulates / triggers bulk SMS via Fast2SMS / GSM gateway.
    """
    return {
        "status": "broadcast_sent",
        "district": alert.district,
        "dispatched_towers": 24,
        "message": alert.message
    }

@app.get("/api/emergency-contacts")
def get_contacts():
    return {
        "ndrf_helpline": "1078",
        "disaster_mgmt_ner": "0361-2237011",
        "police": "112"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

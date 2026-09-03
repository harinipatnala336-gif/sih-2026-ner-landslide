"""
Member 5: Mobile App Connection Test Script
Simulates sending a citizen hazard report and receiving an emergency SMS.
"""

import requests
import json

BACKEND_URL = "http://localhost:8000"

def test_submit_report():
    print("📱 [Member 5] Simulating Citizen Incident Report from mountain highway...")
    payload = {
        "latitude": 27.0435,
        "longitude": 88.4618,
        "hazard_type": "Fresh Road Crack / Subsidence",
        "description": "5cm crack across NH-10 near Teesta Bridge, debris rolling down slope."
    }
    
    try:
        res = requests.post(f"{BACKEND_URL}/api/report-incident", json=payload)
        print("✅ Incident successfully posted to Backend:", res.json())
    except requests.exceptions.ConnectionError:
        print("⚠️ Backend is not running yet. Start Member 2's backend with: python backend/main.py")

def test_sms_broadcast():
    print("\n📲 [Member 5] Simulating 2G Emergency SMS Dispatch...")
    payload = {
        "district": "North Sikkim",
        "message": "⚠️ CRITICAL MDoNER ALERT: Landslide risk imminent on NH-10. Seek shelter or divert via Lava. NDRF: 1078."
    }
    try:
        res = requests.post(f"{BACKEND_URL}/api/trigger-sms-alert", json=payload)
        print("✅ Emergency SMS dispatched to cell towers:", res.json())
    except requests.exceptions.ConnectionError:
        print("⚠️ Backend is not running yet.")

if __name__ == "__main__":
    test_submit_report()
    test_sms_broadcast()

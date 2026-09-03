"""
MDoNER SIH Problem Statement 26001
Live Meteorological Data Ingestion Service
Owned by: Member 4
Data Source: Open-Meteo Open Weather API (Free, No API Key Required)
"""

import requests
import json

# Coordinates for Key North-Eastern Region (NER) Cities & Landslide Hotspots
NER_COORDINATES = {
    "Gangtok (Sikkim)": {"lat": 27.3389, "lon": 88.6065},
    "Mangan (North Sikkim)": {"lat": 27.5085, "lon": 88.5326},
    "Guwahati (Assam)": {"lat": 26.1445, "lon": 91.7362},
    "Haflong (Dima Hasao, Assam)": {"lat": 25.1764, "lon": 93.0232},
    "Shillong (Meghalaya)": {"lat": 25.5788, "lon": 91.8933},
    "Kohima (Nagaland)": {"lat": 25.6751, "lon": 94.1086},
    "Aizawl (Mizoram)": {"lat": 23.7271, "lon": 92.7176},
    "Itanagar (Arunachal Pradesh)": {"lat": 27.0844, "lon": 93.6053}
}

def fetch_live_weather(location_name: str):
    """
    Fetches real-time precipitation and weather parameters for a given NER location.
    """
    if location_name not in NER_COORDINATES:
        return {"error": f"Location '{location_name}' not in NER monitoring registry."}
    
    coords = NER_COORDINATES[location_name]
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={coords['lat']}&longitude={coords['lon']}&"
        f"current=temperature_2m,relative_humidity_2m,precipitation,rain,weather_code,wind_speed_10m&"
        f"daily=precipitation_sum&timezone=Asia%2FKolkata"
    )

    try:
        response = requests.get(url, timeout=6)
        response.raise_for_status()
        data = response.json()

        current = data.get("current", {})
        daily = data.get("daily", {})
        
        # Today's cumulative rainfall in mm
        today_rain_mm = daily.get("precipitation_sum", [0.0])[0] if "precipitation_sum" in daily else 0.0

        return {
            "location": location_name,
            "latitude": coords["lat"],
            "longitude": coords["lon"],
            "current_rain_rate_mm_hr": current.get("rain", 0.0),
            "today_cumulative_rain_mm": today_rain_mm,
            "relative_humidity_pct": current.get("relative_humidity_2m", 0),
            "temperature_c": current.get("temperature_2m", 0),
            "timestamp": current.get("time", "")
        }
    except Exception as e:
        return {"error": f"Failed to fetch live weather: {str(e)}"}

def test_all_ner_stations():
    print("[Member 4] Fetching Live Satellite Weather for North-East India...\n")
    print(f"{'Location':<30} | {'Today Rain (mm)':<16} | {'Humidity':<10} | {'Temp (C)'}")
    print("-" * 75)
    
    for loc in NER_COORDINATES.keys():
        res = fetch_live_weather(loc)
        if "error" not in res:
            print(f"{res['location']:<30} | {res['today_cumulative_rain_mm']:<16} | {str(res['relative_humidity_pct']) + '%':<10} | {res['temperature_c']} C")
        else:
            print(f"{loc:<30} | Error fetching data")

if __name__ == "__main__":
    test_all_ner_stations()

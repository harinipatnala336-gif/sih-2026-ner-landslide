# Smart India Hackathon 2026 - Idea Submission Deck Content
## Problem Statement ID: 26001
**Title:** AI-Based Early Warning and Landslide Risk Monitoring System in NER  
**Organization:** Ministry of Development of North Eastern Region (MDoNER)  
**Category:** Software | **Theme:** Disaster Management  
**Project Name:** DharaRakshak NER

---

### SLIDE 1: Title Slide
* **Idea Title:** DharaRakshak NER: Multi-Modal AI Landslide Early Warning & Offline-Resilient Warning Platform
* **Problem Statement ID:** 26001
* **Ministry / Department:** Ministry of Development of North Eastern Region (MDoNER)
* **Team Name:** [Your Team Name]
* **Team Leader:** Member 6

---

### SLIDE 2: Problem Statement & Regional Challenges
* **The NER Crisis:** The North Eastern Region faces acute vulnerability due to young, fragile Himalayan lithology, extreme monsoon rainfall, seismicity, and rapid highway expansion.
* **Key Lifelines Severed:** Vital arteries like NH-10 (Sikkim lifeline) and NH-29 (Nagaland) face chronic blockages, isolating entire districts for weeks and disrupting defense/civilian supply lines.
* **The Core Gap:** Existing monitoring is **reactive and manual**. Current systems lack real-time predictive triggering and fail to deliver warnings during hill network blackouts.

---

### SLIDE 3: Proposed Solution
* **Hybrid Two-Tier Prediction Engine:**
  1. *Static Susceptibility (LSM):* High-resolution terrain mapping (Slope, Aspect, Lithology, DEM).
  2. *Dynamic Trigger Model:* Real-time rainfall nowcasting (IMD radar) + InSAR satellite ground displacement detection.
* **Central Command GIS Portal:** Real-time risk heatmaps, automated route rerouting for NDRF/BRO, and critical infrastructure monitoring.
* **Offline-Resilient Alerting:** Delivering life-saving warnings via 2G GSM SMS and cell broadcast to cut through mountain connectivity blackouts.

---

### SLIDE 4: Technical Architecture & Workflow
* **Data Sources:** ISRO Bhuvan / Cartosat DEM, Sentinel-1 SAR (InSAR interferometry), IMD Doppler Weather Radar, and Citizen Ground Reports.
* **AI & Processing Layer:** Random Forest / XGBoost ensemble + Antecedent Precipitation Index (API).
* **Backend:** Scalable FastAPI microservices with PostGIS spatial indexing.
* **Frontends:** 
  * Authority GIS Command Dashboard (Leaflet/MapLibre).
  * Offline-First Citizen Mobile App (Flutter/PWA) with camera photo verification.

---

### SLIDE 5: Innovation & Uniqueness (Why We Win)
1. **Offline & 2G Resilient:** Works even when heavy monsoon rains knock out 4G/5G mobile towers.
2. **Pre-Failure Creep Detection:** Tracks millimeter-level ground subsidence using satellite radar before visible collapse occurs.
3. **Crowdsourced Ground Truth Verification:** Local villagers and drivers report road cracks with auto-GPS to calibrate AI probability in real-time.
4. **Emergency Lifeline Rerouting:** Automatically computes safe relief corridors when arterial national highways are blocked.

---

### SLIDE 6: Feasibility, Impact & Future Roadmap
* **Social Impact:** Saves lives, prevents tourist entrapment, and protects remote indigenous communities from isolation.
* **Strategic & Economic Value:** Enables Border Roads Organisation (BRO) and NDRF to pre-deploy earth-moving machinery *before* landslides strike.
* **Scalability:** The platform can scale across all 8 NER states and be extended to Uttarakhand, Himachal Pradesh, and Jammu & Kashmir.

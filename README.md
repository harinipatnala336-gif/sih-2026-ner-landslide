# SIH 2026 - MDoNER Problem Statement 26001
## AI-Based Early Warning and Landslide Risk Monitoring System in NER (North Eastern Region)

### 📌 Team Roles & Folder Ownership

| Member | Focus Area | Primary Folder | Key Deliverable |
| :--- | :--- | :--- | :--- |
| **Member 1** | Web GIS Dashboard | `web-dashboard/` | Interactive regional Leaflet/MapLibre map with hazard zones. |
| **Member 2** | Central Backend API | `backend/` | FastAPI server connecting DB, AI model, and endpoints. |
| **Member 3** | AI / ML Model | `ai-models/` | Scikit-learn / XGBoost landslide probability model (`model.pkl`). |
| **Member 4** | Weather & Remote Sensing | `backend/data_sources/` | Fetching IMD / OpenWeatherMap rainfall & DEM terrain data. |
| **Member 5 (You)** | Mobile App & Alerts | `mobile-app/` | Citizen hazard reporting & offline 2G SMS emergency alerts. |
| **Member 6** | Pitch, PPT & Coordination | `docs-ppt/` | Official SIH Idea Presentation deck & architecture diagrams. |

---

### 🚀 How to Push This Repository to GitHub

1. Go to [github.com](https://github.com) and click **New Repository**.
2. Name it: **`sih-2026-ner-landslide`** (leave it Public or Private).
3. Open your terminal in this folder (`C:\Users\harin\.gemini\antigravity\scratch\sih-2026-ner-landslide`) and run:
   ```bash
   git init
   git add .
   git commit -m "Initial SIH 2026 team repository structure"
   git branch -M main
   git remote add origin https://github.com/<YOUR-GITHUB-USERNAME>/sih-2026-ner-landslide.git
   git push -u origin main
   ```

---

### 💻 How Your Teammates Work on It

* **Clone to their laptop**:
  ```bash
  git clone https://github.com/<YOUR-GITHUB-USERNAME>/sih-2026-ner-landslide.git
  ```
* **Daily workflow before starting work**:
  ```bash
  git pull origin main
  ```
* **After adding their code in their folder**:
  ```bash
  git add .
  git commit -m "Updated backend API / Added new mobile screen"
  git push origin main
  ```

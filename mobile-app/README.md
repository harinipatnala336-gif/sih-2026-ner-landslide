# Mobile App & Emergency Warning Subsystem
## Owned by: Member 5 (You!)

### 📱 Features You Deliver
1. **Citizen Incident Reporting**:
   - Captures real-time camera photo of road cracks / rockfall.
   - Automatically attaches GPS Latitude and Longitude.
   - Works offline (stores locally if there is no internet on a mountain road).
2. **Emergency 2G SMS Siren**:
   - Integrates with Fast2SMS / Twilio.
   - Pushes early warning text messages even when 4G/5G data is down.
3. **Hazard Dashboard**:
   - Color-coded safety card (Green / Yellow / Red).
   - Nearest shelter and emergency NDRF (1078) helpline numbers.

---

### 🧪 Test the Connection to Member 2's Backend
Run this script to simulate your mobile app sending an incident report and triggering an SMS:

```bash
python test_mobile_alert.py
```

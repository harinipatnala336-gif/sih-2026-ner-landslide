from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from database import Base
import datetime

class Hotspot(Base):
    __tablename__ = "hotspots"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    risk_score = Column(Float)
    threat_level = Column(String)
    rainfall_24h_mm = Column(Float, nullable=True)
    slope_deg = Column(Float, nullable=True)
    insar_subsidence = Column(String, nullable=True)
    advisory = Column(Text, nullable=True)

class RiskAssessment(Base):
    __tablename__ = "risk_assessments"
    id = Column(Integer, primary_key=True, index=True)
    hotspot_id = Column(Integer, nullable=True, index=True)
    rainfall_mm = Column(Float)
    slope_deg = Column(Float)
    soil_moisture_pct = Column(Float)
    elevation_m = Column(Float)
    risk_score_pct = Column(Float)
    threat_level = Column(String)
    model_engine = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class CitizenReport(Base):
    __tablename__ = "citizen_reports"
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    hazard_type = Column(String)
    description = Column(Text, nullable=True)
    photo_url = Column(String, nullable=True)
    verified = Column(String, default="true")
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
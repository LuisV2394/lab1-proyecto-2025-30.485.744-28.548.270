from app import db
from datetime import datetime

# --- DIAGNOSES ---
class Diagnosis(db.Model):
    __tablename__ = 'diagnoses'
    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    code = db.Column(db.String(20), nullable=False) # Ej: CIE-10
    description = db.Column(db.String(255))
    type = db.Column(db.String(20)) # presumptive, definitive
    main = db.Column(db.Boolean, default=False)

# Relationships
    episode = db.relationship("Episode", backref=db.backref("diagnoses", lazy=True))
from app import db
from datetime import datetime

# --- CONSENTS ---
class Consent(db.Model):
    __tablename__ = 'consents'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("people.id") , nullable=False)
    process_type = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    # digital_signature, verbal_acceptance_with_registration
    method = db.Column(db.String(50), nullable=False) 
    file_id = db.Column(db.String(255)) # ID del archivo guardado en S3/Disco

# Relationships
    person = db.relationship("Person", backref=db.backref("consents", lazy=True))
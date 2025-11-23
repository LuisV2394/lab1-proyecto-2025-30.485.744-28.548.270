from app import db
from datetime import datetime

# Notes medical
class ClinicalNote(db.Model):
    __tablename__ = 'clinical_notes'
    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    professional_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Similar structure to SOAP but with your fields
    sub_objective = db.Column(db.Text) # Subjective
    objective = db.Column(db.Text)
    test = db.Column(db.Text) # Assessment / Tests realizados
    plan = db.Column(db.Text)
    
    
    # Attachment mockup: We will store a list of URLs or filenames in JSON
    attachments = db.Column(db.JSON, nullable=True)

# Relationships
    episode = db.relationship("Episode", backref=db.backref("clinical_notes", lazy=True))
    professional = db.relationship("Professional", backref=db.backref("clinical_notes", lazy=True))
from app import db
from datetime import datetime
from sqlalchemy.dialects.mysql import JSON

class ClinicalNote(db.Model):
    __tablename__ = 'clinical_notes'

    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey('professionals.id'), nullable=False)
    subjective = db.Column(db.Text, nullable=True)
    objective = db.Column(db.Text, nullable=True)
    assessment = db.Column(db.Text, nullable=True)
    plan = db.Column(db.Text, nullable=True)
    attachments = db.Column(JSON, nullable=True, default=[])
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    episode = db.relationship("Episode", back_populates="clinical_notes")
    professional = db.relationship("Professional", backref=db.backref("clinical_notes", lazy=True))
from app import db
from datetime import datetime

class Diagnosis(db.Model):
    __tablename__ = 'diagnoses'

    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    code = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(255))
    type_diagnoses = db.Column(
        db.Enum('PRESUMPTIVE', 'DEFINITIVE', name='diagnosis_type_enum'),
        nullable=False
    )
    main = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    episode = db.relationship("Episode", backref=db.backref("diagnoses", lazy=True))
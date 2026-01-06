from app import db
from datetime import datetime

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("people.id"), nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey("professionals.id"), nullable=True)
    unit_id = db.Column(db.Integer, db.ForeignKey("units.id"), nullable=True)
    motivo = db.Column(db.String(255), nullable=True)
    type_episode = db.Column(
        db.Enum('CONSULTATION', 'PROCEDURE', 'CONTROL', 'AMBULATORY_EMERGENCY', name='episode_type_enum'),
        nullable=False
    )
    started_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    closed_at = db.Column(db.DateTime)
    status = db.Column(db.Enum('OPEN', 'CLOSED', name='episode_status_enum'), default='OPEN', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    person = db.relationship("Person", backref=db.backref("episodes", lazy=True))
    professional = db.relationship("Professional", backref=db.backref("episodes", lazy=True))
    unit = db.relationship("Unit", backref=db.backref("episodes", lazy=True))
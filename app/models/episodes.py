# Episodes
from app import db
from datetime import datetime

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("people.id"), nullable=False)
    professional_id = db.Column(db.Integer)
    unit_id = db.Column(db.Integer)
    type = db.Column(
        db.Enum('CONSULTATION', 'EMERGENCY', 'ADMISSION', 'PROCEDURE'),
        nullable=False
    )
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    closed_at = db.Column(db.DateTime)
    status = db.Column(db.Enum('OPEN', 'CLOSED'), default='OPEN')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones
    person = db.relationship("Person", backref=db.backref("episodes", lazy=True))
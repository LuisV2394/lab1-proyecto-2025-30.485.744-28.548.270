from app import db
from datetime import datetime


class Professional(db.Model):
    __tablename__ = "professionals"

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("people.id"), nullable=False)
    registration = db.Column(db.String(80), nullable=False)  # matrícula profesional
    specialty = db.Column(db.String(120), nullable=False)
    subspecialty = db.Column(db.String(120))
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    schedule_enabled = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    person = db.relationship("Person", backref=db.backref("professional", uselist=False))

    def to_dict(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "registration": self.registration,
            "specialty": self.specialty,
            "subspecialty": self.subspecialty,
            "is_active": self.is_active,
            "schedule_enabled": self.schedule_enabled,
            "person": self.person.to_dict() if self.person else None
        }
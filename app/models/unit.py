from app import db
from datetime import datetime

class Unit(db.Model):
    __tablename__ = "units"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), nullable=False)
    type = db.Column(
        db.String(30),
        nullable=False,
        comment="SEDE, CONSULTORIO, SERVICIO"
    )
    description = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(45), nullable=True)
    schedule_reference = db.Column(db.String(140), nullable=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "address": self.address,
            "phone": self.phone,
            "schedule_reference": self.schedule_reference,
            "is_active": self.is_active
        }
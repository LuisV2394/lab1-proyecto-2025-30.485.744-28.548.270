from app import db
from datetime import datetime

class Person(db.Model):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    document_number = db.Column(db.String(50))
    gender = db.Column(db.Enum('M','F','OTHER'), default=None)
    birth_date = db.Column(db.Date)
    email = db.Column(db.String(255), unique=True)
    phone = db.Column(db.String(50))
    address = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    users = db.relationship("User", back_populates="person")
    
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "document_number": self.document_number,
            "gender": self.gender,
            "birth_date": self.birth_date.isoformat() if self.birth_date else None,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "active": self.active,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
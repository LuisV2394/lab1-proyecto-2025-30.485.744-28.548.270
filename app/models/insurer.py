from app import db
from datetime import datetime

class Insurer(db.Model):
    __tablename__ = "insurers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    tax_id = db.Column(db.String(50), unique=True, nullable=False)
    contact = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    invoices = db.relationship("Invoice", back_populates="insurer")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "tax_id": self.tax_id,
            "contact": self.contact,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
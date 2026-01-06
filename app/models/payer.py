from app import db
from datetime import datetime

class Payer(db.Model):
    __tablename__ = 'payers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    tax_id = db.Column(db.String(100), nullable=True)
    contact_email = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "tax_id": self.tax_id,
            "contact_email": self.contact_email,
            "phone": self.phone,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
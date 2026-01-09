from app import db
from datetime import datetime

class Tariff(db.Model):
    __tablename__ = 'plan_tariffs'

    id = db.Column(db.Integer, primary_key=True)
    prestation_id = db.Column(db.String(20), db.ForeignKey('services.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('coverage_plans.id'), nullable=False)
    price = db.Column(db.Numeric(12, 2), nullable=False)
    taxes = db.Column(db.Numeric(10, 2), default=0.0)
    valid_from = db.Column(db.Date, nullable=False)
    valid_until = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "prestation_id": self.prestation_id,
            "plan_id": self.plan_id,
            "price": float(self.price),
            "taxes": float(self.taxes),
            "total": float(self.price + self.taxes),
            "valid_from": self.valid_from.isoformat(),
            "valid_until": self.valid_until.isoformat() if self.valid_until else None
        }
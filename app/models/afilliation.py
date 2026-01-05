from app import db
from datetime import datetime

class Affiliation(db.Model):
    __tablename__ = 'affiliations'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('coverage_plans.id'), nullable=False)
    prayer_id = db.Column(db.Integer, db.ForeignKey('prayers.id'), nullable=True)
    policy_number = db.Column(db.String(50), nullable=False)
    card_number = db.Column(db.String(50))
    valid_from = db.Column(db.Date, nullable=False)
    valid_to = db.Column(db.Date)
    
    # Valores económicos
    copayment = db.Column(db.Numeric(10, 2), default=0.0) # Valor fijo por cita
    deductible = db.Column(db.Numeric(10, 2), default=0.0) # Porcentaje o valor base
    
    status = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "plan_id": self.plan_id,
            "policy_number": self.policy_number,
            "valid_from": self.valid_from.isoformat() if self.valid_from else None,
            "valid_until": self.valid_to.isoformat() if self.valid_to else None,
            "copayment": float(self.copayment),
            "deductible": float(self.deductible),
            "status": self.status
        }
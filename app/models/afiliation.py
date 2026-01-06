from app import db
from datetime import datetime

class Affiliation(db.Model):
    __tablename__ = 'affiliations'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)  # The person being affiliated
    plan_id = db.Column(db.Integer, db.ForeignKey('plans.id'), nullable=False)  # The insurance or coverage plan
    payer_id = db.Column(db.Integer, db.ForeignKey('payers.id'), nullable=True)  # Optional: the entity paying for the plan
    card_number = db.Column(db.String(50), nullable=False)  # Health card or membership number
    policy_number = db.Column(db.String(50))  # Policy number
    valid_from = db.Column(db.Date, nullable=False)
    valid_to = db.Column(db.Date)
    
    # Financial fields
    copayment = db.Column(db.Numeric(10, 2), default=0.0)  # Fixed co-pay per appointment
    coinsurance = db.Column(db.Numeric(10, 2), default=0.0)  # Portion of the cost the patient pays (cuota moderadora)
    status = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "plan_id": self.plan_id,
            "payer_id": self.payer_id,
            "card_number": self.card_number,
            "policy_number": self.policy_number,
            "valid_from": self.valid_from.isoformat() if self.valid_from else None,
            "valid_to": self.valid_to.isoformat() if self.valid_to else None,
            "copayment": float(self.copayment),
            "coinsurance": float(self.coinsurance),
            "status": self.status
        }
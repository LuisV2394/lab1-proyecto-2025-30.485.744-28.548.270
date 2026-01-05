from app import db
from datetime import datetime

class CoveragePlan(db.Model):
    __tablename__ = 'plans'

    id = db.Column(db.Integer, primary_key=True)
    payer_id = db.Column(db.Integer, db.ForeignKey('payers.id'), nullable=True)
    name = db.Column(db.String(100), nullable=False)
    general_conditions = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "payer_id": self.payer_id,
            "name": self.name,
            "general_conditions": self.general_conditions,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
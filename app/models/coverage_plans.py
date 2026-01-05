from app import db
from datetime import datetime

class CoveragePlan(db.Model):
    __tablename__ = 'plans'

    id = db.Column(db.Integer, primary_key=True)
    
    insurer_id = db.Column(db.Integer, db.ForeignKey('insurance.id'), nullable=False)
    
    name = db.Column(db.String(100), nullable=False)
    general_conditions = db.Column(db.Text) 
    
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "insurer_id": self.insurer_id,
            "name": self.name,
            "general_conditions": self.general_conditions,
            "active": self.active,
            "created_at": self.created_at.isoformat()
        }
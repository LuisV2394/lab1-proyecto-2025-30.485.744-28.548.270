from app import db
from datetime import datetime

class CoveragePlan(db.Model):
    __tablename__ = 'plans'

    id = db.Column(db.Integer, primary_key=True)
    
    insurer_id = db.Column(db.Integer, db.ForeignKey('insurance.id'), nullable=False)
    prayer_id = db.Column(db.Integer, db.ForeignKey('prayers.id'), nullable=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    general_conditions = db.Column(db.String(100))
    code = db.Column(db.String(50), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "insurer_id": self.insurer_id,
            "prayer_id": self.prayer_id,
            "name": self.name,
            "description": self.description,
            "general_conditions": self.general_conditions,
            "code": self.code,
            "active": self.active,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
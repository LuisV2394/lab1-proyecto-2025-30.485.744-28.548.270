from app import db
from datetime import datetime

class Prestation(db.Model):
    __tablename__ = 'prestations'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False) 
    name = db.Column(db.String(200), nullable=False)
    group_name = db.Column(db.String(100)) 
    requirements = db.Column(db.Text)
    estimated_time = db.Column(db.Integer)
    
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "group_name": self.group_name,
            "requirements": self.requirements,
            "estimated_time": self.estimated_time,
            "active": self.active
        }
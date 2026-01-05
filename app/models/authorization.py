from app import db
from datetime import datetime

class Authorization(db.Model):
    __tablename__ = 'authorizations'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('coverage_plans.id'), nullable=False)
    
    # status: requested, approved, denied
    status = db.Column(db.String(20), default='requested')
    
    request_date = db.Column(db.DateTime, default=datetime.utcnow)
    response_date = db.Column(db.DateTime, nullable=True)
    
    authorization_number = db.Column(db.String(100), nullable=True)
    observations = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "plan_id": self.plan_id,
            "status": self.status,
            "request_date": self.request_date.isoformat() if self.request_date else None,
            "response_date": self.response_date.isoformat() if self.response_date else None,
            "authorization_number": self.authorization_number,
            "observations": self.observations
        }
from app import db
from datetime import datetime

class OrderItem(db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    prestation_code = db.Column(db.String(50), nullable=False)
    instructions = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')
    result_id = db.Column(db.Integer, db.ForeignKey('results.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    order = db.relationship("Order", backref="order_items")
    
    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "prestation_code": self.prestation_code,
            "instructions": self.instructions,
            "status": self.status,
            "result_id": self.result_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
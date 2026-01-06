from app import db
from datetime import datetime

class OrderDetail(db.Model):
    __tablename__ = 'order_details'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    indications = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    order = db.relationship("Order", backref=db.backref(
        "details",
        cascade="all, delete-orphan"
    ))

    def to_dict(self):
        return {
            "code": self.code,
            "description": self.description,
            "indications": self.indications
        }
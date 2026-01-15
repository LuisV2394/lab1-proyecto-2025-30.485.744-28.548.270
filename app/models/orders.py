from app import db
from datetime import datetime
from sqlalchemy import Enum

status_enum = Enum(
    'issued', 'authorized', 'in_progress', 'completed', 'canceled',
    name='order_status'
)
priority_enum = Enum('normal', 'urgent', name='order_priority')

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey('professionals.id'), nullable=True)
    requires_authorization = db.Column(db.Boolean, default=False)
    type = db.Column(db.String(50), nullable=False)
    priority = db.Column(priority_enum, default='normal')
    status = db.Column(status_enum, default='issued')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    episode = db.relationship("Episode", back_populates="orders")
    professional = db.relationship("Professional", backref="orders")
    authorizations = db.relationship(
        "Authorization",
        back_populates="order",
        cascade="all, delete",
        passive_deletes=True
    )
    
    def to_dict(self):
        return {
            "id": self.id,
            "episode_id": self.episode_id,
            "professional_id": self.professional_id,
            "requires_authorization": self.requires_authorization,
            "type": self.type,
            "priority": self.priority,
            "status": self.status,
            "details": [d.to_dict() for d in self.details],
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
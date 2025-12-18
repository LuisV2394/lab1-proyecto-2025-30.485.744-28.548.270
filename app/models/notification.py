from app import db
from datetime import datetime

class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    template = db.Column(db.String(100), nullable=False)
    recipient = db.Column(db.String(255), nullable=False)
    payload = db.Column(db.JSON, nullable=True)
    status = db.Column(
        db.Enum('PENDING', 'SENT', 'FAILED'),
        default='PENDING',
        nullable=False
    )
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "template": self.template,
            "recipient": self.recipient,
            "payload": self.payload,
            "status": self.status,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
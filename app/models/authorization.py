from app import db
from datetime import datetime
import enum

class AuthorizationStatus(enum.Enum):
    REQUESTED = "REQUESTED"
    APPROVED = "APPROVED"
    DENIED = "DENIED"

class Authorization(db.Model):
    __tablename__ = 'authorizations'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=True)
    procedure_code = db.Column(db.String(50), nullable=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('plans.id'), nullable=False)
    status = db.Column(
        db.Enum(AuthorizationStatus),
        default=AuthorizationStatus.REQUESTED,
        nullable=False
    )
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
            "procedure_code": self.procedure_code,
            "plan_id": self.plan_id,
            "status": self.status.value,
            "request_date": self.request_date.isoformat() if self.request_date else None,
            "response_date": self.response_date.isoformat() if self.response_date else None,
            "authorization_number": self.authorization_number,
            "observations": self.observations,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
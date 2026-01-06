from app import db
from datetime import datetime

class CreditDebitNote(db.Model):
    __tablename__ = 'credit_debit_notes'

    id = db.Column(db.Integer, primary_key=True)
    factura_id = db.Column(db.Integer, db.ForeignKey('invoices.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    reason = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relación con la factura
    invoice = db.relationship("Invoice", backref=db.backref(
        "credit_debit_notes",
        cascade="all, delete-orphan"
    ))

    def to_dict(self):
        return {
            "id": self.id,
            "factura_id": self.factura_id,
            "amount": self.amount,
            "reason": self.reason,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
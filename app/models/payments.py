from app import db
from datetime import datetime

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id'), nullable=False)
    amount = db.Column(db.Numeric(12, 2), nullable=False)
    payment_method = db.Column(
        db.Enum('CASH', 'CARD', 'TRANSFER', name='payment_method_enum'),
        nullable=False
    )
    reference = db.Column(db.String(255))
    paid_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationship
    invoice = db.relationship('Invoice', backref=db.backref('payments', lazy=True))
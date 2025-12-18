from app import db
from datetime import date

class Invoice(db.Model):
    __tablename__ = "invoices"

    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(50), nullable=False)
    issue_date = db.Column(db.Date, nullable=False, default=date.today)
    patient_id = db.Column(db.Integer, db.ForeignKey("people.id"), nullable=True)
    insurer_id = db.Column(db.Integer, db.ForeignKey("insurers.id"), nullable=True)
    currency = db.Column(db.String(3), nullable=False, default="USD")
    subtotal = db.Column(db.Numeric(12,2), nullable=False, default=0)
    total = db.Column(db.Numeric(12,2), nullable=False, default=0)
    status = db.Column(db.Enum("PENDING","ISSUED","PAID","CANCELLED", name="invoice_status"), nullable=False, default="PENDING")
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Relationships
    items = db.relationship("InvoiceItem", backref="invoice", cascade="all, delete-orphan")
    insurer = db.relationship("Insurer", back_populates="invoices")

    def to_dict(self, include_items=False):
        data = {
            "id": self.id,
            "invoiceNumber": self.invoice_number,
            "issueDate": self.issue_date.isoformat(),
            "patientId": self.patient_id,
            "insurerId": self.insurer_id,
            "currency": self.currency,
            "subtotal": float(self.subtotal),
            "total": float(self.total),
            "status": self.status.lower()
        }
        if include_items:
            data["items"] = [item.to_dict() for item in self.items]
        return data
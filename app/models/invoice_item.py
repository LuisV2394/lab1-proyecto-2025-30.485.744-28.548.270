from app import db

class InvoiceItem(db.Model):
    __tablename__ = "invoice_items"

    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey("invoices.id"), nullable=False)
    prestation_id = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Numeric(10,2), nullable=False, default=0)
    unit_price = db.Column(db.Numeric(12,2), nullable=False, default=0)
    tax_amount = db.Column(db.Numeric(12,2), nullable=False, default=0)
    total_price = db.Column(db.Numeric(12,2), nullable=False, default=0)

    def to_dict(self):
        return {
        "prestationCode": self.prestation_id,
        "description": self.description,
        "quantity": float(self.quantity),
        "unitPrice": float(self.unit_price),
        "taxAmount": float(self.tax_amount),
        "total": float(self.total_price)
        }
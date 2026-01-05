from app import db
from datetime import datetime

class InsuranceCompany(db.Model):
    __tablename__ = 'insurance'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    tax_nit = db.Column(db.String(50), unique=True, nullable=False) # Identificación tributaria
    contact = db.Column(db.String(100)) # Nombre de contacto o teléfono
    status = db.Column(db.Boolean, default=True) # Activo / Inactivo
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "tax_nit": self.tax_nit,
            "contact": self.contact,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }
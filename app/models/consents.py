from app import db
from datetime import datetime

class Consent(db.Model):
    __tablename__ = 'consents'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("people.id"), nullable=False)
    process_type = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    method = db.Column(
        db.Enum("DIGITAL_SIGNATURE", "VERBAL_WITH_RECORD", name="consent_method_enum"),
        nullable=False
    )
    file_id = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    person = db.relationship("Person", backref=db.backref("consents", lazy=True))
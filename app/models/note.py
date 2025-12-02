from app import db
from datetime import datetime

class ClinicalNote(db.Model):
    __tablename__ = 'clinical_notes'

    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey('professionals.id'), nullable=False)

    # ENUM en la base de datos
    note_type = db.Column(
        db.Enum('EVOLUTION', 'NURSING_NOTE', 'INTERCONSULTATION', 'OTHER'),
        nullable=False,
        default='EVOLUTION'
    )

    # En tu BD solo existe un campo de texto general
    content = db.Column(db.Text, nullable=True)

    # Versionado
    version = db.Column(db.Integer, default=1, nullable=False)

    # Este reemplaza a "date"
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relaciones
    episode = db.relationship("Episode", backref=db.backref("clinical_notes", lazy=True))
    professional = db.relationship("Professional", backref=db.backref("clinical_notes", lazy=True))

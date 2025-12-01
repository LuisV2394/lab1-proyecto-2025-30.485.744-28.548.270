from app import db
from datetime import datetime
from app.models.professional import Professional
from app.models.unit import Unit

class Block(db.Model):
    __tablename__ = 'agenda_blocks'
    
    id = db.Column(db.Integer, primary_key=True)
    professional_id = db.Column(
        db.Integer,
        db.ForeignKey("professionals.id"),
        nullable=False
    )
    unit_id = db.Column(
        db.Integer,
        db.ForeignKey("units.id"),
        nullable=False
    )
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    state = db.Column(
        db.Enum('AVAILABLE','BLOCKED','OCCUPIED', name='block_state_enum'),
        default='AVAILABLE',
        nullable=False
    )
    type = db.Column(
        db.Enum('CONSULTATION','PROCEDURE','INTERCONSULTATION', name='block_type_enum'),
        default='CONSULTATION',
        nullable=False
    )
    capacity = db.Column(db.Integer, default=1)
    notes = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones
    professional = db.relationship(
        Professional,
        backref=db.backref("blocks", lazy=True)
    )
    unit = db.relationship(
        Unit,
        backref=db.backref("blocks", lazy=True)
    )
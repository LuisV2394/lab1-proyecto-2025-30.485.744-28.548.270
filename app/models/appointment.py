from app import db
from datetime import datetime

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("people.id"), nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey("professionals.id"), nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey("units.id"), nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False, default=30)
    motivo = db.Column(db.Text, nullable=False)
    canal = db.Column(
        db.Enum('PRESENCIAL', 'VIRTUAL', name='appointment_channel_enum'),
        nullable=False
    )
    observations = db.Column(db.Text, nullable=True)
    status = db.Column(
        db.Enum(
            'SOLICITADA', 'CONFIRMADA', 'CUMPLIDA', 'CANCELADA', 'NO_ASISTIDA',
            name='appointment_status_enum'
        ),
        default='SOLICITADA',
        nullable=False
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relaciones
    person = db.relationship("Person", backref=db.backref("appointments", lazy=True))
    professional = db.relationship("Professional", backref=db.backref("appointments", lazy=True))
    unit = db.relationship("Unit", backref=db.backref("appointments", lazy=True))

class AppointmentHistory(db.Model):
    __tablename__ = 'appointment_history'

    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'), nullable=False)
    old_state = db.Column(db.Enum(
        'SOLICITADA', 'CONFIRMADA', 'CUMPLIDA', 'CANCELADA', 'NO_ASISTIDA',
        name='appointment_status_enum'
    ))
    new_state = db.Column(db.Enum(
        'SOLICITADA', 'CONFIRMADA', 'CUMPLIDA', 'CANCELADA', 'NO_ASISTIDA',
        name='appointment_status_enum'
    ))
    changed_at = db.Column(db.DateTime, default=datetime.utcnow)
    changed_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    
    appointment = db.relationship("Appointment", backref=db.backref("history", lazy=True))
    user = db.relationship("User", backref=db.backref("appointment_changes", lazy=True))

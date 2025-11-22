from agenda import db, Block
from datetime import datetime

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, nullable=False)
    professional_id = db.Column(db.Integer, nullable=False)
    unit_id = db.Column(db.Integer, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.String(255))
    channel = db.Column(db.String(50)) # in person, online
    state = db.Column(db.String(20), default='request') # request, confirmed, fulfilled, canceled, unassisted
    observations = db.Column(db.Text)
    
    # Relación para validaciones
    block_id = db.Column(db.Integer, db.ForeignKey('blocks.id'), nullable=True)

class AppointmentHistory(db.Model):
    __tablename__ = 'appointment_history'
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'))
    old_state = db.Column(db.String(20))
    new_state = db.Column(db.String(20))
    changed_at = db.Column(db.DateTime, default=datetime.utcnow)
    changed_by = db.Column(db.Integer) # ID del usuario que hizo el cambio
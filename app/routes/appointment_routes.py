from flask import Blueprint, request, jsonify
from models.appointment import db, Appointment, AppointmentHistory
from models.agenda import Block
from app import db
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

appt_bp = Blueprint('appointment', __name__)

# Diccionario de transiciones válidas
VALID_TRANSITIONS = {
    'request': ['confirmed', 'canceled'],
    'confirmed': ['fulfilled', 'canceled', 'unassisted', 'request'], # request si se reprograma
    'fulfilled': [], # Estado final
    'canceled': [],  # Estado final
    'unassisted': [] # Estado final
}

@appt_bp.route('/appointment', methods=['POST'])
@jwt_required()
@swag_from('../docs/appointment_create.yml')
def create_appointment():
    data = request.json
    start = datetime.fromisoformat(data.get('start'))
    end = datetime.fromisoformat(data.get('end'))
    prof_id = data.get('professionalId')
    
    # REGLA 1: Validar que la cita esté dentro de un bloque abierto
    target_block = Block.query.filter(
        Block.professional_id == prof_id,
        Block.start <= start,
        Block.end >= end,
        Block.state == 'open'
    ).first()
    
    if not target_block:
        return jsonify({"error": "No existe agenda abierta para este horario"}), 400

    # REGLA 2: Validar capacidad (ability)
    # Contar citas activas en ese bloque que se solapen con el horario solicitado
    current_appts = Appointment.query.filter(
        Appointment.block_id == target_block.id,
        Appointment.state.in_(['request', 'confirmed']),
        Appointment.start < end,
        Appointment.end > start
    ).count()
    
    if current_appts >= target_block.ability:
        return jsonify({"error": "No hay cupo disponible en este bloque"}), 409

    # Crear cita
    new_appt = Appointment(
        person_id=data.get('personId'),
        professional_id=prof_id,
        unit_id=data.get('unitId'),
        block_id=target_block.id,
        start=start,
        end=end,
        reason=data.get('reason'),
        channel=data.get('channel'),
        state='request', # Estado inicial
        observations=data.get('observations')
    )
    
    db.session.add(new_appt)
    
    # Log Historial (Creación)
    log = AppointmentHistory(appointment=new_appt, old_state=None, new_state='request', changed_by=get_jwt_identity())
    db.session.add(log)
    
    db.session.commit()
    return jsonify({"message": "Cita solicitada con éxito", "id": new_appt.id}), 201

@appt_bp.route('/appointment/<int:id>/status', methods=['PUT'])
@jwt_required()
@swag_from('../docs/appointment_update.yml')
def update_appointment_status(id):
    data = request.json
    new_state = data.get('state')
    appt = Appointment.query.get_or_404(id)
    
    # REGLA 3: Transiciones válidas
    if new_state not in VALID_TRANSITIONS.get(appt.state, []):
        return jsonify({
            "error": f"Transición inválida de {appt.state} a {new_state}"
        }), 400
        
    # Si es reprogramación (cambio de fecha), verificar disponibilidad nuevamente
    if new_state == 'request' and 'start' in data:
        # ... Aquí repetirías la lógica de validación de bloque y capacidad ...
        pass

    # REGLA 4: Registro de historial
    history = AppointmentHistory(
        appointment_id=appt.id,
        old_state=appt.state,
        new_state=new_state,
        changed_by=get_jwt_identity() # ID del usuario JWT
    )
    
    appt.state = new_state
    if 'observations' in data:
        appt.observations = data['observations']
        
    db.session.add(history)
    db.session.commit()
    
    return jsonify({"message": "Estado actualizado", "state": appt.state})
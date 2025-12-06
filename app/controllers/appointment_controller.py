from flask import request, jsonify
from datetime import datetime, timedelta
from sqlalchemy import func, text
from flask_jwt_extended import get_jwt_identity

from app.models.appointment import db, Appointment, AppointmentHistory
from app.models.agenda import Block

# Transiciones válidas
VALID_TRANSITIONS = {
    "PENDING": ["CONFIRMED", "CANCELLED", "RESCHEDULED", "NO_SHOW"],
    "CONFIRMED": ["IN_PROGRESS", "CANCELLED", "RESCHEDULED", "NO_SHOW"],
    "IN_PROGRESS": ["COMPLETED", "CANCELLED", "NO_SHOW"],
    "COMPLETED": [],
    "CANCELLED": [],
    "RESCHEDULED": ["PENDING", "CONFIRMED"],
    "NO_SHOW": []
}


# ---------------------------------------------------------
#   CONTROLADOR: CREAR APPOINTMENT
# ---------------------------------------------------------
def create_appointment_controller():
    data = request.json

    try:
        scheduled_at = datetime.fromisoformat(data.get('start'))
        duration = int(data.get('duration_minutes', 30))
        end_time = scheduled_at + timedelta(minutes=duration)
        prof_id = data.get('professionalId')

        # Buscar bloque disponible
        target_block = Block.query.filter(
            Block.professional_id == prof_id,
            Block.date == scheduled_at.date(),
            Block.start_time <= scheduled_at.time(),
            Block.end_time >= end_time.time(),
            Block.state == 'AVAILABLE'
        ).first()

        if not target_block:
            return jsonify({"error": "No existe agenda abierta para este horario"}), 400

        # Validar capacidad
        current_appts = Appointment.query.filter(
            Appointment.agenda_block_id == target_block.id,
            Appointment.status.in_(['PENDING', 'CONFIRMED']),
            Appointment.scheduled_at < end_time,
            func.timestampadd(text('MINUTE'), Appointment.duration_minutes, Appointment.scheduled_at) > scheduled_at
        ).count()

        if current_appts >= target_block.capacity:
            return jsonify({"error": "No hay cupo disponible en este bloque"}), 409

        # Crear cita
        new_appt = Appointment(
            person_id=data.get('personId'),
            professional_id=prof_id,
            unit_id=data.get('unitId'),
            agenda_block_id=target_block.id,
            scheduled_at=scheduled_at,
            duration_minutes=duration,
            type=data.get('type', 'CONSULTATION'),
            reason=data.get('reason'),
            status='PENDING'
        )
        db.session.add(new_appt)

        # Registro en historial
        log = AppointmentHistory(
            appointment=new_appt,
            old_state=None,
            new_state='PENDING',
            changed_by=get_jwt_identity()
        )
        db.session.add(log)

        db.session.commit()

        return jsonify({"message": "Cita solicitada con éxito", "id": new_appt.id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500



# ---------------------------------------------------------
#   CONTROLADOR: ACTUALIZAR ESTADO DEL APPOINTMENT
# ---------------------------------------------------------
def update_appointment_status_controller(id):
    data = request.json
    new_status = data.get('status')
    appt = Appointment.query.get_or_404(id)

    # Validar transición
    if new_status not in VALID_TRANSITIONS.get(appt.status, []):
        return jsonify({
            "error": f"Transición inválida de {appt.status} a {new_status}"
        }), 400

    # Reprogramación (si aplica)
    if new_status == 'PENDING' and 'start' in data:
        # Aquí puedes repetir lógica de validación del bloque o crear un servicio aparte
        pass

    # Registrar historial
    history = AppointmentHistory(
        appointment_id=appt.id,
        old_state=appt.status,
        new_state=new_status,
        changed_by=get_jwt_identity()
    )

    appt.status = new_status

    if 'observations' in data:
        appt.observations = data['observations']

    db.session.add(history)
    db.session.commit()

    return jsonify({"message": "Estado actualizado", "status": appt.status})
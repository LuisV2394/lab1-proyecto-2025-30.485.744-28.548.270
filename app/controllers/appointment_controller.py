from flask import request, jsonify
from datetime import datetime, timedelta
from sqlalchemy import func, text
from flask_jwt_extended import get_jwt_identity

from app.models.appointment import db, Appointment, AppointmentHistory
from app.models.agenda import Block

VALID_TRANSITIONS = {
    "PENDING": ["CONFIRMED", "CANCELLED", "RESCHEDULED", "NO_SHOW"],
    "CONFIRMED": ["IN_PROGRESS", "CANCELLED", "RESCHEDULED", "NO_SHOW"],
    "IN_PROGRESS": ["COMPLETED", "CANCELLED", "NO_SHOW"],
    "COMPLETED": [],
    "CANCELLED": [],
    "RESCHEDULED": ["PENDING", "CONFIRMED"],
    "NO_SHOW": []
}

def create_appointment_controller():
    data = request.json

    try:
        start = datetime.fromisoformat(data.get('start'))
        duration = int(data.get('duration_minutes', 30))
        end = start + timedelta(minutes=duration)
        prof_id = data.get('professionalId')

        # Buscar bloque disponible
        target_block = Block.query.filter(
            Block.professional_id == prof_id,
            Block.date == start.date(),
            Block.start_time <= start.time(),
            Block.end_time >= end.time(),
            Block.state == 'AVAILABLE'
        ).first()

        if not target_block:
            return jsonify({"error": "No existe agenda abierta para este horario"}), 400

        # Verificar disponibilidad en el bloque
        current_appts = Appointment.query.filter(
            Appointment.agenda_block_id == target_block.id,
            Appointment.status.in_(['PENDING', 'CONFIRMED']),
            Appointment.start < end,
            func.timestampadd(text('MINUTE'), Appointment.duration_minutes, Appointment.start) > start
        ).count()

        if current_appts >= target_block.capacity:
            return jsonify({"error": "No hay cupo disponible en este bloque"}), 409

        # Crear la cita
        new_appt = Appointment(
            person_id=data.get('personId'),
            professional_id=prof_id,
            unit_id=data.get('unitId'),
            agenda_block_id=target_block.id,
            start=start,
            end=end,
            duration_minutes=duration,
            motivo=data.get('motivo'),
            canal=data.get('canal', 'CONSULTATION'),
            observations=data.get('observations'),
            status='PENDING'
        )
        db.session.add(new_appt)

        # Registrar historial
        log = AppointmentHistory(
            appointment=new_appt,
            old_state=None,
            new_state='PENDING',
            changed_by=get_jwt_identity()
        )
        db.session.add(log)
        db.session.commit()

        return jsonify({"message": "Cita creada con éxito", "id": new_appt.id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


def list_appointments_controller():
    appts = Appointment.query.all()
    result = []

    for a in appts:
        result.append({
            "id": a.id,
            "person_id": a.person_id,
            "professional_id": a.professional_id,
            "unit_id": a.unit_id,
            "agenda_block_id": a.agenda_block_id,
            "start": a.start.isoformat(),
            "end": a.end.isoformat(),
            "duration_minutes": a.duration_minutes,
            "motivo": a.motivo,
            "canal": a.canal,
            "observations": a.observations,
            "status": a.status
        })

    return jsonify(result), 200


def get_appointment_controller(id):
    appt = Appointment.query.get(id)

    if not appt:
        return jsonify({"error": "Cita no encontrada"}), 404

    data = {
        "id": appt.id,
        "person_id": appt.person_id,
        "professional_id": appt.professional_id,
        "unit_id": appt.unit_id,
        "agenda_block_id": appt.agenda_block_id,
        "start": appt.start.isoformat(),
        "end": appt.end.isoformat(),
        "duration_minutes": appt.duration_minutes,
        "motivo": appt.motivo,
        "canal": appt.canal,
        "observations": appt.observations,
        "status": appt.status
    }

    return jsonify(data), 200


def update_appointment_controller(id):
    appt = Appointment.query.get(id)

    if not appt:
        return jsonify({"error": "Cita no encontrada"}), 404

    data = request.json

    if "start" in data:
        try:
            appt.start = datetime.fromisoformat(data["start"])
            if "duration_minutes" in data:
                appt.duration_minutes = int(data["duration_minutes"])
            appt.end = appt.start + timedelta(minutes=appt.duration_minutes)
        except ValueError:
            return jsonify({"error": "Fecha/hora inválida"}), 400

    appt.motivo = data.get("motivo", appt.motivo)
    appt.canal = data.get("canal", appt.canal)
    appt.observations = data.get("observations", appt.observations)
    appt.duration_minutes = data.get("duration_minutes", appt.duration_minutes)

    db.session.commit()

    return jsonify({"message": "Cita actualizada correctamente"}), 200


def update_appointment_status_controller(id):
    data = request.json
    new_status = data.get('status')
    appt = Appointment.query.get_or_404(id)

    if new_status not in VALID_TRANSITIONS.get(appt.status, []):
        return jsonify({
            "error": f"Transición inválida de {appt.status} a {new_status}"
        }), 400

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


def delete_appointment_controller(id):
    appt = Appointment.query.get(id)

    if not appt:
        return jsonify({"error": "Cita no encontrada"}), 404

    appt.status = "CANCELLED"
    db.session.commit()

    return jsonify({"message": "Cita cancelada"}), 200
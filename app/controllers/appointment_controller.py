from flask import request, jsonify
from datetime import datetime, timedelta
from flask_jwt_extended import get_jwt_identity

from app.models.appointment import db, Appointment, AppointmentHistory
from app.models.professional import Professional
from app.models.unit import Unit
from app.models.person import Person

VALID_TRANSITIONS = {
    "SOLICITADA": ["CONFIRMADA", "CANCELADA", "NO_ASISTIDA"],
    "CONFIRMADA": ["CUMPLIDA", "CANCELADA", "NO_ASISTIDA"],
    "CUMPLIDA": [],
    "CANCELADA": [],
    "NO_ASISTIDA": []
}

VALID_CHANNELS = ["PRESENCIAL", "VIRTUAL"]

def create_appointment_controller():
    data = request.json or {}

    try:
        # Campos obligatorios
        if not all([data.get('start'), data.get('professionalId'), data.get('unitId'), data.get('personId')]):
            return jsonify({"error": "Faltan campos obligatorios"}), 400

        # Parsear fecha/hora
        try:
            start = datetime.fromisoformat(data.get('start'))
        except ValueError:
            return jsonify({"error": "Formato de fecha/hora inválido"}), 400

        # Duración
        duration = int(data.get('duration_minutes', 30))
        if duration <= 0:
            return jsonify({"error": "La duración debe ser mayor a 0"}), 400

        end = start + timedelta(minutes=duration)

        prof_id = data.get('professionalId')
        unit_id = data.get('unitId')
        person_id = data.get('personId')

        # Validar existencia FK
        if not Professional.query.get(prof_id):
            return jsonify({"error": "El profesional no existe"}), 404
        if not Unit.query.get(unit_id):
            return jsonify({"error": "La unidad no existe"}), 404
        if not Person.query.get(person_id):
            return jsonify({"error": "La persona no existe"}), 404

        # Validar canal
        canal = data.get('canal', 'PRESENCIAL').upper()
        if canal not in VALID_CHANNELS:
            return jsonify({"error": f"Canal inválido. Debe ser {VALID_CHANNELS}"}), 400

        # Validar colisiones por profesional
        prof_conflict = Appointment.query.filter(
            Appointment.professional_id == prof_id,
            Appointment.start < end,
            Appointment.end > start
        ).first()

        if prof_conflict:
            return jsonify({
                "error": "El profesional ya tiene una cita en ese horario",
                "conflict_id": prof_conflict.id
            }), 409

        # Validar colisiones por unidad
        unit_conflict = Appointment.query.filter(
            Appointment.unit_id == unit_id,
            Appointment.start < end,
            Appointment.end > start
        ).first()

        if unit_conflict:
            return jsonify({
                "error": "La unidad ya está ocupada en ese horario",
                "conflict_id": unit_conflict.id
            }), 409

        # Crear cita
        new_appt = Appointment(
            person_id=person_id,
            professional_id=prof_id,
            unit_id=unit_id,
            start=start,
            end=end,
            duration_minutes=duration,
            motivo=data.get('motivo'),
            canal=canal,
            observations=data.get('observations'),
            status='SOLICITADA'
        )
        db.session.add(new_appt)

        # Historial
        log = AppointmentHistory(
            appointment=new_appt,
            old_state=None,
            new_state='SOLICITADA',
            changed_by=get_jwt_identity()
        )
        db.session.add(log)

        db.session.commit()

        return jsonify({
            "message": "Cita creada con éxito",
            "id": new_appt.id
        }), 201

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
    if "canal" in data:
        canal = data.get("canal").upper()
        if canal not in VALID_CHANNELS:
            return jsonify({"error": f"Canal inválido. Debe ser {VALID_CHANNELS}"}), 400
        appt.canal = canal
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

    appt.status = "CANCELADA"
    db.session.commit()

    return jsonify({"message": "Cita cancelada"}), 200
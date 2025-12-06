from flask import request, jsonify
from app.models.agenda import db, Block
from datetime import datetime

def create_block_controller():
    data = request.json

    # Obtener datos del request
    prof_id = data.get('professionalId')
    unit_id = data.get('unitId')
    date_str = data.get('date')
    start_str = data.get('start_time')
    end_str = data.get('end_time')
    block_type = data.get('type', 'CONSULTATION')       # Default tipo
    state = data.get('state', 'AVAILABLE')              # Default estado
    capacity = data.get('capacity', 1)
    notes = data.get('notes', '')

    # Validar campos obligatorios
    if not all([prof_id, unit_id, date_str, start_str, end_str]):
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    # Convertir strings a date/time
    try:
        block_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        start_time = datetime.strptime(start_str, "%H:%M:%S").time()
        end_time = datetime.strptime(end_str, "%H:%M:%S").time()
    except (TypeError, ValueError):
        return jsonify({"error": "Formato de fecha/hora inválido"}), 400

    # Validar orden de las horas
    if start_time >= end_time:
        return jsonify({"error": "La hora de inicio debe ser anterior a la hora de fin"}), 400

    # Validar solapamiento
    overlap = Block.query.filter(
        Block.professional_id == prof_id,
        Block.date == block_date,
        Block.start_time < end_time,
        Block.end_time > start_time,
        Block.state != 'BLOCKED'
    ).first()

    if overlap:
        return jsonify({"error": "El profesional ya tiene un bloque en este horario"}), 409

    # Crear bloque
    new_block = Block(
        professional_id=prof_id,
        unit_id=unit_id,
        date=block_date,
        start_time=start_time,
        end_time=end_time,
        state=state,
        type=block_type,
        capacity=capacity,
        notes=notes
    )

    db.session.add(new_block)
    db.session.commit()

    return jsonify({"message": "Bloque creado", "id": new_block.id}), 201
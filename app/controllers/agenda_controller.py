from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from app.models.agenda import db, Block
from datetime import datetime
from app.models.professional import Professional
from app.models.unit import Unit

def list_blocks_controller():
    blocks = Block.query.all()
    result = []

    for b in blocks:
        result.append({
            "id": b.id,
            "professional_id": b.professional_id,
            "unit_id": b.unit_id,
            "date": b.date.isoformat(),
            "start_time": b.start_time.isoformat(),
            "end_time": b.end_time.isoformat(),
            "type": b.type,
            "state": b.state,
            "capacity": b.capacity,
            "notes": b.notes
        })

    return jsonify(result), 200

def get_block_controller(block_id):
    block = Block.query.get(block_id)

    if not block:
        return jsonify({"error": "Bloque no encontrado"}), 404

    data = {
        "id": block.id,
        "professional_id": block.professional_id,
        "unit_id": block.unit_id,
        "date": block.date.isoformat(),
        "start_time": block.start_time.isoformat(),
        "end_time": block.end_time.isoformat(),
        "type": block.type,
        "state": block.state,
        "capacity": block.capacity,
        "notes": block.notes
    }

    return jsonify(data), 200

def create_block_controller():
    data = request.json or {}

    prof_id = data.get('professionalId')
    unit_id = data.get('unitId')
    date_str = data.get('date')
    start_str = data.get('start_time')
    end_str = data.get('end_time')
    block_type = data.get('type', 'CONSULTATION')
    state = data.get('state', 'AVAILABLE')
    capacity = data.get('capacity', 1)
    notes = data.get('notes', '')

    if not all([prof_id, unit_id, date_str, start_str, end_str]):
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    try:
        block_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        start_time = datetime.strptime(start_str, "%H:%M:%S").time()
        end_time = datetime.strptime(end_str, "%H:%M:%S").time()
    except (TypeError, ValueError):
        return jsonify({"error": "Formato de fecha/hora inválido"}), 400

    if start_time >= end_time:
        return jsonify({"error": "La hora de inicio debe ser anterior a la hora de fin"}), 400

    if capacity <= 0:
        return jsonify({"error": "La capacidad debe ser mayor a 0"}), 400

    if not Professional.query.get(prof_id):
        return jsonify({"error": "El profesional no existe"}), 404

    if not Unit.query.get(unit_id):
        return jsonify({"error": "La unidad no existe"}), 404

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

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Error de integridad en los datos"}), 400

    return jsonify({"message": "Bloque creado", "id": new_block.id}), 201

def update_block_controller(block_id):
    block = Block.query.get(block_id)

    if not block:
        return jsonify({"error": "Bloque no encontrado"}), 404

    data = request.json or {}

    # 🔹 Validar FK solo si vienen en el payload
    if 'professionalId' in data:
        if not Professional.query.get(data['professionalId']):
            return jsonify({"error": "El profesional no existe"}), 404
        block.professional_id = data['professionalId']

    if 'unitId' in data:
        if not Unit.query.get(data['unitId']):
            return jsonify({"error": "La unidad no existe"}), 404
        block.unit_id = data['unitId']

    block.type = data.get('type', block.type)
    block.state = data.get('state', block.state)

    if 'capacity' in data:
        if data['capacity'] <= 0:
            return jsonify({"error": "La capacidad debe ser mayor a 0"}), 400
        block.capacity = data['capacity']

    block.notes = data.get('notes', block.notes)

    if data.get('date'):
        try:
            block.date = datetime.strptime(data['date'], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Fecha inválida"}), 400

    if data.get('start_time'):
        try:
            block.start_time = datetime.strptime(data['start_time'], "%H:%M:%S").time()
        except ValueError:
            return jsonify({"error": "Hora de inicio inválida"}), 400

    if data.get('end_time'):
        try:
            block.end_time = datetime.strptime(data['end_time'], "%H:%M:%S").time()
        except ValueError:
            return jsonify({"error": "Hora de fin inválida"}), 400

    if block.start_time >= block.end_time:
        return jsonify({"error": "La hora de inicio debe ser anterior a la hora de fin"}), 400

    overlap = Block.query.filter(
        Block.id != block_id,
        Block.professional_id == block.professional_id,
        Block.date == block.date,
        Block.start_time < block.end_time,
        Block.end_time > block.start_time,
        Block.state != 'BLOCKED'
    ).first()

    if overlap:
        return jsonify({"error": "El profesional ya tiene un bloque en este horario"}), 409

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Error de integridad en los datos"}), 400

    return jsonify({"message": "Bloque actualizado"}), 200

def delete_block_controller(block_id):
    block = Block.query.get(block_id)

    if not block:
        return jsonify({"error": "Bloque no encontrado"}), 404

    db.session.delete(block)
    db.session.commit()

    return jsonify({"message": "Bloque eliminado"}), 200

def soft_delete_block_controller(block_id):
    block = Block.query.get(block_id)

    if not block:
        return jsonify({"error": "Bloque no encontrado"}), 404

    block.state = "DELETED"

    db.session.commit()

    return jsonify({"message": "Bloque marcado como eliminado"}), 200
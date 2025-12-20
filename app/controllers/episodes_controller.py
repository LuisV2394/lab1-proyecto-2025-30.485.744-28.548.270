from flask import jsonify, request
from app.models.episodes import Episode
from app import db
from datetime import datetime
from app.models.person import Person
from app.models.professional import Professional
from app.models.unit import Unit

# Función auxiliar para regla de negocio futura
def check_orders_completed(episode_id):
    # Lógica futura: return Order.query.filter(...).count() == 0
    return True

def create_episode_controller():
    data = request.json or {}

    try:
        # 1️⃣ Campos obligatorios
        if not all([data.get('person_id'), data.get('type')]):
            return jsonify({"error": "Faltan campos obligatorios"}), 400

        person_id = data.get('person_id')
        professional_id = data.get('professional_id')
        unit_id = data.get('unit_id')

        # 2️⃣ Validar existencia de la persona
        if not Person.query.get(person_id):
            return jsonify({"error": "La persona no existe"}), 404

        # 3️⃣ Validar existencia del profesional si se envía
        if professional_id and not Professional.query.get(professional_id):
            return jsonify({"error": "El profesional no existe"}), 404

        # 4️⃣ Validar existencia de la unidad si se envía
        if unit_id and not Unit.query.get(unit_id):
            return jsonify({"error": "La unidad no existe"}), 404

        # 5️⃣ Crear nuevo episodio
        new_episode = Episode(
            person_id=person_id,
            professional_id=professional_id,
            unit_id=unit_id,
            type=data.get('type'),  # CONSULTATION, EMERGENCY, etc.
            status='OPEN',
            started_at=datetime.utcnow()
        )

        db.session.add(new_episode)
        db.session.commit()

        return jsonify({
            "message": "Episodio abierto",
            "id": new_episode.id
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# READ ALL – Obtener todos los episodios
def get_all_episodes_controller():
    episodes = Episode.query.all()

    return jsonify([
        {
            "id": episode.id,
            "person_id": episode.person_id,
            "type": episode.type,
            "status": episode.status,
            "started_at": episode.started_at.isoformat() if episode.started_at else None,
            "closed_at": episode.closed_at.isoformat() if episode.closed_at else None
        }
        for episode in episodes
    ]), 200


# READ BY ID – Obtener episodio por ID
def get_episode_by_id_controller(episode_id):
    episode = Episode.query.get(episode_id)

    if not episode:
        return jsonify({"message": "Episodio no encontrado"}), 404

    return jsonify({
        "id": episode.id,
        "person_id": episode.person_id,
        "type": episode.type,
        "status": episode.status,
        "started_at": episode.started_at.isoformat() if episode.started_at else None,
        "closed_at": episode.closed_at.isoformat() if episode.closed_at else None
    }), 200


# UPDATE – Actualizar datos del episodio (NO cerrar)
def update_episode_controller(episode_id):
    episode = Episode.query.get(episode_id)

    if not episode:
        return jsonify({"message": "Episodio no encontrado"}), 404

    data = request.json

    episode.type = data.get("type", episode.type)

    db.session.commit()

    return jsonify({
        "message": "Episodio actualizado",
        "id": episode.id
    }), 200


# CLOSE – Cerrar episodio
def close_episode_controller(episode_id):
    episode = Episode.query.get(episode_id)

    if not episode:
        return jsonify({"message": "Episodio no encontrado"}), 404

    if episode.status == 'CLOSED':
        return jsonify({"message": "El episodio ya está cerrado"}), 409

    if not check_orders_completed(episode.id):
        return jsonify({"error": "Existen órdenes pendientes"}), 409

    episode.status = 'CLOSED'
    episode.closed_at = datetime.utcnow()

    db.session.commit()

    return jsonify({
        "message": "Episodio cerrado exitosamente"
    }), 200


# DELETE – Eliminar episodio (opcional / administrativo)
def delete_episode_controller(episode_id):
    episode = Episode.query.get(episode_id)

    if not episode:
        return jsonify({"message": "Episodio no encontrado"}), 404

    db.session.delete(episode)
    db.session.commit()

    return jsonify({
        "message": "Episodio eliminado"
    }), 200
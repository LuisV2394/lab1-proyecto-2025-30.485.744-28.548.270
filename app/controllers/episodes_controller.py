from flask import jsonify, request
from app.models.episodes import Episode
from app import db
from datetime import datetime


# Función auxiliar para regla de negocio futura
def check_orders_completed(episode_id):
    # Lógica futura: return Order.query.filter(...).count() == 0
    return True

# CREATE – Abrir episodio
def create_episode_controller():
    data = request.json

    new_episode = Episode(
        person_id=data.get('person_id'),
        type=data.get('type'),            # CONSULTATION, EMERGENCY, etc.
        status='OPEN',                     # Estado inicial
        started_at=datetime.utcnow()
    )

    db.session.add(new_episode)
    db.session.commit()

    return jsonify({
        "message": "Episodio abierto",
        "id": new_episode.id
    }), 201


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
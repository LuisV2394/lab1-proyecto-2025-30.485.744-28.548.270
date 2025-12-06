from flask import jsonify, request
from app.models.episodes import Episode
from app import db
from datetime import datetime

# Función auxiliar para regla de negocio futura
def check_orders_completed(episode_id):
    # Lógica futura: return Order.query.filter(...).count() == 0
    return True


def create_episode_controller():
    data = request.json
    new_episode = Episode(
        person_id=data.get('person_id'),
        type=data.get('type'),               # CONSULTATION, EMERGENCY, etc.
        status='OPEN',                        # Estado inicial
        started_at=datetime.utcnow()          # Fecha de inicio
    )

    db.session.add(new_episode)
    db.session.commit()

    return jsonify({
        "message": "Episodio abierto",
        "id": new_episode.id
    }), 201


def close_episode_controller(id):
    episode = Episode.query.get_or_404(id)

    if not check_orders_completed(episode.id):
        return jsonify({"error": "Existen órdenes pendientes."}), 409

    episode.status = 'CLOSED'
    episode.closed_at = datetime.utcnow()

    db.session.commit()

    return jsonify({"message": "Episodio cerrado exitosamente"})
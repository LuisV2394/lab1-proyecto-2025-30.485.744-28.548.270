from flask import Blueprint, request, jsonify
from app.models.episodes import Episode
from app import db
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from datetime import datetime
import os

episode_bp = Blueprint('episodes', __name__, url_prefix="/episodes")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "episodes")
)

# Función auxiliar para regla de negocio futura
def check_orders_completed(episode_id):
    # Lógica futura: return Order.query.filter(...).count() == 0
    return True 

@episode_bp.route('/', methods=['POST'])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'create.yml'))
def create_episode():
    data = request.json
    new_episode = Episode(
        person_id=data.get('person_id'),
        type=data.get('type'),              # Debe ser CONSULTATION, EMERGENCY, etc.
        status='OPEN',                       # Valor inicial del ENUM
        started_at=datetime.utcnow()         # Fecha de inicio
    )
    db.session.add(new_episode)
    db.session.commit()
    return jsonify({"message": "Episodio abierto", "id": new_episode.id}), 201

@episode_bp.route('/<int:id>/close', methods=['PUT'])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'close.yml'))
def close_episode(id):
    episode = Episode.query.get_or_404(id)
    
    if not check_orders_completed(episode.id):
        return jsonify({"error": "Existen órdenes pendientes."}), 409
    
    episode.status = 'CLOSED'              # Coincide con el ENUM de la tabla
    episode.closed_at = datetime.utcnow()  # Guardar fecha de cierre
    db.session.commit()
    return jsonify({"message": "Episodio cerrado exitosamente"})
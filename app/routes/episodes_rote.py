from flask import Blueprint, request, jsonify
from models.episodes import Episode
from app import db
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from datetime import datetime

episode_bp = Blueprint('episodes', __name__)

# Función auxiliar para regla de negocio futura
def check_orders_completed(episode_id):
    # Lógica futura: return Order.query.filter...count() == 0
    return True 

@episode_bp.route('/episodes', methods=['POST'])
@jwt_required()
@swag_from('../docs/episode_create.yml')
def create_episode():
    data = request.json
    new_episode = Episode(
        person_id=data.get('person_id'),
        reason=data.get('reason'),
        kind=data.get('kind'),
        status='open',
        opening_date=datetime.utcnow()
    )
    db.session.add(new_episode)
    db.session.commit()
    return jsonify({"message": "Episodio abierto", "id": new_episode.id}), 201

@episode_bp.route('/episodes/<int:id>/close', methods=['PUT'])
@jwt_required()
@swag_from('../docs/episode_close.yml')
def close_episode(id):
    episode = Episode.query.get_or_404(id)
    
    if not check_orders_completed(episode.id):
        return jsonify({"error": "Existen órdenes pendientes."}), 409
    
    episode.status = 'close'
    db.session.commit()
    return jsonify({"message": "Episodio cerrado exitosamente"})
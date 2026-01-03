from flask import jsonify, request
from app.models.orders import Order
from app.models.episodes import Episode # Asumiendo que el modelo se llama Episode
from app import db
from datetime import datetime

# Listas de validación
VALID_TYPES = ['laboratory', 'imaging', 'procedure']
VALID_PRIORITIES = ['normal', 'urgent']
VALID_STATUSES = ['issued', 'authorized', 'in_progress', 'completed', 'canceled']

def create_order_controller():
    data = request.get_json()
    
    # 1. Validar campos obligatorios
    required_fields = ['episodeId', 'type', 'details']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Falta el campo requerido: {field}"}), 400

    # 2. Validar existencia del episodio
    episode = Episode.query.get(data['episodeId'])
    if not episode:
        return jsonify({"error": "Episodio no encontrado"}), 404
        
    # 3. Validar que el episodio esté abierto (Regla de negocio lógica)
    if episode.status == 'close':
        return jsonify({"error": "No se pueden crear órdenes para un episodio cerrado"}), 409

    # 4. Validar enumeraciones
    if data['type'] not in VALID_TYPES:
        return jsonify({"error": f"Tipo inválido. Opciones: {VALID_TYPES}"}), 400
        
    priority = data.get('priority', 'normal')
    if priority not in VALID_PRIORITIES:
         return jsonify({"error": f"Prioridad inválida. Opciones: {VALID_PRIORITIES}"}), 400

    # Crear la orden
    new_order = Order(
        episode_id=data['episodeId'],
        type=data['type'],
        details=data['details'], # Espera una lista de objetos [{...}]
        priority=priority,
        status='issued' # Estado inicial por defecto
    )

    db.session.add(new_order)
    db.session.commit()

    return jsonify({
        "message": "Orden médica creada exitosamente",
        "order": new_order.to_dict()
    }), 201

def get_orders_by_episode_controller(episode_id):
    # Verificar si el episodio existe
    episode = Episode.query.get(episode_id)
    if not episode:
         return jsonify({"error": "Episodio no encontrado"}), 404

    orders = Order.query.filter_by(episode_id=episode_id).all()
    return jsonify([order.to_dict() for order in orders]), 200

def update_order_status_controller(order_id):
    data = request.get_json()
    new_status = data.get('status')

    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Orden no encontrada"}), 404

    if new_status not in VALID_STATUSES:
        return jsonify({"error": f"Estado inválido. Opciones: {VALID_STATUSES}"}), 400

    # Aquí podrías agregar lógica de transiciones (ej: no pasar de canceled a issued)
    
    order.status = new_status
    db.session.commit()

    return jsonify({
        "message": "Estado de orden actualizado",
        "order": order.to_dict()
    }), 200
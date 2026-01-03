from flask import jsonify, request
from app.models.orders import Order
from app.models.episodes import Episode 
from app import db
from datetime import datetime

VALID_TYPES = ['laboratory', 'imaging', 'procedure']
VALID_PRIORITIES = ['normal', 'urgent']
VALID_STATUSES = ['issued', 'authorized', 'in_progress', 'completed', 'canceled']

def create_order_controller():
    data = request.get_json()
    
    required_fields = ['episodeId', 'type', 'details']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"missin required fiels: {field}"}), 400

    episode = Episode.query.get(data['episodeId'])
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
        
    if episode.status == 'close':
        return jsonify({"error": "Orders cannot be created for a closed episode"}), 409

    if data['type'] not in VALID_TYPES:
        return jsonify({"error": f"Tipe invaid. Options: {VALID_TYPES}"}), 400
        
    priority = data.get('priority', 'normal')
    if priority not in VALID_PRIORITIES:
         return jsonify({"error": f"invalid priority. options: {VALID_PRIORITIES}"}), 400

    new_order = Order(
        episode_id=data['episodeId'],
        type=data['type'],
        details=data['details'], 
        priority=priority,
        status='issued' 
    )

    db.session.add(new_order)
    db.session.commit()

    return jsonify({
        "message": "medical order created successfully",
        "order": new_order.to_dict()
    }), 201

def get_orders_by_episode_controller(episode_id):
    episode = Episode.query.get(episode_id)
    if not episode:
         return jsonify({"error": "Episode not found"}), 404

    orders = Order.query.filter_by(episode_id=episode_id).all()
    return jsonify([order.to_dict() for order in orders]), 200

def update_order_status_controller(order_id):
    data = request.get_json()
    new_status = data.get('status')

    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    if new_status not in VALID_STATUSES:
        return jsonify({"error": f"invalid estate. Opctions: {VALID_STATUSES}"}), 400

    
    order.status = new_status
    db.session.commit()

    return jsonify({
        "message": "Order status updated successfully",
        "order": order.to_dict()
    }), 200

def delete_order_controller(order_id):
    order = Order.query.get(order_id)
    
    if not order:
        return jsonify({"error: order not found"}), 404

    if order.status not in ['issued', 'authorized']:
        return jsonify({
            "error": f"An order with status cannot be deleted'{order.status}'. "
                     "Try to cancel it instead."
        }), 409

    try:
        db.session.delete(order)
        db.session.commit()
        return jsonify({"message": "order delete sussefuly"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
from flask import jsonify, request
from app.models.order_item import OrderItem
from app.models.orders import Order
from app import db

def create_order_item_controller():
    data = request.get_json()
    
    if not data.get('order_id') or not data.get('prestation_code'):
        return jsonify({"error": "order_id y prestation_code son obligatorios"}), 400

    # Verificar que la orden principal existe
    order = Order.query.get(data['order_id'])
    if not order:
        return jsonify({"error": "La orden principal no existe"}), 404

    new_item = OrderItem(
        order_id=data['order_id'],
        prestation_code=data['prestation_code'],
        instructions=data.get('instructions'),
        status='pending'
    )

    try:
        db.session.add(new_item)
        db.session.commit()
        return jsonify(new_item.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def update_item_status_controller(item_id):
    data = request.get_json()
    item = OrderItem.query.get(item_id)
    
    if not item:
        return jsonify({"error": "Ítem no encontrado"}), 404

    if 'status' in data:
        item.status = data['status']
    if 'result_id' in data:
        item.result_id = data['result_id']

    db.session.commit()
    return jsonify(item.to_dict()), 200

def get_items_by_order_controller(order_id):
    items = OrderItem.query.filter_by(order_id=order_id).all()
    return jsonify([i.to_dict() for i in items]), 200
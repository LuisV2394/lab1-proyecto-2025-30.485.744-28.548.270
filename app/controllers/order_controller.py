from flask import jsonify, request
from datetime import datetime
from app import db
from app.models.orders import Order
from app.models.episodes import Episode
from app.models.professional import Professional

def get_all_orders_controller():
    orders = Order.query.all()
    return jsonify([o.to_dict() for o in orders]), 200

def get_order_by_id_controller(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    return jsonify(order.to_dict()), 200

def create_order_controller():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    required_fields = ["episode_id", "type", "details"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Validate episode
    episode = Episode.query.get(data["episode_id"])
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    # Validate professional if provided
    professional_id = data.get("professional_id")
    if professional_id:
        professional = Professional.query.get(professional_id)
        if not professional:
            return jsonify({"error": "Professional not found"}), 404

    # Validate type
    valid_types = ["LABORATORY", "IMAGING", "PROCEDURE", "MEDICATION", "OTHER"]
    if data["type"] not in valid_types:
        return jsonify({"error": f"Invalid type. Must be one of {valid_types}"}), 400

    # Validate details
    if not isinstance(data["details"], list) or not data["details"]:
        return jsonify({"error": "details must be a non-empty list"}), 400

    # Validate priority
    priority = data.get("priority", "normal")
    if priority not in ["normal", "urgent"]:
        return jsonify({"error": "priority must be 'normal' or 'urgent'"}), 400

    order = Order(
        episode_id=data["episode_id"],
        professional_id=professional_id,
        requires_authorization=data.get("requires_authorization", False),
        type=data["type"],
        details=data["details"],
        priority=priority,
        status="issued"
    )

    db.session.add(order)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error creating order", "details": str(e)}), 500

    return jsonify({"message": "Order created successfully", "order_id": order.id}), 201

def update_order_status_controller(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    data = request.get_json()
    new_status = data.get("status")

    valid_status = ["issued", "authorized", "in_progress", "completed", "canceled"]
    if new_status not in valid_status:
        return jsonify({"error": f"Invalid status. Must be one of {valid_status}"}), 400

    if order.status == "canceled":
        return jsonify({"error": "Canceled orders cannot be modified"}), 400

    order.status = new_status
    db.session.commit()

    return jsonify({"message": "Order status updated successfully", "status": order.status}), 200

def cancel_order_controller(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    order.status = "canceled"
    db.session.commit()

    return jsonify({"message": "Order canceled successfully"}), 200
from flask import request, jsonify
from datetime import datetime
from app import db
from app.models.order_details import OrderDetail
from app.models.orders import Order

# Get All Order Items
def get_all_order_items():
    try:
        order_items = OrderDetail.query.all()
        return jsonify([item.to_dict() for item in order_items]), 200
    except Exception as e:
        return jsonify({
            "error": "Failed to retrieve order items",
            "details": str(e)
        }), 500

# Create Order Item
def create_order_item():
    data = request.get_json() or {}

    order_id = data.get("order_id")
    prestation_code = data.get("prestation_code")

    # Required fields validation
    if not order_id or not prestation_code:
        return jsonify({
            "error": "order_id and prestation_code are required"
        }), 400

    # Validate order exists
    order = Order.query.get(order_id)
    if not order:
        return jsonify({
            "error": "Order not found"
        }), 404

    order_item = OrderDetail(
        order_id=order_id,
        prestation_code=prestation_code,
        instructions=data.get("instructions"),
        status=data.get("status", "pending"),
        result_id=data.get("result_id")
    )

    try:
        db.session.add(order_item)
        db.session.commit()
        return jsonify(order_item.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Failed to create order item",
            "details": str(e)
        }), 500

# Get Order Item by ID
def get_order_item(order_item_id):
    order_item = OrderDetail.query.get(order_item_id)

    if not order_item:
        return jsonify({
            "error": "Order item not found"
        }), 404

    return jsonify(order_item.to_dict()), 200

# Get Order Items by Order
def get_order_items_by_order(order_id):
    order = Order.query.get(order_id)

    if not order:
        return jsonify({
            "error": "Order not found"
        }), 404

    items = OrderDetail.query.filter_by(order_id=order_id).all()
    return jsonify([item.to_dict() for item in items]), 200

# Update Order Item
def update_order_item(order_item_id):
    order_item = OrderDetail.query.get(order_item_id)

    if not order_item:
        return jsonify({
            "error": "Order item not found"
        }), 404

    data = request.get_json() or {}

    allowed_fields = [
        "prestation_code",
        "instructions",
        "status",
        "result_id"
    ]

    for field in allowed_fields:
        if field in data:
            setattr(order_item, field, data[field])

    order_item.updated_at = datetime.utcnow()

    try:
        db.session.commit()
        return jsonify(order_item.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Failed to update order item",
            "details": str(e)
        }), 500

# Delete Order Item
def delete_order_item(order_item_id):
    order_item = OrderDetail.query.get(order_item_id)

    if not order_item:
        return jsonify({
            "error": "Order item not found"
        }), 404

    try:
        db.session.delete(order_item)
        db.session.commit()
        return jsonify({
            "message": "Order item deleted successfully"
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Failed to delete order item",
            "details": str(e)
        }), 500
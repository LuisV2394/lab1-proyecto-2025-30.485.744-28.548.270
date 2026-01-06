from flask import request, jsonify
from datetime import datetime
from app import db
from app.models.order_details import OrderDetail
from app.models.orders import Order

# Get All Order Details
def get_all_order_details_controller():
    try:
        details = OrderDetail.query.all()
        return jsonify([detail.to_dict() for detail in details]), 200
    except Exception as e:
        return jsonify({
            "error": "Failed to retrieve order details",
            "details": str(e)
        }), 500

# Create Order Detail
def create_order_detail_controller():
    data = request.get_json() or {}

    order_id = data.get("order_id")
    code = data.get("code")
    description = data.get("description")

    # Required fields validation
    if not order_id or not code or not description:
        return jsonify({
            "error": "order_id, code, and description are required"
        }), 400

    # Validate order exists
    order = Order.query.get(order_id)
    if not order:
        return jsonify({
            "error": "Order not found"
        }), 404

    detail = OrderDetail(
        order_id=order_id,
        code=code,
        description=description,
        indications=data.get("indications")
    )

    try:
        db.session.add(detail)
        db.session.commit()
        return jsonify(detail.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Failed to create order detail",
            "details": str(e)
        }), 500

# Get Order Detail by ID
def get_order_detail_controller(detail_id):
    detail = OrderDetail.query.get(detail_id)

    if not detail:
        return jsonify({
            "error": "Order detail not found"
        }), 404

    return jsonify(detail.to_dict()), 200

# Get Order Details by Order
def get_order_details_by_order_controller(order_id):
    order = Order.query.get(order_id)

    if not order:
        return jsonify({
            "error": "Order not found"
        }), 404

    details = OrderDetail.query.filter_by(order_id=order_id).all()
    return jsonify([detail.to_dict() for detail in details]), 200

# Update Order Detail
def update_order_detail_controller(detail_id):
    detail = OrderDetail.query.get(detail_id)

    if not detail:
        return jsonify({
            "error": "Order detail not found"
        }), 404

    data = request.get_json() or {}

    allowed_fields = [
        "code",
        "description",
        "indications"
    ]

    for field in allowed_fields:
        if field in data:
            setattr(detail, field, data[field])

    detail.updated_at = datetime.utcnow()

    try:
        db.session.commit()
        return jsonify(detail.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Failed to update order detail",
            "details": str(e)
        }), 500

# Delete Order Detail
def delete_order_detail_controller(detail_id):
    detail = OrderDetail.query.get(detail_id)

    if not detail:
        return jsonify({
            "error": "Order detail not found"
        }), 404

    try:
        db.session.delete(detail)
        db.session.commit()
        return jsonify({
            "message": "Order detail deleted successfully"
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": "Failed to delete order detail",
            "details": str(e)
        }), 500
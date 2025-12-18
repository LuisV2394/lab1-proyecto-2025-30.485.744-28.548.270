from flask import jsonify, request
from app.models.notification import Notification
from app import db
from datetime import datetime


# Obtener todas las notificaciones
def get_all_notifications_controller():
    notifications = Notification.query.all()
    return jsonify([n.to_dict() for n in notifications]), 200


# Obtener notificación por ID
def get_notification_by_id_controller(notification_id):
    notification = Notification.query.get(notification_id)
    if not notification:
        return jsonify({"error": "Notification not found"}), 404

    return jsonify(notification.to_dict()), 200


# Crear notificación nueva
def create_notification_controller():
    data = request.get_json()

    required_fields = ["type", "template", "recipient"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    new_notification = Notification(
        type=data["type"],
        template=data["template"],
        recipient=data["recipient"],
        payload=data.get("payload"),
        status=data.get("status", "PENDING"),
        timestamp=datetime.utcnow()
    )

    db.session.add(new_notification)
    db.session.commit()

    return jsonify({
        "message": "Notification created successfully",
        "notification": new_notification.to_dict()
    }), 201


# Actualizar notificación
def update_notification_controller(notification_id):
    notification = Notification.query.get(notification_id)
    if not notification:
        return jsonify({"error": "Notification not found"}), 404

    data = request.get_json()

    for key, value in data.items():
        if hasattr(notification, key):
            setattr(notification, key, value)

    db.session.commit()

    return jsonify({
        "message": "Notification updated successfully",
        "notification": notification.to_dict()
    }), 200


# Cambiar estado de la notificación
def update_notification_status_controller(notification_id):
    notification = Notification.query.get(notification_id)
    if not notification:
        return jsonify({"error": "Notification not found"}), 404

    data = request.get_json()

    if "status" not in data:
        return jsonify({"error": "Missing status field"}), 400

    notification.status = data["status"]
    notification.timestamp = datetime.utcnow()

    db.session.commit()

    return jsonify({
        "message": "Notification status updated successfully",
        "notification": notification.to_dict()
    }), 200
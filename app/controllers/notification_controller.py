import re
from flask import jsonify, request
from datetime import datetime
from app import db
from app.models.notification import Notification
from app.models.invoice import Invoice
from app.services.email_service import send_email
from app.services.invoice_service import generate_invoice_pdf

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

ALLOWED_TYPES = {"EMAIL", "SMS", "WHATSAPP"}
ALLOWED_STATUS = {"PENDING", "SENT", "FAILED", "RETRYING"}


def is_valid_email(email: str) -> bool:
    return re.match(EMAIL_REGEX, email) is not None

def send_notification(notification):
    if notification.type.upper() != "EMAIL":
        return

    payload = notification.payload or {}
    attachment_path = None

    invoice_id = payload.get("invoice_id")
    if invoice_id:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            notification.status = "FAILED"
            db.session.commit()
            return

        attachment_path = generate_invoice_pdf(invoice)

    result = send_email(
        recipient=notification.recipient,
        subject=notification.template,
        html_content=payload.get("message", ""),
        attachment_path=attachment_path
    )

    notification.status = "FAILED" if result.get("error") else "SENT"
    notification.timestamp = datetime.utcnow()
    db.session.commit()

def get_all_notifications_controller():
    notifications = Notification.query.all()
    return jsonify([n.to_dict() for n in notifications]), 200

def get_notification_by_id_controller(notification_id):
    notification = Notification.query.get(notification_id)
    if not notification:
        return jsonify({"error": "Notification not found"}), 404

    return jsonify(notification.to_dict()), 200

def create_notification_controller():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    required_fields = ["type", "template", "recipient"]

    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Validar tipo
    if data["type"].upper() not in ALLOWED_TYPES:
        return jsonify({
            "error": f"Invalid notification type. Allowed: {list(ALLOWED_TYPES)}"
        }), 400

    # Validar correo
    if not is_valid_email(data["recipient"]):
        return jsonify({
            "error": "Invalid email format"
        }), 400

    # Validar payload
    payload = data.get("payload")
    if payload is not None and not isinstance(payload, dict):
        return jsonify({
            "error": "Payload must be a JSON object"
        }), 400

    # Validar invoice_id si existe
    if payload and payload.get("invoice_id"):
        invoice = Invoice.query.get(payload["invoice_id"])
        if not invoice:
            return jsonify({
                "error": "Invoice not found"
            }), 404

    new_notification = Notification(
        type=data["type"].upper(),
        template=data["template"],
        recipient=data["recipient"],
        payload=payload,
        status="PENDING",
        timestamp=datetime.utcnow()
    )

    db.session.add(new_notification)
    db.session.commit()

    send_notification(new_notification)

    return jsonify({
        "message": "Notification created successfully",
        "notification": new_notification.to_dict()
    }), 201

def update_notification_controller(notification_id):
    notification = Notification.query.get(notification_id)
    if not notification:
        return jsonify({"error": "Notification not found"}), 404

    data = request.get_json()

    if "recipient" in data:
        if not is_valid_email(data["recipient"]):
            return jsonify({"error": "Invalid email format"}), 400

    if "type" in data:
        if data["type"].upper() not in ALLOWED_TYPES:
            return jsonify({
                "error": f"Invalid notification type. Allowed: {list(ALLOWED_TYPES)}"
            }), 400
        notification.type = data["type"].upper()

    if "status" in data:
        if data["status"].upper() not in ALLOWED_STATUS:
            return jsonify({
                "error": f"Invalid status. Allowed: {list(ALLOWED_STATUS)}"
            }), 400
        notification.status = data["status"].upper()

    if "payload" in data:
        if not isinstance(data["payload"], dict):
            return jsonify({"error": "Payload must be a JSON object"}), 400
        notification.payload = data["payload"]

    if "template" in data:
        notification.template = data["template"]

    notification.updated_at = datetime.utcnow()
    db.session.commit()

    return jsonify({
        "message": "Notification updated successfully",
        "notification": notification.to_dict()
    }), 200

def update_notification_status_controller(notification_id):
    notification = Notification.query.get(notification_id)
    if not notification:
        return jsonify({"error": "Notification not found"}), 404

    data = request.get_json()

    status = data.get("status")
    if not status:
        return jsonify({"error": "Missing status field"}), 400

    if status.upper() not in ALLOWED_STATUS:
        return jsonify({
            "error": f"Invalid status. Allowed: {list(ALLOWED_STATUS)}"
        }), 400

    notification.status = status.upper()
    notification.timestamp = datetime.utcnow()
    db.session.commit()

    return jsonify({
        "message": "Notification status updated successfully",
        "notification": notification.to_dict()
    }), 200
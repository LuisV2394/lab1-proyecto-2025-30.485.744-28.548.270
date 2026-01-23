from flask import jsonify, request
from app.models.access_logs import AccessLog
from app import db
from app.models.user import User
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

# GET ALL LOGS (pagination)
def get_all_logs_controller():
    try:
        limit = int(request.args.get("limit", 100))
        page = int(request.args.get("page", 1))

        if limit > 500:
            limit = 500

        logs_query = AccessLog.query.order_by(AccessLog.date.desc())

        logs = logs_query.paginate(page=page, per_page=limit, error_out=False)

        return jsonify({
            "message": "Logs retrieved successfully",
            "total": logs.total,
            "page": page,
            "logs": [log.to_dict() for log in logs.items]
        }), 200

    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

# GET LOG BY ID
def get_log_by_id_controller(log_id):
    log = AccessLog.query.get(log_id)

    if not log:
        return jsonify({"error": "Access log not found"}), 404

    return jsonify({
        "message": "Log retrieved successfully",
        "log": log.to_dict()
    }), 200

# GET LOGS BY USER
def get_logs_by_user_controller(user_id):
    logs = AccessLog.query.filter_by(user_id=user_id) \
                          .order_by(AccessLog.date.desc()) \
                          .all()

    return jsonify({
        "message": "Logs retrieved successfully",
        "logs": [log.to_dict() for log in logs]
    }), 200

# CREATE LOG ENTRY
def create_log_controller():
    data = request.get_json() or {}

    required_fields = ["resource", "action"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    if len(data.get("resource", "")) > 100:
        return jsonify({"error": "Resource exceeds maximum length (100)"}), 400

    if len(data.get("action", "")) > 100:
        return jsonify({"error": "Action exceeds maximum length (100)"}), 400

    if data.get("details") and len(data["details"]) > 5000:
        return jsonify({"error": "Details exceeds maximum length (5000)"}), 400

    user_id = data.get("user_id")
    if user_id is not None:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": f"user_id {user_id} does not exist"}), 400

    date_value = data.get("date")
    if date_value:
        try:
            date_value = datetime.fromisoformat(date_value)
        except ValueError:
            return jsonify({"error": "Invalid date format. Use ISO 8601"}), 400
    else:
        date_value = datetime.utcnow()

    try:
        new_log = AccessLog(
            user_id=user_id,   # ya validado o None
            resource=data["resource"],
            action=data["action"],
            details=data.get("details"),
            ip_address=request.remote_addr or request.environ.get("HTTP_X_REAL_IP"),
            user_agent=getattr(request.user_agent, "string", None),
            date=date_value
        )

        db.session.add(new_log)
        db.session.commit()

        return jsonify({
            "message": "Access log created successfully",
            "log": new_log.to_dict()
        }), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": f"Database error: {str(e)}"}), 500

# INTERNAL UTILITY
def create_log_entry(user_id, resource, action, details=None):
    try:
        safe_user_id = None

        if user_id is not None:
            user = User.query.get(user_id)
            if user:
                safe_user_id = user.id
            else:
                print(f"[WARN] Invalid user_id {user_id} for access log. Using NULL.")

        log = AccessLog(
            user_id=safe_user_id, 
            resource=resource,
            action=action,
            details=details,
            ip_address=request.remote_addr,
            user_agent=getattr(request.user_agent, "string", None),
            date=datetime.utcnow()
        )

        db.session.add(log)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        print(f"Error saving access log: {e}")

# UPDATE LOG ENTRY
def update_log_controller(log_id):
    log = AccessLog.query.get(log_id)

    if not log:
        return jsonify({"error": "Access log not found"}), 404

    data = request.get_json() or {}

    # Allowed to update only descriptive data
    allowed_fields = ["resource", "action", "details"]

    for key, value in data.items():
        if key not in allowed_fields:
            return jsonify({"error": f"Field '{key}' cannot be updated"}), 400

        if key == "details" and value and len(value) > 5000:
            return jsonify({"error": "Details exceeds maximum length (5000)"}), 400

        setattr(log, key, value)

    db.session.commit()

    return jsonify({
        "message": "Access log updated successfully",
        "log": log.to_dict()
    }), 200

# DELETE LOG ENTRY
def delete_log_controller(log_id):
    log = AccessLog.query.get(log_id)

    if not log:
        return jsonify({"error": "Access log not found"}), 404

    db.session.delete(log)
    db.session.commit()

    return jsonify({"message": "Access log deleted successfully"}), 200
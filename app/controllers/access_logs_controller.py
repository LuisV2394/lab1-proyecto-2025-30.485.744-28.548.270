from flask import jsonify, request
from app.models.access_logs import AccessLog
from app import db
from sqlalchemy.exc import SQLAlchemyError

# GET ALL LOGS (with optional pagination)
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
    logs = AccessLog.query.filter_by(user_id=user_id)\
                          .order_by(AccessLog.date.desc())\
                          .all()

    if not logs:
        return jsonify({"message": "No logs found for this user", "logs": []}), 200

    return jsonify({
        "message": "Logs retrieved successfully",
        "logs": [log.to_dict() for log in logs]
    }), 200

# CREATE LOG ENTRY (API endpoint)-
def create_log_controller():
    data = request.get_json() or {}

    required_fields = ["user_id", "resource", "action"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Basic validations
    if len(data.get("resource", "")) > 255:
        return jsonify({"error": "Resource exceeds maximum length (255)"}), 400

    if len(data.get("action", "")) > 100:
        return jsonify({"error": "Action exceeds maximum length (100)"}), 400

    details = data.get("details")
    if details and len(details) > 5000:
        return jsonify({"error": "Details exceeds maximum length (5000)"}), 400

    try:
        new_log = AccessLog(
            user_id=data["user_id"],
            resource=data["resource"],
            action=data["action"],
            details=details,
            ip_address=request.remote_addr,
            user_agent=request.user_agent.string
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

# INTERNAL UTILITY FUNCTION (unchanged but improved)
def create_log_entry(user_id, resource, action, details=None):
    try:
        log = AccessLog(
            user_id=user_id,
            resource=resource,
            action=action,
            details=details,
            ip_address=request.remote_addr,
            user_agent=request.user_agent.string
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

# DELETE LOG
def delete_log_controller(log_id):
    log = AccessLog.query.get(log_id)

    if not log:
        return jsonify({"error": "Access log not found"}), 404

    db.session.delete(log)
    db.session.commit()

    return jsonify({"message": "Access log deleted successfully"}), 200
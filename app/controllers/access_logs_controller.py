from flask import jsonify, request
from app.models.access_logs import AccessLog
from app import db

def get_all_logs_controller():
    # Usually the logs would be paginated 
    logs = AccessLog.query.order_by(AccessLog.date.desc()).limit(100).all()
    return jsonify([log.to_dict() for log in logs]), 200

def create_log_entry(user_id, resource, action, details):
    """ Utility function to be called internally by other modules"""
    try:
        new_log = AccessLog(
            user_id=user_id,
            resource=resource,
            action=action,
            details=details,
            ip_address=request.remote_addr,
            user_agent=request.user_agent.string
        )
        db.session.add(new_log)
        db.session.commit()
    except Exception as e:
        print(f"Error saving access log: {e}")
        db.session.rollback()

def get_logs_by_user_controller(user_id):
    logs = AccessLog.query.filter_by(user_id=user_id).order_by(AccessLog.date.desc()).all()
    return jsonify([log.to_dict() for log in logs]), 200
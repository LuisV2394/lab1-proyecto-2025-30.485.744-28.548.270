from flask import jsonify, request
from app import db
from app.models.authorization import Authorization, AuthorizationStatus
from app.models.orders import Order
from app.models.coverage_plans import CoveragePlan
from datetime import datetime

VALID_STATUSES = {status.value for status in AuthorizationStatus}

# GET all authorizations
def get_all_authorizations_controller():
    authorizations = Authorization.query.all()
    data = [a.to_dict() for a in authorizations]
    return jsonify(data), 200

# GET authorization by ID
def get_authorization_by_id_controller(auth_id):
    auth = Authorization.query.get(auth_id)
    if not auth:
        return jsonify({"error": "Authorization not found"}), 404

    return jsonify({
        "message": "Authorization retrieved successfully",
        "authorization": auth.to_dict()
    }), 200

# CREATE new authorization
def create_authorization_controller():
    data = request.get_json() or {}

    order_id = data.get("order_id")
    procedure_code = data.get("procedure_code")
    if not order_id and not procedure_code:
        return jsonify({"error": "Either order_id or procedure_code must be provided"}), 400

    if order_id and not Order.query.get(order_id):
        return jsonify({"error": "Order not found"}), 404

    plan_id = data.get("plan_id")
    if not plan_id:
        return jsonify({"error": "plan_id is required"}), 400
    if not CoveragePlan.query.get(plan_id):
        return jsonify({"error": "Coverage plan not found"}), 404

    if procedure_code and Authorization.query.filter_by(procedure_code=procedure_code).first():
        return jsonify({"error": "procedure_code already exists"}), 400

    # Optional fields
    authorization_number = data.get("authorization_number")
    response_date = data.get("response_date")
    observations = data.get("observations")

    # Validate authorization_number uniqueness
    if authorization_number and Authorization.query.filter_by(authorization_number=authorization_number).first():
        return jsonify({"error": "authorization_number already exists"}), 400

    status = data.get("status", AuthorizationStatus.REQUESTED.value)
    if status not in VALID_STATUSES:
        return jsonify({"error": f"Invalid status. Must be one of {list(VALID_STATUSES)}"}), 400

    if response_date:
        try:
            response_date = datetime.fromisoformat(response_date)
        except ValueError:
            return jsonify({"error": "Invalid response_date format. Must be ISO format"}), 400

    new_auth = Authorization(
        order_id=order_id,
        procedure_code=procedure_code,
        plan_id=plan_id,
        status=status,
        response_date=response_date,
        authorization_number=authorization_number,
        observations=observations
    )

    db.session.add(new_auth)
    db.session.commit()

    return jsonify({
        "message": "Authorization created successfully",
        "authorization": new_auth.to_dict()
    }), 201

# UPDATE authorization
def update_authorization_controller(auth_id):
    auth = Authorization.query.get(auth_id)
    if not auth:
        return jsonify({"error": "Authorization not found"}), 404

    data = request.get_json() or {}

    # Allow update of order_id, procedure_code, plan_id, status, response_date, authorization_number, observations
    for key, value in data.items():
        if hasattr(auth, key):

            if key == "order_id" and value:
                if not Order.query.get(value):
                    return jsonify({"error": "Order not found"}), 404

            if key == "plan_id" and value:
                if not CoveragePlan.query.get(value):
                    return jsonify({"error": "Coverage plan not found"}), 404

            if key == "status" and value:
                if value not in VALID_STATUSES:
                    return jsonify({"error": f"Invalid status. Must be one of {list(VALID_STATUSES)}"}), 400

            if key == "response_date" and value:
                try:
                    value = datetime.fromisoformat(value)
                except ValueError:
                    return jsonify({"error": "Invalid response_date format. Must be ISO format"}), 400

            setattr(auth, key, value)

    db.session.commit()

    return jsonify({
        "message": "Authorization updated successfully",
        "authorization": auth.to_dict()
    }), 200

# DELETE (soft delete can be added if needed)
def delete_authorization_controller(auth_id):
    auth = Authorization.query.get(auth_id)
    if not auth:
        return jsonify({"error": "Authorization not found"}), 404

    db.session.delete(auth)
    db.session.commit()

    return jsonify({"message": "Authorization deleted successfully"}), 200
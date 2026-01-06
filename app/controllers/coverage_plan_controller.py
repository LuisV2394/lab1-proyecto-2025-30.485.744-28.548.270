from flask import jsonify, request
from app.models.coverage_plans import CoveragePlan
from app.models.insurer import Insurer
from app import db

# Obtener todos los planes de cobertura
def get_all_coverage_plans_controller():
    plans = CoveragePlan.query.all()
    data = [p.to_dict() for p in plans]
    return jsonify(data), 200

# Obtener plan por ID
def get_coverage_plan_by_id_controller(plan_id):
    plan = CoveragePlan.query.get(plan_id)
    if not plan:
        return jsonify({"error": "Coverage plan not found"}), 404

    return jsonify({
        "message": "Coverage plan retrieved successfully",
        "plan": plan.to_dict()
    }), 200

# Crear un nuevo plan
def create_coverage_plan_controller():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    required_fields = ["insurer_id", "name"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Validar que la aseguradora exista
    insurer = Insurer.query.get(data["insurer_id"])
    if not insurer:
        return jsonify({"error": "Insurer not found"}), 404

    # Validar nombre no vacío y longitud
    name = data["name"].strip()
    if not name or len(name) > 100:
        return jsonify({"error": "Invalid name"}), 400

    new_plan = CoveragePlan(
        insurer_id=data["insurer_id"],
        name=name,
        general_conditions=data.get("general_conditions")
    )

    db.session.add(new_plan)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error creating coverage plan", "details": str(e)}), 500

    return jsonify({
        "message": "Coverage plan created successfully",
        "plan": new_plan.to_dict()
    }), 201

# Actualizar un plan existente
def update_coverage_plan_controller(plan_id):
    plan = CoveragePlan.query.get(plan_id)
    if not plan:
        return jsonify({"error": "Coverage plan not found"}), 404

    data = request.get_json()

    # Validar e intentar actualizar aseguradora si se proporciona
    if "insurer_id" in data and data["insurer_id"] is not None:
        insurer = Insurer.query.get(data["insurer_id"])
        if not insurer:
            return jsonify({"error": "Insurer not found"}), 404
        plan.insurer_id = data["insurer_id"]

    # Validar nombre si se proporciona
    if "name" in data and data["name"]:
        name = data["name"].strip()
        if not name or len(name) > 100:
            return jsonify({"error": "Invalid name"}), 400
        plan.name = name

    # Actualizar condiciones generales
    if "general_conditions" in data:
        plan.general_conditions = data["general_conditions"]

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error updating coverage plan", "details": str(e)}), 500

    return jsonify({
        "message": "Coverage plan updated successfully",
        "plan": plan.to_dict()
    }), 200

# Eliminar un plan (soft delete opcional o real delete)
def delete_coverage_plan_controller(plan_id):
    plan = CoveragePlan.query.get(plan_id)
    if not plan:
        return jsonify({"error": "Coverage plan not found"}), 404

    db.session.delete(plan)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error deleting coverage plan", "details": str(e)}), 500

    return jsonify({"message": "Coverage plan deleted successfully"}), 200
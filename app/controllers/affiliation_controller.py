from flask import jsonify, request
from app.models.afiliation import Affiliation
from app.models.person import Person
from app.models.coverage_plans import CoveragePlan
from app.models.payer import Payer
from app import db
from datetime import datetime

# GET: Obtener todas las afiliaciones
def get_all_affiliations_controller():
    affiliations = Affiliation.query.all()
    data = [a.to_dict() for a in affiliations]
    return jsonify(data), 200

# GET: Obtener afiliación por ID
def get_affiliation_by_id_controller(affiliation_id):
    affiliation = Affiliation.query.get(affiliation_id)
    if not affiliation:
        return jsonify({"error": "Affiliation not found"}), 404

    return jsonify({
        "message": "Affiliation retrieved successfully",
        "affiliation": affiliation.to_dict()
    }), 200

# POST: Crear nueva afiliación
def create_affiliation_controller():
    data = request.get_json()

    # Campos requeridos
    required_fields = ["person_id", "plan_id", "card_number", "valid_from"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Validar existencia de persona
    person = Person.query.get(data["person_id"])
    if not person:
        return jsonify({"error": "Person not found"}), 404

    # Validar existencia de plan
    plan = CoveragePlan.query.get(data["plan_id"])
    if not plan:
        return jsonify({"error": "Coverage plan not found"}), 404

    # Validar payer si se proporcionó
    payer_id = data.get("payer_id")
    if payer_id:
        payer = Payer.query.get(payer_id)
        if not payer:
            return jsonify({"error": "Payer not found"}), 404
        
    # Validar coinsurance no sean negativo
    if data.get("coinsurance", 0) < 0:
        return jsonify({"error": "coinsurance cannot be negative"}), 400
    
    # Validar que copayment no sea negativo
    if data.get("copayment", 0) < 0:
        return jsonify({"error": "copayment cannot be negative"}), 400

    # Validar fechas
    try:
        valid_from = datetime.strptime(data["valid_from"], "%Y-%m-%d").date()
        valid_to = datetime.strptime(data["valid_to"], "%Y-%m-%d").date() if data.get("valid_to") else None
        if valid_to and valid_to < valid_from:
            return jsonify({"error": "valid_to cannot be earlier than valid_from"}), 400
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    # Validar duplicados por persona y plan
    existing_affiliation = Affiliation.query.filter_by(
        person_id=data["person_id"],
        plan_id=data["plan_id"],
        card_number=data["card_number"]
    ).first()
    if existing_affiliation:
        return jsonify({"error": "This affiliation already exists"}), 400

    # Crear afiliación
    new_affiliation = Affiliation(
        person_id=data["person_id"],
        plan_id=data["plan_id"],
        payer_id=payer_id,
        card_number=data["card_number"],
        policy_number=data.get("policy_number"),
        valid_from=valid_from,
        valid_to=valid_to,
        copayment=data.get("copayment", 0.0),
        coinsurance=data.get("coinsurance", 0.0),
        status=data.get("status", True)
    )

    db.session.add(new_affiliation)
    db.session.commit()

    return jsonify({
        "message": "Affiliation created successfully",
        "affiliation": new_affiliation.to_dict()
    }), 201

# PUT: Actualizar afiliación existente
def update_affiliation_controller(affiliation_id):
    affiliation = Affiliation.query.get(affiliation_id)
    if not affiliation:
        return jsonify({"error": "Affiliation not found"}), 404

    data = request.get_json()

    # Validaciones para IDs relacionados
    if "person_id" in data:
        person = Person.query.get(data["person_id"])
        if not person:
            return jsonify({"error": "Person not found"}), 404

    if "plan_id" in data:
        plan = CoveragePlan.query.get(data["plan_id"])
        if not plan:
            return jsonify({"error": "Coverage plan not found"}), 404

    if "payer_id" in data and data["payer_id"]:
        payer = Payer.query.get(data["payer_id"])
        if not payer:
            return jsonify({"error": "Payer not found"}), 404

        # Validar coinsurance no sean negativo
    if data.get("coinsurance", 0) < 0:
        return jsonify({"error": "coinsurance cannot be negative"}), 400
    
    # Validar que copayment no sea negativo
    if data.get("copayment", 0) < 0:
        return jsonify({"error": "copayment cannot be negative"}), 400
    
    # Validar fechas si se proporcionan
    if "valid_from" in data or "valid_to" in data:
        try:
            valid_from = datetime.strptime(data.get("valid_from", affiliation.valid_from.strftime("%Y-%m-%d")), "%Y-%m-%d").date()
            valid_to = datetime.strptime(data.get("valid_to", affiliation.valid_to.strftime("%Y-%m-%d") if affiliation.valid_to else None), "%Y-%m-%d").date() if data.get("valid_to") else None
            if valid_to and valid_to < valid_from:
                return jsonify({"error": "valid_to cannot be earlier than valid_from"}), 400
            data["valid_from"] = valid_from
            data["valid_to"] = valid_to
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    # Actualizar campos
    for key, value in data.items():
        if hasattr(affiliation, key):
            setattr(affiliation, key, value)

    db.session.commit()

    return jsonify({
        "message": "Affiliation updated successfully",
        "affiliation": affiliation.to_dict()
    }), 200

# PATCH: Desactivar afiliación
def deactivate_affiliation_controller(affiliation_id):
    affiliation = Affiliation.query.get(affiliation_id)
    if not affiliation:
        return jsonify({"error": "Affiliation not found"}), 404

    affiliation.status = False
    db.session.commit()

    return jsonify({"message": "Affiliation deactivated successfully"}), 200
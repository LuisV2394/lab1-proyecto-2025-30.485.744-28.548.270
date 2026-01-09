from flask import jsonify, request
from app.models.tariff import Tariff
from app.models.prestation import Prestation
from app.models.coverage_plans import CoveragePlan
from app import db
from datetime import datetime


def get_all_tariffs_controller():
    try:
        tariffs = Tariff.query.order_by(Tariff.valid_from.desc()).all()
        return jsonify({
            "count": len(tariffs),
            "tariffs": [t.to_dict() for t in tariffs]
        }), 200
    except Exception as e:
        return jsonify({"error": "Error retrieving tariffs", "details": str(e)}), 500

# CREATE TARIFF
def create_tariff_controller():
    data = request.get_json() or {}

    # Validar campos requeridos
    required_fields = ["service_code", "plan_id", "price", "validFrom"]
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    # Validar existencia de Service y CoveragePlan
    service = Prestation.query.filter_by(code=data.get('service_code')).first()
    plan = CoveragePlan.query.get(data.get('plan_id'))

    if not service:
        return jsonify({"error": "Service not found"}), 404
    if not plan:
        return jsonify({"error": "Coverage plan not found"}), 404

    # Validar fechas
    try:
        valid_from = datetime.strptime(data.get('validFrom'), '%Y-%m-%d').date()
        valid_until = datetime.strptime(data.get('validUntil'), '%Y-%m-%d').date() if data.get('validUntil') else None
    except ValueError:
        return jsonify({"error": "Invalid date format, should be YYYY-MM-DD"}), 400

    # Crear tarifa
    try:
        new_tariff = Tariff(
            service_code=data.get('service_code'),
            plan_id=data.get('plan_id'),
            base_value=data.get('price'),
            taxes=data.get('taxes', 0.0),
            valid_from=valid_from,
            valid_until=valid_until
        )
        db.session.add(new_tariff)
        db.session.commit()

        return jsonify({
            "message": "Tariff created successfully",
            "tariff": new_tariff.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error creating tariff", "details": str(e)}), 500

# GET TARIFF BY ID
def get_tariff_by_id_controller(tariff_id):
    tariff = Tariff.query.get(tariff_id)
    if not tariff:
        return jsonify({"error": "Tariff not found"}), 404

    return jsonify({
        "message": "Tariff retrieved successfully",
        "tariff": tariff.to_dict()
    }), 200

# UPDATE TARIFF
def update_tariff_controller(tariff_id):
    tariff = Tariff.query.get(tariff_id)
    if not tariff:
        return jsonify({"error": "Tariff not found"}), 404

    data = request.get_json() or {}

    try:
        if 'price' in data:
            tariff.base_value = data['price']
        if 'taxes' in data:
            tariff.taxes = data['taxes']
        if 'validUntil' in data:
            tariff.valid_until = datetime.strptime(data['validUntil'], '%Y-%m-%d').date()

        db.session.commit()
        return jsonify({
            "message": "Tariff updated successfully",
            "tariff": tariff.to_dict()
        }), 200

    except ValueError:
        return jsonify({"error": "Invalid date format, should be YYYY-MM-DD"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error updating tariff", "details": str(e)}), 500

# DELETE TARIFF
def delete_tariff_controller(tariff_id):
    tariff = Tariff.query.get(tariff_id)
    if not tariff:
        return jsonify({"error": "Tariff not found"}), 404

    try:
        db.session.delete(tariff)
        db.session.commit()
        return jsonify({"message": "Tariff deleted successfully"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error deleting tariff", "details": str(e)}), 500
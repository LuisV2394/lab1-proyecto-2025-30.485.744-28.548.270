from flask import jsonify, request
from app.models.tariff import Tariff
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


def create_tariff_controller():
    data = request.get_json() or {}

    required_fields = ["prestation_code", "plan_id", "price", "validFrom"]
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    # Validar existencia de CoveragePlan si plan_id no es null
    plan_id = data.get('plan_id')
    if plan_id:
        plan = CoveragePlan.query.get(plan_id)
        if not plan:
            return jsonify({"error": "Coverage plan not found"}), 404

    # Validar precios positivos
    try:
        price = float(data.get('price'))
        taxes = float(data.get('taxes', 0.0))
        if price < 0 or taxes < 0:
            return jsonify({"error": "Price and taxes must be positive numbers"}), 400
    except ValueError:
        return jsonify({"error": "Price and taxes must be numeric"}), 400

    # Validar fechas
    try:
        valid_from = datetime.strptime(data.get('validFrom'), '%Y-%m-%d').date()
        valid_until = datetime.strptime(data.get('validUntil'), '%Y-%m-%d').date() if data.get('validUntil') else None
    except ValueError:
        return jsonify({"error": "Invalid date format, should be YYYY-MM-DD"}), 400

    # Validar unicidad: no puede existir otra tarifa con mismo code + plan + fecha inicio
    existing = Tariff.query.filter_by(
        prestation_code=data.get('prestation_code'),
        plan_id=plan_id,
        valid_from=valid_from
    ).first()
    if existing:
        return jsonify({"error": "A tariff with this code, plan and valid_from already exists"}), 400

    # Crear tarifa
    try:
        new_tariff = Tariff(
            prestation_code=data.get('prestation_code'),
            plan_id=plan_id,
            price=price,
            taxes=taxes,
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

def get_tariff_by_id_controller(tariff_id):
    tariff = Tariff.query.get(tariff_id)
    if not tariff:
        return jsonify({"error": "Tariff not found"}), 404

    return jsonify({
        "message": "Tariff retrieved successfully",
        "tariff": tariff.to_dict()
    }), 200

def update_tariff_controller(tariff_id):
    tariff = Tariff.query.get(tariff_id)
    if not tariff:
        return jsonify({"error": "Tariff not found"}), 404

    data = request.get_json() or {}

    try:
        if 'price' in data:
            price = float(data['price'])
            if price < 0:
                return jsonify({"error": "Price must be positive"}), 400
            tariff.price = price

        if 'taxes' in data:
            taxes = float(data['taxes'])
            if taxes < 0:
                return jsonify({"error": "Taxes must be positive"}), 400
            tariff.taxes = taxes

        if 'validUntil' in data:
            tariff.valid_until = datetime.strptime(data['validUntil'], '%Y-%m-%d').date()

        # Opcional: validar unicidad si cambió code o plan o valid_from
        if 'prestation_code' in data or 'plan_id' in data or 'validFrom' in data:
            prestation_code = data.get('prestation_code', tariff.prestation_code)
            plan_id = data.get('plan_id', tariff.plan_id)
            valid_from = datetime.strptime(data.get('validFrom'), '%Y-%m-%d').date() if data.get('validFrom') else tariff.valid_from

            existing = Tariff.query.filter(
                Tariff.id != tariff.id,
                Tariff.prestation_code == prestation_code,
                Tariff.plan_id == plan_id,
                Tariff.valid_from == valid_from
            ).first()
            if existing:
                return jsonify({"error": "Another tariff with this code, plan and valid_from already exists"}), 400

            tariff.prestation_code = prestation_code
            tariff.plan_id = plan_id
            tariff.valid_from = valid_from

        db.session.commit()
        return jsonify({
            "message": "Tariff updated successfully",
            "tariff": tariff.to_dict()
        }), 200

    except ValueError:
        return jsonify({"error": "Invalid data format"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error updating tariff", "details": str(e)}), 500

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
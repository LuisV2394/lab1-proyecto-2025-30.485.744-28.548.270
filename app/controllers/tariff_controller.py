from flask import jsonify, request
from app.models.tariff import Tariff
from app.models.services import Service
from app.models.coverage_plans import CoveragePlan
from app import db
from datetime import datetime

def create_tariff_controller():
    data = request.get_json()
    
    # Validate existance of related service and plan
    service = Service.query.filter_by(code=data.get('service_code')).first()
    plan = CoveragePlan.query.get(data.get('plan_id'))
    
    if not service or not plan:
        return jsonify({"error": "service or coverage_plans not found"}), 404

    try:
        new_tariff = Tariff(
            service_code=data.get('service_code'),
            plan_id=data.get('plan_id'),
            base_value=data.get('price'),
            taxes=data.get('taxes', 0.0),
            valid_from=datetime.strptime(data.get('validFrom'), '%Y-%m-%d').date(),
            valid_until=datetime.strptime(data.get('validUntil'), '%Y-%m-%d').date() if data.get('validUntil') else None
        )
        db.session.add(new_tariff)
        db.session.commit()
        return jsonify(new_tariff.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

def get_tariff_by_id_controller(tariff_id):
    tariff = Tariff.query.get(tariff_id)
    if not tariff:
        return jsonify({"error": "Tariff not found"}), 404
    return jsonify(tariff.to_dict()), 200

def update_tariff_controller(tariff_id):
    tariff = Tariff.query.get(tariff_id)
    if not tariff:
        return jsonify({"error": "Tariff not found"}), 404
    
    data = request.get_json()
    if 'price' in data: tariff.base_value = data['price']
    if 'taxes' in data: tariff.taxes = data['taxes']
    if 'validUntil' in data: 
        tariff.valid_until = datetime.strptime(data['validUntil'], '%Y-%m-%d').date()

    db.session.commit()
    return jsonify(tariff.to_dict()), 200

def delete_tariff_controller(tariff_id):
    tariff = Tariff.query.get(tariff_id)
    if not tariff:
        return jsonify({"error": "Tariff not found"}), 404
    
    db.session.delete(tariff)
    db.session.commit()
    return jsonify({"message": "Tariff delete susefully"}), 200
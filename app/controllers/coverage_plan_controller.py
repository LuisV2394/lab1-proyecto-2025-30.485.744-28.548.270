from flask import jsonify, request
from app.models.coverage_plans import CoveragePlan
from app.models.insurance_company import InsuranceCompany
from app import db

def create_coverage_plan_controller():
    data = request.get_json()
    
    # Validar campos obligatorios
    if not data.get('insurer_company_id') or not data.get('name'):
        return jsonify({"error": "insurer_company_id y name son obligatorios"}), 400

    # Validar que la aseguradora existe
    insurer = InsuranceCompany.query.get(data.get('insurer_company_id'))
    if not insurer:
        return jsonify({"error": "La aseguradora especificada no existe"}), 404

    new_plan = CoveragePlan(
        insurer_company_id=data.get('insurer_company_id'),
        name=data.get('name'),
        general_conditions=data.get('generalConditions'), # Adaptado del prompt
        active=data.get('active', True)
    )

    try:
        db.session.add(new_plan)
        db.session.commit()
        return jsonify(new_plan.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def get_plans_by_insurer_controller(insurer_id):
    plans = CoveragePlan.query.filter_by(insurer_company_id=insurer_id).all()
    return jsonify([p.to_dict() for p in plans]), 200

def update_coverage_plan_controller(plan_id):
    plan = CoveragePlan.query.get(plan_id)
    if not plan:
        return jsonify({"error": "Plan de cobertura no encontrado"}), 404

    data = request.get_json()
    
    # Actualización de campos
    if 'name' in data: plan.name = data['name']
    if 'generalConditions' in data: plan.general_conditions = data['generalConditions']
    if 'active' in data: plan.active = data['active']

    db.session.commit()
    return jsonify(plan.to_dict()), 200

def delete_coverage_plan_controller(plan_id):
    plan = CoveragePlan.query.get(plan_id)
    if not plan:
        return jsonify({"error": "Plan no encontrado"}), 404

    try:
        db.session.delete(plan)
        db.session.commit()
        return jsonify({"message": "Plan eliminado exitosamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "No se pudo eliminar el plan"}), 400
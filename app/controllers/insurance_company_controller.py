from flask import jsonify, request
from app.models.insurance_company import InsuranceCompany
from app import db

def get_all_insurances_controller():
    insurances = InsuranceCompany.query.all()
    return jsonify([i.to_dict() for i in insurances]), 200

def create_insurance_controller():
    data = request.get_json()
    
    # Validate obligatory field
    if not data.get('name') or not data.get('tax_nit'):
        return jsonify({"error": "name and nit are obligatory"}), 400

    # Check for existing insurance with same NIT
    existing = InsuranceCompany.query.filter_by(tax_nit=data.get('tax_nit')).first()
    if existing:
        return jsonify({"error": "a insurance company with that NIT already exist"}), 409

    new_insurance = InsuranceCompany(
        name=data.get('name'),
        tax_nit=data.get('tax_nit'),
        contact=data.get('contact'),
        status=data.get('status', True)
    )

    try:
        db.session.add(new_insurance)
        db.session.commit()
        return jsonify(new_insurance.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def update_insurance_controller(insurance_id):
    insurance = InsuranceCompany.query.get(insurance_id)
    if not insurance:
        return jsonify({"error": "insurance company not found"}), 404

    data = request.get_json()
    
    # dinamic update of fields
    for key, value in data.items():
        if hasattr(insurance, key):
            setattr(insurance, key, value)

    db.session.commit()
    return jsonify(insurance.to_dict()), 200

def delete_insurance_controller(insurance_id):
    insurance = InsuranceCompany.query.get(insurance_id)
    if not insurance:
        return jsonify({"error": "insurance company not found"}), 404

    # In master entities like this, sometimes a logical deletion (status=False) is better
    # But here we implement physical deletion as requested.
    try:
        db.session.delete(insurance)
        db.session.commit()
        return jsonify({"message": "insurance company deleat sucefully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "The insurance company cannot be deleted because it has linked records"}), 409
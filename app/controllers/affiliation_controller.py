from flask import jsonify, request
from app.models.afilliation import Affiliation
from app.models.person import Person
from app.models.coverage_plans import CoveragePlan
from app import db
from datetime import datetime

def create_affiliation_controller():
    data = request.get_json()
    
    # 1. Validate existence of Person and CoveragePlan
    person = Person.query.get(data.get('personId'))
    plan = CoveragePlan.query.get(data.get('planId'))
    
    if not person or not plan:
        return jsonify({"error": "person o coverage plan not found"}), 404

    # 2. date convertor
    try:
        valid_from = datetime.strptime(data.get('validFrom'), '%Y-%m-%d').date()
        valid_until = None
        if data.get('validUntil'):
            valid_until = datetime.strptime(data.get('validUntil'), '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "date format. Use AAAA-MM-DD"}), 400

    new_affiliation = Affiliation(
        person_id=data.get('personId'),
        plan_id=data.get('planId'),
        policy_number=data.get('policyNumber'),
        valid_from=valid_from,
        valid_until=valid_until,
        copayment=data.get('copayment', 0.0),
        deductible=data.get('deductible', 0.0)
    )

    db.session.add(new_affiliation)
    db.session.commit()
    return jsonify(new_affiliation.to_dict()), 201

def get_person_affiliations_controller(person_id):
    affiliations = Affiliation.query.filter_by(person_id=person_id, active=True).all()
    return jsonify([a.to_dict() for a in affiliations]), 200

def deactivate_affiliation_controller(affiliation_id):
    affiliation = Affiliation.query.get(affiliation_id)
    if not affiliation:
        return jsonify({"error": "affiliation not found"}), 404
    
    affiliation.active = False
    db.session.commit()
    return jsonify({"message": "Affiliation deley sussefuly"}), 200
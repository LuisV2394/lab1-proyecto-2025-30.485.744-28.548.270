# from flask import jsonify, request
# from app.models.affiliation import Affiliations
# from app.models.person import Person
# from app.models.coverage_plans import CoveragePlan
# from app.models.payer import Payer   # <--- importar modelo Payer
# from app import db
# from datetime import datetime

# # GET ALL AFFILIATIONS
# def get_all_affiliations_controller():
#     try:
#         affiliations = Affiliation.query.all()
#         return jsonify([a.to_dict() for a in affiliations]), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # CREATE AFFILIATION
# def create_affiliation_controller():
#     data = request.get_json() or {}

#     # Validar campos obligatorios
#     required_fields = ["personId", "planId", "payerId", "validFrom", "policyNumber"]
#     missing_fields = [f for f in required_fields if not data.get(f)]
#     if missing_fields:
#         return jsonify({"error": f"Faltan campos obligatorios: {missing_fields}"}), 400

#     # Validar existencia de Person, CoveragePlan y Payer
#     person = Person.query.get(data.get('personId'))
#     plan = CoveragePlan.query.get(data.get('planId'))
#     payer = Payer.query.get(data.get('payerId'))
#     if not person or not plan or not payer:
#         return jsonify({"error": "Person, CoveragePlan o Payer no encontrados"}), 404

#     # Validar fechas
#     try:
#         valid_from = datetime.strptime(data.get('validFrom'), '%Y-%m-%d').date()
#         valid_until = datetime.strptime(data.get('validUntil'), '%Y-%m-%d').date() if data.get('validUntil') else None
#         if valid_until and valid_until < valid_from:
#             return jsonify({"error": "validUntil no puede ser menor que validFrom"}), 400
#     except ValueError:
#         return jsonify({"error": "Formato de fecha inválido. Use YYYY-MM-DD"}), 400

#     # Validar copayment y deductible
#     try:
#         copayment = float(data.get('copayment', 0.0))
#         deductible = float(data.get('deductible', 0.0))
#         if copayment < 0 or deductible < 0:
#             return jsonify({"error": "copayment y deductible deben ser >= 0"}), 400
#     except ValueError:
#         return jsonify({"error": "copayment y deductible deben ser números"}), 400

#     # Validar unicidad de policy_number
#     if Affiliation.query.filter_by(policy_number=data.get("policyNumber")).first():
#         return jsonify({"error": "policyNumber ya existe"}), 409

#     new_affiliation = Affiliation(
#         person_id=data.get('personId'),
#         plan_id=data.get('planId'),
#         payer_id=data.get('payerId'),  # <--- asignar payer_id
#         policy_number=data.get('policyNumber'),
#         valid_from=valid_from,
#         valid_until=valid_until,
#         copayment=copayment,
#         deductible=deductible,
#         active=True
#     )

#     try:
#         db.session.add(new_affiliation)
#         db.session.commit()
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"error": str(e)}), 500

#     return jsonify(new_affiliation.to_dict()), 201

# # GET AFFILIATIONS BY PERSON
# def get_person_affiliations_controller(person_id):
#     person = Person.query.get(person_id)
#     if not person:
#         return jsonify({"error": "Person not found"}), 404

#     affiliations = Affiliation.query.filter_by(person_id=person_id, active=True).all()
#     return jsonify([a.to_dict() for a in affiliations]), 200

# # UPDATE AFFILIATION
# def update_affiliation_controller(affiliation_id):
#     data = request.get_json() or {}
#     affiliation = Affiliation.query.get(affiliation_id)
#     if not affiliation:
#         return jsonify({"error": "Affiliation not found"}), 404

#     # Actualizar plan
#     if "planId" in data:
#         plan = CoveragePlan.query.get(data.get("planId"))
#         if not plan:
#             return jsonify({"error": "CoveragePlan no encontrado"}), 404
#         affiliation.plan_id = plan.id

#     # Actualizar policy_number
#     if "policyNumber" in data:
#         existing = Affiliation.query.filter(
#             Affiliation.policy_number == data.get("policyNumber"),
#             Affiliation.id != affiliation.id
#         ).first()
#         if existing:
#             return jsonify({"error": "policyNumber ya existe"}), 409
#         affiliation.policy_number = data.get("policyNumber")

#     # Actualizar fechas
#     try:
#         if "validFrom" in data:
#             affiliation.valid_from = datetime.strptime(data.get("validFrom"), '%Y-%m-%d').date()
#         if "validUntil" in data:
#             valid_until = datetime.strptime(data.get("validUntil"), '%Y-%m-%d').date()
#             if valid_until < affiliation.valid_from:
#                 return jsonify({"error": "validUntil no puede ser menor que validFrom"}), 400
#             affiliation.valid_until = valid_until
#     except ValueError:
#         return jsonify({"error": "Formato de fecha inválido. Use YYYY-MM-DD"}), 400

#     # Actualizar copayment y deductible
#     try:
#         if "copayment" in data:
#             copayment = float(data.get("copayment"))
#             if copayment < 0:
#                 return jsonify({"error": "copayment debe ser >= 0"}), 400
#             affiliation.copayment = copayment
#         if "deductible" in data:
#             deductible = float(data.get("deductible"))
#             if deductible < 0:
#                 return jsonify({"error": "deductible debe ser >= 0"}), 400
#             affiliation.deductible = deductible
#     except ValueError:
#         return jsonify({"error": "copayment y deductible deben ser números"}), 400

#     try:
#         db.session.commit()
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"error": str(e)}), 500

#     return jsonify({"message": "Affiliation updated successfully", "affiliation": affiliation.to_dict()}), 200

# # DEACTIVATE AFFILIATION
# def deactivate_affiliation_controller(affiliation_id):
#     affiliation = Affiliation.query.get(affiliation_id)
#     if not affiliation:
#         return jsonify({"error": "Affiliation not found"}), 404

#     if not affiliation.active:
#         return jsonify({"message": "Affiliation already deactivated"}), 200

#     affiliation.active = False
#     try:
#         db.session.commit()
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"error": str(e)}), 500

#     return jsonify({"message": "Affiliation deactivated successfully"}), 200
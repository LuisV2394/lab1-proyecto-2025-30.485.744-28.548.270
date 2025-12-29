from flask import jsonify, request
from app.models.person import Person
from app import db
from datetime import datetime
import re
from app.models.person import Person


# Obtener todas las personas
def get_all_people_controller():
    people = Person.query.all()
    return jsonify([p.to_dict() for p in people]), 200


# Obtener persona por ID
def get_person_by_id_controller(person_id):
    person = Person.query.get(person_id)
    if not person:
        return jsonify({"error": "Person not found"}), 404
    
    return jsonify(person.to_dict()), 200

def create_person_controller():
    data = request.get_json()
    required_fields = ["first_name", "last_name"]
    
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    email = data.get("email")
    if email:
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            return jsonify({"error": "Invalid email format"}), 400
        
        existing_person = Person.query.filter_by(email=email).first()
        if existing_person:
            return jsonify({"error": "Email already in use"}), 400

    new_person = Person(
        document_number=data.get("document_number"),
        first_name=data["first_name"],
        last_name=data["last_name"],
        gender=data.get("gender"),
        birth_date=data.get("birth_date"),
        email=email,
        phone=data.get("phone"),
        address=data.get("address"),
        emergency_contact=data.get("emergency_contact"),
        active=data.get("active", True)
    )

    db.session.add(new_person)
    db.session.commit()

    return jsonify({
        "message": "Person created successfully",
        "person": new_person.to_dict()
    }), 201

# Actualizar persona
def update_person_controller(person_id):
    person = Person.query.get(person_id)
    if not person:
        return jsonify({"error": "Person not found"}), 404

    data = request.get_json()

    for key, value in data.items():
        if hasattr(person, key):

            if key == "birth_date":
                if value:
                    value = datetime.strptime(value, "%Y-%m-%d").date()
                else:
                    value = None

            setattr(person, key, value)

    db.session.commit()

    return jsonify({
        "message": "Person updated successfully",
        "person": person.to_dict()
    }), 200


# Desactivar persona
def deactivate_person_controller(person_id):
    person = Person.query.get(person_id)
    if not person:
        return jsonify({"error": "Person not found"}), 404

    person.active = False
    db.session.commit()

    return jsonify({"message": "Person deactivated successfully"}), 200
from flask import jsonify, request
import re
from app.models.user import User
from app.models.person import Person
from app import db

EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
)

def get_all_users_controller():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users]), 200

def get_user_by_id_controller(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

def create_user_controller():
    data = request.get_json()

    required_fields = ["person_id", "username", "password", "email"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Validar formato de email
    email = data["email"].strip().lower()
    if not EMAIL_REGEX.match(email):
        return jsonify({"error": "Invalid email format"}), 400

    person = Person.query.get(data["person_id"])
    if not person:
        return jsonify({"error": "Person not found"}), 404

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "Username already exists"}), 409

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 409

    if User.query.filter_by(person_id=data["person_id"]).first():
        return jsonify({"error": "This person already has a user"}), 409

    new_user = User(
        person_id=data["person_id"],
        username=data["username"],
        email=email,
        is_active=data.get("is_active", True)
    )
    new_user.set_password(data["password"])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User created successfully",
        "user": new_user.to_dict()
    }), 201

def update_user_controller(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    for key, value in data.items():
        if key == "password":
            user.set_password(value)
        elif hasattr(user, key):
            setattr(user, key, value)

    db.session.commit()

    return jsonify({
        "message": "User updated successfully",
        "user": user.to_dict()
    }), 200

def deactivate_user_controller(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    user.is_active = False
    db.session.commit()

    return jsonify({"message": "User deactivated successfully"}), 200
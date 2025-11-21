from flask import Blueprint, jsonify, request
from app.models.user import User
from app.models.person import Person
from app import db
from app.utils.middleware import role_required
from flask_jwt_extended import jwt_required
from flasgger.utils import swag_from
import os

users_bp = Blueprint("users", __name__, url_prefix="/users")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "users")
)
print("BASE_DOCS:", BASE_DOCS)  # Para verificar la ruta

# Obtener todos los usuarios
@users_bp.route("/", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_all.yml"))
def get_all_users():
    users = User.query.all()
    data = [u.to_dict() for u in users]
    return jsonify(data), 200

# Obtener usuario por ID
@users_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "get_by_id.yml"))
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

# Crear nuevo usuario
@users_bp.route("/", methods=["POST"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "create.yml"))
def create_user():
    data = request.get_json()

    required_fields = ["person_id", "username", "password"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    person = Person.query.get(data["person_id"])
    if not person:
        return jsonify({"error": "Person not found"}), 404

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "Username already exists"}), 409

    # Validar que la persona no tenga ya un usuario
    if User.query.filter_by(person_id=data["person_id"]).first():
        return jsonify({"error": "This person already has a user"}), 409
    
    
    
    new_user = User(
        person_id=data["person_id"],
        username=data["username"],
        email=data.get("email"),
        is_active=data.get("is_active", True)
    )
    new_user.set_password(data["password"])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User created successfully",
        "user": new_user.to_dict()
    }), 201

# Actualizar usuario existente
@users_bp.route("/<int:user_id>", methods=["PATCH"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "update.yml"))
def update_user(user_id):
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

# Desactivar usuario
@users_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
@role_required(["admin"])
@swag_from(os.path.join(BASE_DOCS, "delete.yml"))
def deactivate_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    user.is_active = False
    db.session.commit()

    return jsonify({"message": "User deactivated successfully"}), 200
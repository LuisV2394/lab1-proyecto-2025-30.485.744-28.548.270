from flask import Blueprint, jsonify, request
from app.models.professional import Professional
from app import db
from app.utils.middleware import role_required

professionals_bp = Blueprint("professionals", __name__, url_prefix="/professionals")

@professionals_bp.route("/", methods=["GET"])
@role_required(["administrator", "auditor"])
def list_professionals():
    professionals = Professional.query.all()
    data = [p.to_dict() for p in professionals]
    return jsonify(data), 200

@professionals_bp.route("/", methods=["POST"])
@role_required(["administrator"])
def create_professional():
    data = request.get_json()
    professional = Professional(**data)
    db.session.add(professional)
    db.session.commit()
    return jsonify({"message": "Professional created successfully"}), 201
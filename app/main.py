from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return jsonify({
        "message": "Medical API running",
        "status": "ok",
        "version": "1.0.0"
    })
from flask import Blueprint, request, jsonify
from models.diagnoses import Diagnosis
from app import db
from flasgger import swag_from
from flask_jwt_extended import jwt_required

diagnosis_bp = Blueprint('diagnoses', __name__)

@diagnosis_bp.route('/diagnoses', methods=['POST'])
@jwt_required()
@swag_from('../docs/diagnosis_create.yml')
def add_diagnosis():
    data = request.json
    
    # Regla: Si es 'main', actualizar otros registros del mismo episodio
    if data.get('main') is True:
        Diagnosis.query.filter_by(episode_id=data.get('episode_id'), main=True).update({'main': False})
    
    new_diag = Diagnosis(
        episode_id=data.get('episode_id'),
        code=data.get('code'),
        description=data.get('description'),
        type=data.get('type'),
        main=data.get('main', False)
    )
    db.session.add(new_diag)
    db.session.commit()
    return jsonify({"message": "Diagnóstico añadido", "id": new_diag.id}), 201
from flask import Blueprint, request, jsonify
from models.consets import Consent
from app import db
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from datetime import datetime

consent_bp = Blueprint('consents', __name__)

@consent_bp.route('/consents', methods=['POST'])
@jwt_required()
@swag_from('../docs/consent_create.yml')
def create_consent():
    data = request.json
    
    # Mock de generación de ID de archivo
    mock_file_id = f"file_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{data.get('person_id')}.pdf"
    
    new_consent = Consent(
        person_id=data.get('person_id'),
        process_type=data.get('processTipe'),
        method=data.get('method'),
        file_id=mock_file_id, 
        date=datetime.utcnow()
    )
    
    db.session.add(new_consent)
    db.session.commit()
    return jsonify({
        "message": "Consentimiento registrado", 
        "id": new_consent.id,
        "file_reference": mock_file_id
    }), 201
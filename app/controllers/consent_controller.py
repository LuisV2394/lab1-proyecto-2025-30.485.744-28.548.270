from flask import request, jsonify
from datetime import datetime
from app.models.consets import Consent
from app import db


def create_consent_controller():
    data = request.json

    # Generación de ID de archivo (mock)
    mock_file_id = (
        f"file_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_"
        f"{data.get('person_id')}.pdf"
    )

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
from flask import request, jsonify, Blueprint
from datetime import datetime
from app.models.consets import Consent
from app import db

consent_bp = Blueprint('consent_bp', __name__)


@consent_bp.route('/consents', methods=['POST'])
def create_consent_controller():
    data = request.json

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


@consent_bp.route('/consents', methods=['GET'])
def get_all_consents_controller():
    consents = Consent.query.all()

    return jsonify([
        {
            "id": consent.id,
            "person_id": consent.person_id,
            "process_type": consent.process_type,
            "method": consent.method,
            "file_id": consent.file_id,
            "date": consent.date.isoformat()
        }
        for consent in consents
    ]), 200


@consent_bp.route('/consents/<int:consent_id>', methods=['GET'])
def get_consent_by_id_controller(consent_id):
    consent = Consent.query.get(consent_id)

    if not consent:
        return jsonify({"message": "Consentimiento no encontrado"}), 404

    return jsonify({
        "id": consent.id,
        "person_id": consent.person_id,
        "process_type": consent.process_type,
        "method": consent.method,
        "file_id": consent.file_id,
        "date": consent.date.isoformat()
    }), 200


@consent_bp.route('/consents/<int:consent_id>', methods=['PUT'])
def update_consent_controller(consent_id):
    consent = Consent.query.get(consent_id)

    if not consent:
        return jsonify({"message": "Consentimiento no encontrado"}), 404

    data = request.json

    consent.person_id = data.get('person_id', consent.person_id)
    consent.process_type = data.get('processTipe', consent.process_type)
    consent.method = data.get('method', consent.method)

    db.session.commit()

    return jsonify({
        "message": "Consentimiento actualizado",
        "id": consent.id
    }), 200


@consent_bp.route('/consents/<int:consent_id>', methods=['DELETE'])
def delete_consent_controller(consent_id):
    consent = Consent.query.get(consent_id)

    if not consent:
        return jsonify({"message": "Consentimiento no encontrado"}), 404

    db.session.delete(consent)
    db.session.commit()

    return jsonify({
        "message": "Consentimiento eliminado"
    }), 200
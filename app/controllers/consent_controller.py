from flask import request, jsonify
from datetime import datetime
from app.models.consets import Consent
from app import db
from app.models.person import Person

def create_consent_controller():
    data = request.json or {}

    try:
        # 1️⃣ Campos obligatorios
        if not all([data.get('person_id'), data.get('processTipe'), data.get('method')]):
            return jsonify({"error": "Faltan campos obligatorios"}), 400

        # 2️⃣ Validar existencia de la persona
        if not Person.query.get(data.get('person_id')):
            return jsonify({"error": "La persona no existe"}), 404

        # 3️⃣ Crear file_id simulado
        mock_file_id = (
            f"file_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_"
            f"{data.get('person_id')}.pdf"
        )

        # 4️⃣ Crear consentimiento
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

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
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

def delete_consent_controller(consent_id):
    consent = Consent.query.get(consent_id)

    if not consent:
        return jsonify({"message": "Consentimiento no encontrado"}), 404

    db.session.delete(consent)
    db.session.commit()

    return jsonify({
        "message": "Consentimiento eliminado"
    }), 200
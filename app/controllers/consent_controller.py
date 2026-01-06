from flask import request, jsonify
from datetime import datetime
from app.models.consents import Consent
from app import db
from app.models.person import Person

ALLOWED_METHODS = {"DIGITAL_SIGNATURE", "VERBAL_WITH_RECORD"}

# Crear consentimiento
def create_consent_controller():
    data = request.json or {}

    try:
        # Campos obligatorios
        if not all([data.get('person_id'), data.get('process_type'), data.get('method')]):
            return jsonify({"error": "Faltan campos obligatorios"}), 400

        # Validar existencia de la persona
        person = Person.query.get(data.get('person_id'))
        if not person:
            return jsonify({"error": "La persona no existe"}), 404

        # Validar method
        method = data.get('method')
        if method not in ALLOWED_METHODS:
            return jsonify({"error": f"Method inválido. Valores permitidos: {list(ALLOWED_METHODS)}"}), 400

        # Crear file_id simulado solo si method requiere archivo
        file_id = None
        if method == "DIGITAL_SIGNATURE":
            file_id = f"file_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{data.get('person_id')}.pdf"

        # Crear consentimiento
        new_consent = Consent(
            person_id=data.get('person_id'),
            process_type=data.get('process_type'),
            method=method,
            file_id=file_id,
            date=datetime.utcnow()
        )

        db.session.add(new_consent)
        db.session.commit()

        return jsonify({
            "message": "Consentimiento registrado",
            "id": new_consent.id,
            "file_reference": file_id
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Obtener todos
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
        } for consent in consents
    ]), 200

# Obtener por ID
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

# Actualizar consentimiento
def update_consent_controller(consent_id):
    consent = Consent.query.get(consent_id)
    if not consent:
        return jsonify({"message": "Consentimiento no encontrado"}), 404

    data = request.json or {}

    # Validar persona si viene
    if 'person_id' in data:
        person = Person.query.get(data['person_id'])
        if not person:
            return jsonify({"error": "La persona no existe"}), 404
        consent.person_id = data['person_id']

    # Validar process_type
    if 'process_type' in data:
        consent.process_type = data['process_type']

    # Validar method
    if 'method' in data:
        method = data['method']
        if method not in ALLOWED_METHODS:
            return jsonify({"error": f"Method inválido. Valores permitidos: {list(ALLOWED_METHODS)}"}), 400
        consent.method = method

    db.session.commit()
    return jsonify({
        "message": "Consentimiento actualizado",
        "id": consent.id
    }), 200

# Eliminar consentimiento
def delete_consent_controller(consent_id):
    consent = Consent.query.get(consent_id)
    if not consent:
        return jsonify({"message": "Consentimiento no encontrado"}), 404

    db.session.delete(consent)
    db.session.commit()
    return jsonify({"message": "Consentimiento eliminado"}), 200
from flask import request, jsonify
from app.models.diagnoses import Diagnosis
from app.models.episodes import Episode
from app import db

ALLOWED_TYPES = ['PRESUMPTIVE', 'DEFINITIVE']

def add_diagnosis_controller():
    data = request.json or {}

    episode_id = data.get("episode_id")
    code = data.get("code")
    description = data.get("description")
    type_diagnoses = data.get("type_diagnoses")
    main = data.get("main", False)

    # Validar campos obligatorios
    if not all([episode_id, code, description, type_diagnoses]):
        return jsonify({"error": "Faltan campos obligatorios: episode_id, code, description, type_diagnoses"}), 400

    # Validar tipo de diagnóstico
    if type_diagnoses not in ALLOWED_TYPES:
        return jsonify({"error": f"type_diagnoses inválido. Valores permitidos: {ALLOWED_TYPES}"}), 400

    # Validar existencia del episodio
    episode = Episode.query.get(episode_id)
    if not episode:
        return jsonify({"error": "El episodio no existe"}), 404

    try:
        # Si se marca como principal, desmarcar otros diagnósticos principales del episodio
        if main:
            Diagnosis.query.filter(
                Diagnosis.episode_id == episode_id,
                Diagnosis.main == True
            ).update({"main": False})

        # Crear nuevo diagnóstico
        new_diag = Diagnosis(
            episode_id=episode_id,
            code=code,
            description=description,
            type_diagnoses=type_diagnoses,
            main=main
        )

        db.session.add(new_diag)
        db.session.commit()

        return jsonify({
            "message": "Diagnóstico añadido",
            "id": new_diag.id
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


def get_all_diagnoses_controller():
    diagnoses = Diagnosis.query.all()

    return jsonify([
        {
            "id": d.id,
            "episode_id": d.episode_id,
            "code": d.code,
            "description": d.description,
            "type_diagnoses": d.type_diagnoses,
            "main": d.main,
            "created_at": d.created_at.isoformat(),
            "updated_at": d.updated_at.isoformat()
        }
        for d in diagnoses
    ]), 200


def get_diagnosis_by_id_controller(diagnosis_id):
    d = Diagnosis.query.get(diagnosis_id)

    if not d:
        return jsonify({"message": "Diagnóstico no encontrado"}), 404

    return jsonify({
        "id": d.id,
        "episode_id": d.episode_id,
        "code": d.code,
        "description": d.description,
        "type_diagnoses": d.type_diagnoses,
        "main": d.main,
        "created_at": d.created_at.isoformat(),
        "updated_at": d.updated_at.isoformat()
    }), 200


def update_diagnosis_controller(diagnosis_id):
    d = Diagnosis.query.get(diagnosis_id)

    if not d:
        return jsonify({"message": "Diagnóstico no encontrado"}), 404

    data = request.json

    # Validar tipo_diagnoses si se actualiza
    type_diagnoses = data.get("type_diagnoses", d.type_diagnoses)
    if type_diagnoses not in ALLOWED_TYPES:
        return jsonify({"error": f"type_diagnoses inválido. Valores permitidos: {ALLOWED_TYPES}"}), 400

    # Regla: solo un diagnóstico principal por episodio
    if data.get("main") is True:
        Diagnosis.query.filter(
            Diagnosis.episode_id == d.episode_id,
            Diagnosis.id != diagnosis_id,
            Diagnosis.main == True
        ).update({"main": False})

    # Actualizar campos
    d.code = data.get("code", d.code)
    d.description = data.get("description", d.description)
    d.type_diagnoses = type_diagnoses
    d.main = data.get("main", d.main)

    try:
        db.session.commit()
        return jsonify({
            "message": "Diagnóstico actualizado",
            "id": d.id
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


def delete_diagnosis_controller(diagnosis_id):
    d = Diagnosis.query.get(diagnosis_id)

    if not d:
        return jsonify({"message": "Diagnóstico no encontrado"}), 404

    try:
        db.session.delete(d)
        db.session.commit()
        return jsonify({"message": "Diagnóstico eliminado"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
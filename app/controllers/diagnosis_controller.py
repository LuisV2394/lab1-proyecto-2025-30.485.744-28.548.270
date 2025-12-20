from flask import request, jsonify
from app.models.diagnoses import Diagnosis
from app import db
from app.models.episodes import Episode

def add_diagnosis_controller():
    data = request.json or {}

    try:
        # 1️⃣ Campos obligatorios
        if not all([data.get("episode_id"), data.get("code"), data.get("description"), data.get("type")]):
            return jsonify({"error": "Faltan campos obligatorios"}), 400

        episode_id = data.get("episode_id")

        # 2️⃣ Validar existencia del episodio
        if not Episode.query.get(episode_id):
            return jsonify({"error": "El episodio no existe"}), 404

        # 3️⃣ Crear nuevo diagnóstico
        new_diag = Diagnosis(
            episode_id=episode_id,
            code=data.get("code"),
            description=data.get("description"),
            type=data.get("type"),
            main=data.get("main", False)
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
            "id": diagnosis.id,
            "episode_id": diagnosis.episode_id,
            "code": diagnosis.code,
            "description": diagnosis.description,
            "type": diagnosis.type,
            "main": diagnosis.main
        }
        for diagnosis in diagnoses
    ]), 200


def get_diagnosis_by_id_controller(diagnosis_id):
    diagnosis = Diagnosis.query.get(diagnosis_id)

    if not diagnosis:
        return jsonify({"message": "Diagnóstico no encontrado"}), 404

    return jsonify({
        "id": diagnosis.id,
        "episode_id": diagnosis.episode_id,
        "code": diagnosis.code,
        "description": diagnosis.description,
        "type": diagnosis.type,
        "main": diagnosis.main
    }), 200


def update_diagnosis_controller(diagnosis_id):
    diagnosis = Diagnosis.query.get(diagnosis_id)

    if not diagnosis:
        return jsonify({"message": "Diagnóstico no encontrado"}), 404

    data = request.json

    # Regla: si se marca como principal, desmarcar otros diagnósticos del episodio
    if data.get("main") is True:
        Diagnosis.query.filter(
            Diagnosis.episode_id == diagnosis.episode_id,
            Diagnosis.id != diagnosis_id,
            Diagnosis.main == True
        ).update({"main": False})

    diagnosis.code = data.get("code", diagnosis.code)
    diagnosis.description = data.get("description", diagnosis.description)
    diagnosis.type = data.get("type", diagnosis.type)
    diagnosis.main = data.get("main", diagnosis.main)

    db.session.commit()

    return jsonify({
        "message": "Diagnóstico actualizado",
        "id": diagnosis.id
    }), 200


def delete_diagnosis_controller(diagnosis_id):
    diagnosis = Diagnosis.query.get(diagnosis_id)

    if not diagnosis:
        return jsonify({"message": "Diagnóstico no encontrado"}), 404

    db.session.delete(diagnosis)
    db.session.commit()

    return jsonify({
        "message": "Diagnóstico eliminado"
    }), 200
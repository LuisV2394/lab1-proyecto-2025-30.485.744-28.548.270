from flask import request, jsonify
from app.models.diagnoses import Diagnosis
from app import db


def add_diagnosis_controller():
    data = request.json

    episode_id = data.get("episode_id")

    # Regla: Si es 'main', actualizar otros diagnósticos del mismo episodio
    if data.get("main") is True:
        Diagnosis.query.filter_by(
            episode_id=episode_id,
            main=True
        ).update({"main": False})

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
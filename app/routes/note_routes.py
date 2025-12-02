from flask import Blueprint, request, jsonify
from app.models.note import ClinicalNote
from app.models.episodes import Episode
from app import db
from flasgger import swag_from
from flask_jwt_extended import jwt_required
import os

note_bp = Blueprint('notes', __name__, url_prefix="/notes")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "note")
)

@note_bp.route('/', methods=['POST'])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'create.yml'))
def create_note():
    data = request.json

    episode_id = data.get('episode_id')
    professional_id = data.get('professional_id')

    # Validar episodio
    episode = Episode.query.get(episode_id)
    if not episode or episode.status == 'close':
        return jsonify({"error": "El episodio no existe o está cerrado"}), 400

    # Determinar contenido
    # Si viene contenido directo
    content = data.get('content')

    # Si todavía están enviando SOAP, los convertimos automáticamente
    if not content:
        sub = data.get('sub_objective', "")
        obj = data.get('objective', "")
        test = data.get('test', "")
        plan = data.get('plan', "")

        if any([sub, obj, test, plan]):
            content = (
                f"S: {sub}\n"
                f"O: {obj}\n"
                f"A: {test}\n"
                f"P: {plan}"
            )
        else:
            return jsonify({"error": "Debe enviar 'content' o campos SOAP"}), 400

    # Crear nota
    new_note = ClinicalNote(
        episode_id=episode_id,
        professional_id=professional_id,
        note_type=data.get('note_type', 'EVOLUTION'),
        content=content,
        version=data.get('version', 1)
    )

    db.session.add(new_note)
    db.session.commit()

    return jsonify({
        "message": "Nota clínica registrada",
        "id": new_note.id
    }), 201
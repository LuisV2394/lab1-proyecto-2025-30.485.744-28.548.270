from flask import Blueprint, request, jsonify
from models.note import ClinicalNote
from models.episodes import Episode
from app import db
from flasgger import swag_from
from flask_jwt_extended import jwt_required

note_bp = Blueprint('notes', __name__)

@note_bp.route('/note', methods=['POST'])
@jwt_required()
@swag_from('../docs/note_create.yml')
def create_note():
    data = request.json
    episode_id = data.get('episode_id')
    
    # Validar estado del episodio
    episode = Episode.query.get(episode_id)
    if not episode or episode.status == 'close':
        return jsonify({"error": "El episodio no existe o está cerrado"}), 400

    # Mock de adjuntos
    attachments_mock = data.get('attachments', [])

    new_note = ClinicalNote(
        episode_id=episode_id,
        professional_id=data.get('professional_id'),
        sub_objective=data.get('sub_objective'),
        objective=data.get('objective'),
        test=data.get('test'),
        plan=data.get('plan'),
        attachments=attachments_mock 
    )
    
    db.session.add(new_note)
    db.session.commit()
    return jsonify({"message": "Nota clínica registrada", "id": new_note.id}), 201
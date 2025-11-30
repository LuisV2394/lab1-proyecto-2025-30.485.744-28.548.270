from flask import Blueprint, request, jsonify
from app.models.agenda import db, Block
from app import db
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from datetime import datetime
import os

agenda_bp = Blueprint('agenda', __name__, url_prefix="/agenda")

BASE_DOCS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "agenda")
)

@agenda_bp.route('/', methods=['POST'])
@jwt_required()
@swag_from(os.path.join(BASE_DOCS, 'create.yml'))
def create_block():
    data = request.json
    prof_id = data.get('professionalId')
    start = datetime.fromisoformat(data.get('start'))
    end = datetime.fromisoformat(data.get('end'))

    # REGLA: Evitar solapamiento de horarios del mismo profesional
    # Un solapamiento ocurre si (StartA < EndB) y (EndA > StartB)
    overlap = Block.query.filter(
        Block.professional_id == prof_id,
        Block.start < end,
        Block.end > start,
        Block.state != 'close'
    ).first()

    if overlap:
        return jsonify({"error": "El profesional ya tiene un bloque en este horario"}), 409

    new_block = Block(
        professional_id=prof_id,
        unit_id=data.get('unitId'),
        start=start,
        end=end,
        ability=data.get('ability', 1),
        state='open'
    )
    
    db.session.add(new_block)
    db.session.commit()
    
    return jsonify({"message": "Bloque creado", "id": new_block.id}), 201
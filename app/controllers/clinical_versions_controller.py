from flask import jsonify
from app.models.clinical_versions import ClinicalVersion
from app import db

def get_history_by_entity_controller(entity_type, entity_id):
    """
    Gets all previous versions of a specific note or result.
    """
    versions = ClinicalVersion.query.filter_by(
        entity_type=entity_type, 
        entity_id=entity_id
    ).order_by(ClinicalVersion.version_number.desc()).all()
    
    return jsonify([v.to_dict() for v in versions]), 200

def create_version_snapshot(entity_type, entity_id, content, user_id, current_version):
    """
   Internal (helper) function to save the previous state before updating.
    """
    try:
        new_version = ClinicalVersion(
            entity_type=entity_type,
            entity_id=entity_id,
            content_snapshot=content,
            user_id=user_id,
            version_number=current_version
        )
        db.session.add(new_version)
        # We don't commit here; we let the main controller do it
        # along with the update of the note/result to ensure atomicity.
    except Exception as e:
        print(f"Error creating version: {e}")
from flask import jsonify, request
from app.models.clinical_versions import ClinicalVersion
from app import db

# GET ALL VERSIONS
def get_all_versions_controller():
    versions = ClinicalVersion.query.order_by(
        ClinicalVersion.created_at.desc()
    ).all()

    return jsonify([v.to_dict() for v in versions]), 200

# GET VERSION BY ID
def get_version_by_id_controller(version_id):
    version = ClinicalVersion.query.get(version_id)

    if not version:
        return jsonify({"error": "Clinical version not found"}), 404

    return jsonify({
        "message": "Clinical version retrieved successfully",
        "version": version.to_dict()
    }), 200

# GET HISTORY BY ENTITY
def get_history_by_entity_controller(entity_type, entity_id):
    if not entity_type:
        return jsonify({"error": "entity_type is required"}), 400

    if not entity_id:
        return jsonify({"error": "entity_id is required"}), 400

    # Optional validation list
    allowed_types = ["clinical_note", "lab_result", "prescription", "episode"]

    if entity_type not in allowed_types:
        return jsonify({
            "error": "Invalid entity_type",
            "allowed": allowed_types
        }), 400

    versions = ClinicalVersion.query.filter_by(
        entity_type=entity_type,
        entity_id=entity_id
    ).order_by(ClinicalVersion.version_number.desc()).all()

    if not versions:
        return jsonify({"message": "No versions found"}), 200

    return jsonify({
        "message": "Version history retrieved successfully",
        "count": len(versions),
        "versions": [v.to_dict() for v in versions]
    }), 200

# CREATE VERSION (manual API)
def create_version_controller():
    data = request.get_json() or {}

    required_fields = ["entity_type", "entity_id", "content_snapshot", "user_id", "version_number"]

    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    try:
        new_version = ClinicalVersion(
            entity_type=data["entity_type"],
            entity_id=data["entity_id"],
            content_snapshot=data["content_snapshot"],
            user_id=data["user_id"],
            version_number=data["version_number"]
        )

        db.session.add(new_version)
        db.session.commit()

        return jsonify({
            "message": "Clinical version created successfully",
            "version": new_version.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error creating clinical version", "details": str(e)}), 500

# UPDATE VERSION
def update_version_controller(version_id):
    version = ClinicalVersion.query.get(version_id)

    if not version:
        return jsonify({"error": "Clinical version not found"}), 404

    data = request.get_json() or {}

    allowed_fields = ["content_snapshot"]

    for key, value in data.items():
        if key in allowed_fields:
            setattr(version, key, value)

    try:
        db.session.commit()

        return jsonify({
            "message": "Clinical version updated successfully",
            "version": version.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error updating version", "details": str(e)}), 500

# DELETE VERSION
def delete_version_controller(version_id):
    version = ClinicalVersion.query.get(version_id)

    if not version:
        return jsonify({"error": "Clinical version not found"}), 404

    try:
        db.session.delete(version)
        db.session.commit()

        return jsonify({"message": "Clinical version deleted successfully"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error deleting version", "details": str(e)}), 500

# INTERNAL SNAPSHOT FUNCTION
def create_version_snapshot(entity_type, entity_id, content, user_id, current_version):
    try:
        new_version = ClinicalVersion(
            entity_type=entity_type,
            entity_id=entity_id,
            content_snapshot=content,
            user_id=user_id,
            version_number=current_version
        )
        db.session.add(new_version)
    except Exception as e:
        print(f"Error creating version snapshot: {e}")
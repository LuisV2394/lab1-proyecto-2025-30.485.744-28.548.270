from flask import jsonify, request
from app.models.clinical_versions import ClinicalVersion
from app.models.user import User
from app import db

# ALLOWED ENTITY TYPES
ALLOWED_ENTITY_TYPES = ["clinical_note", "lab_result", "prescription", "episode"]

# GET ALL VERSIONS
def get_all_versions_controller():
    try:
        versions = ClinicalVersion.query.order_by(ClinicalVersion.created_at.desc()).all()
        return jsonify([v.to_dict() for v in versions]), 200
    except Exception as e:
        return jsonify({"error": "Error retrieving clinical versions", "details": str(e)}), 500


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
    if not entity_type or not entity_id:
        return jsonify({"error": "entity_type and entity_id are required"}), 400

    if entity_type not in ALLOWED_ENTITY_TYPES:
        return jsonify({
            "error": "Invalid entity_type",
            "allowed": ALLOWED_ENTITY_TYPES
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


# CREATE VERSION
def create_version_controller():
    data = request.get_json() or {}

    required_fields = ["entity_type", "entity_id", "content_snapshot", "user_id", "version_number"]
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    # VALIDATE ENTITY TYPE
    if data["entity_type"] not in ALLOWED_ENTITY_TYPES:
        return jsonify({"error": "Invalid entity_type", "allowed": ALLOWED_ENTITY_TYPES}), 400

    # VALIDATE USER EXISTS
    user = User.query.get(data["user_id"])
    if not user:
        return jsonify({"error": "User not found"}), 400

    # VALIDATE VERSION NUMBER
    if not isinstance(data["version_number"], int) or data["version_number"] <= 0:
        return jsonify({"error": "version_number must be a positive integer"}), 400

    # VALIDATE CONTENT SNAPSHOT
    if not data["content_snapshot"] or len(data["content_snapshot"]) > 10000:
        return jsonify({"error": "content_snapshot is required and must be less than 10000 characters"}), 400

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
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    allowed_fields = ["content_snapshot"]

    for key, value in data.items():
        if key in allowed_fields:
            if key == "content_snapshot":
                if not value or len(value) > 10000:
                    return jsonify({"error": "content_snapshot is required and must be less than 10000 characters"}), 400
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
    # Validate entity_type
    if entity_type not in ALLOWED_ENTITY_TYPES:
        print(f"Invalid entity_type for snapshot: {entity_type}")
        return None

    # Validate user exists
    user = User.query.get(user_id)
    if not user:
        print(f"User not found for snapshot: {user_id}")
        return None

    # Validate content
    if not content or len(content) > 10000:
        print(f"Invalid content snapshot for version: {current_version}")
        return None

    try:
        new_version = ClinicalVersion(
            entity_type=entity_type,
            entity_id=entity_id,
            content_snapshot=content,
            user_id=user_id,
            version_number=current_version
        )
        db.session.add(new_version)
        db.session.commit()
        return new_version
    except Exception as e:
        db.session.rollback()
        print(f"Error creating version snapshot: {e}")
        return None
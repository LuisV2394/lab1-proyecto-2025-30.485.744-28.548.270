from flask import jsonify, request
from app.models.services import Service
from app import db

# Obtener todos los servicios
def get_all_services_controller():
    services = Service.query.all()
    data = [s.to_dict() for s in services]
    return jsonify(data), 200


# Buscar servicio por ID
def get_service_by_id_controller(service_id):
    service = Service.query.get(service_id)

    if not service:
        return jsonify({"error": "Service not found"}), 404

    return jsonify({
        "message": "Service retrieved successfully",
        "service": service.to_dict()
    }), 200

# Crear un nuevo servicio
def create_service_controller():
    data = request.get_json() or {}

    # Validar campos requeridos
    required_fields = ["code", "name"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Verificar que el código sea único
    existing_service = Service.query.filter_by(code=data["code"]).first()
    if existing_service:
        return jsonify({"error": "Service code already in use"}), 400

    # Validar estimated_time si se proporciona
    estimated_time = data.get("estimated_time")
    if estimated_time is not None:
        if not isinstance(estimated_time, int) or estimated_time < 0:
            return jsonify({"error": "Estimated time must be a positive integer"}), 400

    # Crear el servicio
    new_service = Service(
        code=data["code"],
        name=data["name"],
        group_name=data.get("group_name"),
        requirements=data.get("requirements"),
        estimated_time=estimated_time,
        active=data.get("active", True)
    )

    db.session.add(new_service)
    db.session.commit()

    return jsonify({
        "message": "Service created successfully",
        "service": new_service.to_dict()
    }), 201

# Actualizar servicio existente
def update_service_controller(service_id):
    service = Service.query.get(service_id)
    if not service:
        return jsonify({"error": "Service not found"}), 404

    data = request.get_json() or {}

    for key, value in data.items():
        if hasattr(service, key):

            # Validar código único
            if key == "code" and value:
                existing_service = Service.query.filter(
                    Service.code == value,
                    Service.id != service.id
                ).first()
                if existing_service:
                    return jsonify({"error": "Service code already in use"}), 400

            # Validar estimated_time
            if key == "estimated_time" and value is not None:
                if not isinstance(value, int) or value < 0:
                    return jsonify({"error": "Estimated time must be a positive integer"}), 400

            setattr(service, key, value)

    db.session.commit()

    return jsonify({
        "message": "Service updated successfully",
        "service": service.to_dict()
    }), 200

# Desactivar servicio
def deactivate_service_controller(service_id):
    service = Service.query.get(service_id)
    if not service:
        return jsonify({"error": "Service not found"}), 404

    service.active = False
    db.session.commit()

    return jsonify({"message": "Service deactivated successfully"}), 200
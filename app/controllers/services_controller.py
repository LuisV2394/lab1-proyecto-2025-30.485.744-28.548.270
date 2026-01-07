from flask import jsonify, request
from app.models.services import Service
from app.models.order_item import OrderItem
from app import db

def get_all_services_controller():
    # Optionally filter by group or search by name
    group = request.args.get('group')
    query = Service.query.filter_by(active=True)
    
    if group:
        query = query.filter_by(group=group)
        
    services = query.all()
    return jsonify([s.to_dict() for s in services]), 200

def create_service_controller():
    data = request.get_json()
    
    if not data.get('code') or not data.get('name'):
        return jsonify({"error": "Códe and name obligatory"}), 400

    # Validate unique code
    if Service.query.filter_by(code=data.get('code')).first():
        return jsonify({"error": "validate unic code"}), 409

    new_service = Service(
        code=data.get('code'),
        name=data.get('name'),
        group=data.get('group'),
        requirements=data.get('requirements'),
        estimated_time=data.get('estimated_time')
    )

    db.session.add(new_service)
    db.session.commit()
    return jsonify(new_service.to_dict()), 201

def update_service_controller(service_id):
    service = Service.query.get(service_id)
    if not service:
        return jsonify({"error": "Services not found"}), 404

    data = request.get_json()
    for key in ['name', 'group', 'requirements', 'estimated_time', 'active']:
        if key in data:
            setattr(service, key, data[key])
    db.session.commit()
    return jsonify(service.to_dict()), 200

def delete_service_controller(service_id):
    service = Service.query.get(service_id)
    
    if not service:
        return jsonify({"error": "Servicio no encontrado"}), 404

def delete_service_controller(service_id):
    service = Service.query.get(service_id)
    
    if not service:
        return jsonify({"error": "Servicio no encontrado"}), 404

    # INTEGRITY RULE: Check if the service has already been used in orders
    # We look to see if the code for this service already exists in the order items table
    has_usage = OrderItem.query.filter_by(prestation_code=service.code).first()
    
    if has_usage:
        return jsonify({
            "error": " INTEGRITY RULE: Check if the service has already been used in orders"
                      "We look to see if the code for this service already exists in the order items table"
        }), 400
    
    try:
        db.session.delete(service)
        db.session.commit()
        return jsonify({"message": "service delete sussefuly"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
   
from flask import jsonify, request
from app.models.authorization import Authorization
from app.models.orders import Order
from app import db
from datetime import datetime

def create_authorization_request_controller():
    data = request.get_json()
    
    # Validar orden
    order = Order.query.get(data.get('order_id'))
    if not order:
        return jsonify({"error": "Orden not found"}), 404

    new_auth = Authorization(
        order_id=data.get('order_id'),
        plan_id=data.get('plan_id'),
        status='requested',
        request_date=datetime.utcnow(),
        observations=data.get('observations')
    )

    db.session.add(new_auth)
    db.session.commit()
    return jsonify(new_auth.to_dict()), 201

def update_authorization_response_controller(auth_id):
    data = request.get_json()
    auth = Authorization.query.get(auth_id)
    
    if not auth:
        return jsonify({"error": "authorization solicity not found"}), 404

    # Actualizar respuesta del pagador
    auth.status = data.get('status') # approved / denied
    auth.response_date = datetime.utcnow()
    auth.authorization_number = data.get('authorization_number')
    auth.observations = data.get('observations', auth.observations)

    # REGLA DE NEGOCIO: Si se aprueba, actualizar el estado de la orden
    if auth.status == 'approved':
        order = Order.query.get(auth.order_id)
        if order:
            order.status = 'authorized'

    db.session.commit()
    return jsonify(auth.to_dict()), 200

def get_authorizations_by_order_controller(order_id):
    auths = Authorization.query.filter_by(order_id=order_id).all()
    return jsonify([a.to_dict() for a in auths]), 200
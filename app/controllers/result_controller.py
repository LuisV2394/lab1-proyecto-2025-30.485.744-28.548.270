from flask import jsonify, request
from app.models.result import Result
from app.models.orders import Order
from app import db

def create_result_controller():
    data = request.get_json()
    
    # Valide the required fields
    if 'orderId' not in data or 'summary' not in data:
        return jsonify({"error": "orderId and summary are obligatory"}), 400

    # verifidy that the order exists
    order = Order.query.get(data['orderId'])
    if not order:
        return jsonify({"error": "the asociate order do not exist"}), 404

    new_result = Result(
        order_id=data['orderId'],
        summary=data['summary'],
        file_id=data.get('fileId'),
        version=1
    )

    try:
        db.session.add(new_result)
        
        # ruler of business: when a result is created, the order status changes to 'completed'
        order.status = 'completed'
        
        db.session.commit()
        return jsonify(new_result.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def update_result_controller(result_id):
    data = request.get_json()
    result = Result.query.get(result_id)
    
    if not result:
        return jsonify({"error": "Resultado no encontrado"}), 404

    # update fields
    if 'summary' in data:
        result.summary = data['summary']
    if 'fileId' in data:
        result.file_id = data['fileId']
    
    # increse version by 1
    result.version += 1
    
    db.session.commit()
    return jsonify(result.to_dict()), 200

def delete_result_controller(result_id):
    result = Result.query.get(result_id)
    if not result:
        return jsonify({"error": "Resultado no encontrado"}), 404

    try:
        db.session.delete(result)
        db.session.commit()
        return jsonify({"message": "Resultado eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
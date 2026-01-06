from flask import jsonify, request
from app.models.result import Result
from app.models.orders import Order
from app.models.order_item import OrderItem
from app import db
from datetime import datetime

# Obtener todos los resultados
def get_all_results_controller():
    results = Result.query.all()
    data = [r.to_dict() for r in results]
    return jsonify(data), 200

# Obtener resultado por ID
def get_result_by_id_controller(result_id):
    result = Result.query.get(result_id)
    if not result:
        return jsonify({"error": "Result not found"}), 404

    return jsonify({
        "message": "Result retrieved successfully",
        "result": result.to_dict()
    }), 200

# Crear un nuevo resultado
def create_result_controller():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    required_fields = ["order_id", "summary"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Validar que la orden exista
    order = Order.query.get(data["order_id"])
    if not order:
        return jsonify({"error": "Order not found"}), 404

    # Validar fecha
    if data.get("date"):
        try:
            date = datetime.strptime(data["date"], "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format, should be YYYY-MM-DD"}), 400
    else:
        date = datetime.utcnow()

    new_result = Result(
        order_id=data["order_id"],
        summary=data["summary"],
        file_id=data.get("file_id"),
        date=date
    )

    db.session.add(new_result)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error creating result", "details": str(e)}), 500

    return jsonify({
        "message": "Result created successfully",
        "result": new_result.to_dict()
    }), 201

# Actualizar un resultado existente (versionar)
def update_result_controller(result_id):
    result = Result.query.get(result_id)
    if not result:
        return jsonify({"error": "Result not found"}), 404

    data = request.get_json()
    updated = False

    if "summary" in data and data["summary"]:
        result.summary = data["summary"]
        updated = True

    if "file_id" in data and data["file_id"]:
        result.file_id = data["file_id"]
        updated = True

    if updated:
        result.version += 1  # Incrementar versión al actualizar
        result.updated_at = datetime.utcnow()

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error updating result", "details": str(e)}), 500

    return jsonify({
        "message": "Result updated successfully",
        "result": result.to_dict()
    }), 200
    
# Eliminar un resultado existente
def delete_result_controller(result_id):
    result = Result.query.get(result_id)
    if not result:
        return jsonify({"error": "Result not found"}), 404

    try:
        db.session.delete(result)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error deleting result", "details": str(e)}), 500

    return jsonify({
        "message": "Result deleted successfully"
    }), 200

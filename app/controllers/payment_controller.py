from flask import request, jsonify
from app.models.payments import Payment
from app.models.invoice import Invoice
from app import db
from datetime import datetime

# CREATE – Registrar un nuevo pago
def create_payment_controller():
    data = request.json or {}

    try:
        # Campos obligatorios
        if not all([data.get('invoice_id'), data.get('amount'), data.get('payment_method')]):
            return jsonify({"error": "Faltan campos obligatorios"}), 400

        invoice_id = data.get('invoice_id')
        amount = data.get('amount')
        payment_method = data.get('payment_method')
        reference = data.get('reference')
        paid_at = data.get('paid_at')

        # Validar existencia de la factura
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return jsonify({"error": "La factura no existe"}), 404

        # Validar método de pago
        allowed_methods = ['CASH', 'CARD', 'TRANSFER']
        if payment_method not in allowed_methods:
            return jsonify({"error": f"payment_method inválido. Valores permitidos: {allowed_methods}"}), 400

        # Validar amount positivo
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            return jsonify({"error": "amount debe ser un número positivo"}), 400

        # Validar paid_at si se envía
        if paid_at:
            try:
                paid_at = datetime.fromisoformat(paid_at)
            except ValueError:
                return jsonify({"error": "paid_at debe ser un formato ISO válido"}), 400

        new_payment = Payment(
            invoice_id=invoice_id,
            amount=amount,
            payment_method=payment_method,
            reference=reference,
            paid_at=paid_at
        )

        db.session.add(new_payment)
        db.session.commit()

        return jsonify({
            "message": "Pago registrado",
            "id": new_payment.id
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# READ ALL – Obtener todos los pagos
def get_all_payments_controller():
    payments = Payment.query.all()

    return jsonify([
        {
            "id": payment.id,
            "invoice_id": payment.invoice_id,
            "amount": float(payment.amount),
            "payment_method": payment.payment_method,
            "reference": payment.reference,
            "paid_at": payment.paid_at.isoformat() if payment.paid_at else None,
            "created_at": payment.created_at.isoformat() if payment.created_at else None,
            "updated_at": payment.updated_at.isoformat() if payment.updated_at else None
        }
        for payment in payments
    ]), 200


# READ BY ID – Obtener pago por ID
def get_payment_by_id_controller(payment_id):
    payment = Payment.query.get(payment_id)

    if not payment:
        return jsonify({"message": "Pago no encontrado"}), 404

    return jsonify({
        "id": payment.id,
        "invoice_id": payment.invoice_id,
        "amount": float(payment.amount),
        "payment_method": payment.payment_method,
        "reference": payment.reference,
        "paid_at": payment.paid_at.isoformat() if payment.paid_at else None,
        "created_at": payment.created_at.isoformat() if payment.created_at else None,
        "updated_at": payment.updated_at.isoformat() if payment.updated_at else None
    }), 200


# UPDATE – Actualizar un pago
def update_payment_controller(payment_id):
    payment = Payment.query.get(payment_id)

    if not payment:
        return jsonify({"message": "Pago no encontrado"}), 404

    data = request.json

    invoice_id = data.get('invoice_id', payment.invoice_id)
    amount = data.get('amount', payment.amount)
    payment_method = data.get('payment_method', payment.payment_method)
    reference = data.get('reference', payment.reference)
    paid_at = data.get('paid_at', payment.paid_at)

    # Validaciones
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return jsonify({"error": "La factura no existe"}), 404

    allowed_methods = ['CASH', 'CARD', 'TRANSFER']
    if payment_method not in allowed_methods:
        return jsonify({"error": f"payment_method inválido. Valores permitidos: {allowed_methods}"}), 400

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        return jsonify({"error": "amount debe ser un número positivo"}), 400

    if paid_at:
        try:
            paid_at = datetime.fromisoformat(paid_at) if isinstance(paid_at, str) else paid_at
        except ValueError:
            return jsonify({"error": "paid_at debe ser un formato ISO válido"}), 400

    payment.invoice_id = invoice_id
    payment.amount = amount
    payment.payment_method = payment_method
    payment.reference = reference
    payment.paid_at = paid_at

    db.session.commit()

    return jsonify({
        "message": "Pago actualizado",
        "id": payment.id
    }), 200


# DELETE – Eliminar un pago
def delete_payment_controller(payment_id):
    payment = Payment.query.get(payment_id)

    if not payment:
        return jsonify({"message": "Pago no encontrado"}), 404

    db.session.delete(payment)
    db.session.commit()

    return jsonify({
        "message": "Pago eliminado"
    }), 200
from flask import jsonify, request
from datetime import datetime
from app import db
from app.models.invoice import Invoice
from app.models.invoice_item import InvoiceItem
from app.models.person import Person
from app.models.insurer import Insurer
# Descomentar cuando exista el modelo de prestaciones
# from app.models.prestation import Prestation


def get_all_invoices_controller():
    invoices = Invoice.query.all()
    return jsonify([i.to_dict() for i in invoices]), 200


def get_invoice_by_id_controller(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return jsonify({"error": "Invoice not found"}), 404

    return jsonify(invoice.to_dict(include_items=True)), 200


def create_invoice_controller():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    required_fields = ["numero", "fechaEmision", "moneda", "items"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # items debe ser una lista no vacía
    if not isinstance(data["items"], list) or not data["items"]:
        return jsonify({"error": "items must be a non-empty list"}), 400

    persona_id = data.get("personaId")
    aseguradora_id = data.get("aseguradoraId")

    if not persona_id and not aseguradora_id:
        return jsonify({"error": "personaId or aseguradoraId is required"}), 400

    if persona_id and aseguradora_id:
        return jsonify({"error": "Only one of personaId or aseguradoraId is allowed"}), 400
    
    # Validar número de factura único
    existing = Invoice.query.filter_by(invoice_number=data["numero"]).first()
    if existing:
        return jsonify({"error": "Invoice number already exists"}), 409

    
    # Validación de fecha
    try:
        issue_date = datetime.strptime(data["fechaEmision"], "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid fechaEmision format (YYYY-MM-DD)"}), 400

    # Validar existencia de persona
    if persona_id:
        person = Person.query.get(persona_id)
        if not person:
            return jsonify({"error": "Persona not found"}), 404

    # Validar existencia de aseguradora
    if aseguradora_id:
        insurer = Insurer.query.get(aseguradora_id)
        if not insurer:
            return jsonify({"error": "Aseguradora not found"}), 404

    # Crear factura
    invoice = Invoice(
        invoice_number=data["numero"],
        issue_date=issue_date,
        patient_id=persona_id,
        insurer_id=aseguradora_id,
        currency=data["moneda"],
        status="PENDING"
    )

    db.session.add(invoice)

    subtotal = 0
    total_tax = 0

    for item in data["items"]:
        quantity = item.get("cantidad")
        unit_price = item.get("valorUnitario")
        tax_amount = item.get("impuestos", 0)
        prestation_id = item.get("prestacionId")

        # Validaciones defensivas
        if quantity is None or quantity <= 0:
            return jsonify({"error": "cantidad must be greater than 0"}), 400

        if unit_price is None or unit_price < 0:
            return jsonify({"error": "valorUnitario must be >= 0"}), 400

        if tax_amount < 0:
            return jsonify({"error": "impuestos must be >= 0"}), 400

        # Descomentar cuando exista el modelo de prestaciones
        # if prestation_id:
        #     prestation = Prestation.query.get(prestation_id)
        #     if not prestation:
        #         return jsonify({
        #             "error": f"Prestacion not found (id: {prestation_id})"
        #         }), 404

        line_subtotal = quantity * unit_price
        line_total = line_subtotal + tax_amount

        invoice_item = InvoiceItem(
            invoice=invoice,
            prestation_id=prestation_id,
            description=item.get("descripcion"),
            quantity=quantity,
            unit_price=unit_price,
            tax_amount=tax_amount,
            total_price=line_total
        )

        subtotal += line_subtotal
        total_tax += tax_amount

        db.session.add(invoice_item)

    invoice.subtotal = subtotal
    invoice.total = subtotal + total_tax

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({
        "error": "Error creating invoice",
        "details": str(e)
        }), 500

    return jsonify({
        "message": "Invoice created successfully",
        "invoice_id": invoice.id,
        "subtotal": invoice.subtotal,
        "total": invoice.total
    }), 201

def update_invoice_status_controller(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return jsonify({"error": "Invoice not found"}), 404

    data = request.get_json()
    new_status = data.get("estado")

    status_map = {
        "pendiente": "PENDING",
        "emitida": "ISSUED",
        "pagada": "PAID",
        "anulada": "CANCELLED"
    }

    if new_status not in status_map:
        return jsonify({"error": "Invalid estado"}), 400

    if invoice.status == "CANCELLED":
        return jsonify({"error": "Cancelled invoices cannot be modified"}), 400

    invoice.status = status_map[new_status]
    db.session.commit()

    return jsonify({
        "message": "Invoice status updated successfully",
        "estado": new_status
    }), 200


def cancel_invoice_controller(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return jsonify({"error": "Invoice not found"}), 404

    invoice.status = "CANCELLED"
    db.session.commit()

    return jsonify({"message": "Invoice cancelled successfully"}), 200
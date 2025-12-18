from flask import jsonify, request
from app.models.invoice import Invoice
from app.models.invoice_item import InvoiceItem
from app import db
from datetime import datetime


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

    required_fields = ["numero", "fechaEmision", "moneda", "items"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    if not data.get("personaId") and not data.get("aseguradoraId"):
        return jsonify({"error": "personaId or aseguradoraId is required"}), 400

    if data.get("personaId") and data.get("aseguradoraId"):
        return jsonify({"error": "Only one of personaId or aseguradoraId is allowed"}), 400

    try:
        issue_date = datetime.strptime(data["fechaEmision"], "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid fechaEmision format (YYYY-MM-DD)"}), 400

    invoice = Invoice(
        invoice_number=data["numero"],
        issue_date=issue_date,
        patient_id=data.get("personaId"),
        insurer_id=data.get("aseguradoraId"),
        currency=data["moneda"],
        status="PENDING"
    )

    db.session.add(invoice)

    subtotal = 0
    total_tax = 0

    for item in data["items"]:
        quantity = item.get("cantidad", 0)
        unit_price = item.get("valorUnitario", 0)
        tax_amount = item.get("impuestos", 0)

        line_subtotal = quantity * unit_price
        line_total = line_subtotal + tax_amount

        invoice_item = InvoiceItem(
            invoice=invoice,
            prestation_id=item.get("prestacionId"),
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

    db.session.commit()

    return jsonify({
        "message": "Invoice created successfully",
        "invoice": invoice.to_dict(include_items=True)
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
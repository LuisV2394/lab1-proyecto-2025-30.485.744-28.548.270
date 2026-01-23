from flask import jsonify, request
from decimal import Decimal,  InvalidOperation
from app.models.invoice_item import InvoiceItem
from app.models.prestation import Prestation
from app.models.invoice import Invoice
from app import db

def get_all_invoice_items_controller():
    items = InvoiceItem.query.all()
    return jsonify([item.to_dict() for item in items]), 200

def get_invoice_item_by_id_controller(item_id):
    item = InvoiceItem.query.get(item_id)
    if not item:
        return jsonify({"error": "Invoice item not found"}), 404

    return jsonify(item.to_dict()), 200

def create_invoice_item_controller():
    data = request.get_json()

    required_fields = ["invoiceId", "descripcion", "cantidad", "valorUnitario"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    invoice = Invoice.query.get(data["invoiceId"])
    if not invoice:
        return jsonify({"error": "Associated invoice not found"}), 404

    quantity = data.get("cantidad", 0)
    unit_price = data.get("valorUnitario", 0)
    tax_amount = data.get("impuestos", 0)
    line_total = quantity * unit_price + tax_amount

    item = InvoiceItem(
        invoice_id=data["invoiceId"],
        prestation_id=data.get("prestacionId"),
        description=data["descripcion"],
        quantity=quantity,
        unit_price=unit_price,
        tax_amount=tax_amount,
        total_price=line_total
    )

    db.session.add(item)

    # Actualizar subtotal y total de la factura
    invoice.subtotal += quantity * unit_price
    invoice.total += line_total
    db.session.commit()

    return jsonify({
        "message": "Invoice item created successfully",
        "item": item.to_dict()
    }), 201

def update_invoice_item_controller(item_id):
    item = InvoiceItem.query.get(item_id)
    if not item:
        return jsonify({"error": "Invoice item not found"}), 404

    data = request.get_json() or {}

    # Validaciones y actualizaciones
    try:
        if "cantidad" in data:
            quantity = Decimal(data["cantidad"])
            if quantity <= 0:
                return jsonify({"error": "Quantity must be greater than 0"}), 400
            item.quantity = quantity

        if "valorUnitario" in data:
            unit_price = Decimal(data["valorUnitario"])
            if unit_price <= 0:
                return jsonify({"error": "Unit price must be greater than 0"}), 400
            item.unit_price = unit_price

        if "impuestos" in data:
            tax_amount = Decimal(data["impuestos"])
            if tax_amount < 0:
                return jsonify({"error": "Tax amount cannot be negative"}), 400
            item.tax_amount = tax_amount

        if "descripcion" in data:
            item.description = str(data["descripcion"])

        if "prestacionId" in data:
            prestation_id = data["prestacionId"]
            prestation = Prestation.query.get(prestation_id)
            if not prestation:
                return jsonify({"error": f"Prestation with id {prestation_id} does not exist"}), 404
            item.prestation_id = prestation_id

    except (InvalidOperation, ValueError):
        return jsonify({"error": "Invalid numeric value provided"}), 400

    # Recalcular total del ítem
    item.total_price = item.quantity * item.unit_price + item.tax_amount

    # Recalcular subtotal y total de la factura
    invoice = item.invoice
    subtotal = sum([i.quantity * i.unit_price for i in invoice.items])
    total_tax = sum([i.tax_amount for i in invoice.items])
    invoice.subtotal = subtotal
    invoice.total = subtotal + total_tax

    db.session.commit()

    return jsonify({
        "message": "Invoice item updated successfully",
        "item": item.to_dict()
    }), 200

def delete_invoice_item_controller(item_id):
    item = InvoiceItem.query.get(item_id)
    if not item:
        return jsonify({"error": "Invoice item not found"}), 404

    invoice = item.invoice

    quantity = Decimal(item.quantity)
    unit_price = Decimal(item.unit_price)
    total_price = Decimal(item.total_price)

    invoice.subtotal -= quantity * unit_price
    invoice.total -= total_price

    if invoice.subtotal < 0:
        invoice.subtotal = Decimal("0.00")
    if invoice.total < 0:
        invoice.total = Decimal("0.00")

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Invoice item deleted successfully"}), 200
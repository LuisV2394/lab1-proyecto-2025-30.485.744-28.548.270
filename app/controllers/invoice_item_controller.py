from flask import jsonify, request
from app.models.invoice_item import InvoiceItem
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

    data = request.get_json()

    if "cantidad" in data:
        item.quantity = data["cantidad"]
    if "valorUnitario" in data:
        item.unit_price = data["valorUnitario"]
    if "impuestos" in data:
        item.tax_amount = data["impuestos"]
    if "descripcion" in data:
        item.description = data["descripcion"]
    if "prestacionId" in data:
        item.prestation_id = data["prestacionId"]

    # Recalcular total
    item.total_price = float(item.quantity) * float(item.unit_price) + float(item.tax_amount)

    # Actualizar subtotal y total de la factura
    invoice = item.invoice
    subtotal = sum([float(i.quantity) * float(i.unit_price) for i in invoice.items])
    total_tax = sum([float(i.tax_amount) for i in invoice.items])
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
    invoice.subtotal -= float(item.quantity) * float(item.unit_price)
    invoice.total -= float(item.total_price)

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Invoice item deleted successfully"}), 200
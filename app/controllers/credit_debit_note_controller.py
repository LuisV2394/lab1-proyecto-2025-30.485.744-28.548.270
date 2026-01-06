from flask import request, jsonify
from datetime import datetime
from app import db
from app.models.credit_debit_note import CreditDebitNote
from app.models.invoice import Invoice

# Get all Credit/Debit Notes
def get_all_credit_debit_notes():
    try:
        notes = CreditDebitNote.query.all()
        return jsonify([note.to_dict() for note in notes]), 200
    except Exception as e:
        return jsonify({"error": "Failed to retrieve notes", "details": str(e)}), 500

# Get a single note by ID
def get_credit_debit_note_by_id(note_id):
    note = CreditDebitNote.query.get(note_id)
    if not note:
        return jsonify({"error": "Note not found"}), 404
    return jsonify(note.to_dict()), 200

# Create a new note
def create_credit_debit_note():
    data = request.get_json() or {}

    factura_id = data.get("factura_id")
    amount = data.get("amount")
    reason = data.get("reason")

    # Validaciones básicas
    if not factura_id:
        return jsonify({"error": "factura_id is required"}), 400
    if amount is None:
        return jsonify({"error": "amount is required"}), 400
    if amount <= 0:
        return jsonify({"error": "amount must be greater than 0"}), 400
    if reason and len(reason) > 255:
        return jsonify({"error": "reason must be at most 255 characters"}), 400

    # Validar que la factura exista
    invoice = Invoice.query.get(factura_id)
    if not invoice:
        return jsonify({"error": "Invoice not found"}), 404

    note = CreditDebitNote(
        factura_id=factura_id,
        amount=amount,
        reason=reason
    )

    try:
        db.session.add(note)
        db.session.commit()
        return jsonify({"message": "Credit/Debit note created successfully", "id": note.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create note", "details": str(e)}), 500

# Update an existing note
def update_credit_debit_note(note_id):
    note = CreditDebitNote.query.get(note_id)
    if not note:
        return jsonify({"error": "Note not found"}), 404

    data = request.get_json() or {}

    amount = data.get("amount")
    reason = data.get("reason")

    if amount is not None:
        if amount <= 0:
            return jsonify({"error": "amount must be greater than 0"}), 400
        note.amount = amount

    if reason is not None:
        if len(reason) > 255:
            return jsonify({"error": "reason must be at most 255 characters"}), 400
        note.reason = reason

    note.updated_at = datetime.utcnow()

    try:
        db.session.commit()
        return jsonify({"message": "Credit/Debit note updated successfully", "id": note.id}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to update note", "details": str(e)}), 500

# Delete a note
def delete_credit_debit_note(note_id):
    note = CreditDebitNote.query.get(note_id)
    if not note:
        return jsonify({"error": "Note not found"}), 404

    try:
        db.session.delete(note)
        db.session.commit()
        return jsonify({"message": "Credit/Debit note deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to delete note", "details": str(e)}), 500
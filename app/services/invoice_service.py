from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_invoice_pdf(invoice, output_dir="invoices"):
    os.makedirs(output_dir, exist_ok=True)

    file_path = f"{output_dir}/invoice_{invoice.id}.pdf"
    c = canvas.Canvas(file_path, pagesize=letter)

    c.drawString(50, 750, f"Factura N° {invoice.id}")
    c.drawString(50, 720, f"Cliente: {invoice.client_name}")
    c.drawString(50, 690, f"Monto Total: ${invoice.total}")

    c.save()
    return file_path
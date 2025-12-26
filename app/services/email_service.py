from datetime import datetime
import os
from app import db
from app.services.invoice_service import generate_invoice_pdf
from app.models.invoice import Invoice
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import base64

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL = os.getenv("SENDGRID_SENDER_EMAIL")


def send_email(recipient: str, subject: str, html_content: str, attachment_path: str = None):
    try:
        message = Mail(
            from_email=SENDER_EMAIL,
            to_emails=recipient,
            subject=subject,
            html_content=html_content
        )

        if attachment_path:
            with open(attachment_path, "rb") as f:
                data = f.read()
                encoded_file = base64.b64encode(data).decode()
            
            attached_file = Attachment(
                FileContent(encoded_file),
                FileName(os.path.basename(attachment_path)),
                FileType("application/pdf"),
                Disposition("attachment")
            )
            message.attachment = attached_file

        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)

        if 200 <= response.status_code < 300:
            return {"success": True}
        else:
            return {"error": f"SendGrid error: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


def send_notification(notification):
    if notification.type.upper() != "EMAIL":
        return

    attachment_path = None

    invoice_id = notification.payload.get("invoice_id") if notification.payload else None
    if invoice_id:
        invoice = Invoice.query.get(invoice_id)
        if invoice:
            attachment_path = generate_invoice_pdf(invoice)

    result = send_email(
        recipient=notification.recipient,
        subject=notification.template,
        html_content=notification.payload.get("message", ""),
        attachment_path=attachment_path
    )

    notification.status = "FAILED" if result.get("error") else "SENT"
    notification.timestamp = datetime.utcnow()
    db.session.commit()
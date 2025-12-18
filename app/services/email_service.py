from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
SENDGRID_SENDER_EMAIL = os.environ.get("SENDGRID_SENDER_EMAIL")

def send_email(recipient, subject, html_content):
    message = Mail(
        from_email=SENDGRID_SENDER_EMAIL,
        to_emails=recipient,
        subject=subject,
        html_content=html_content
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return {
            "status_code": response.status_code,
            "body": response.body,
            "headers": response.headers
        }
    except Exception as e:
        return {"error": str(e)}
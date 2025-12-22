from app import create_app, db
from flask_migrate import Migrate
from app.models.professional import Professional
from app.models.person import Person
from app.models.agenda import Block
from app.models.unit import Unit
from app.models.episodes import Episode
from app.models.note import ClinicalNote
from app.models.insurer import Insurer
from app.models.invoice import Invoice
from app.models.invoice_item import InvoiceItem
from app.models.notification import Notification
from app.models.user import User
from app.models.appointment import Appointment
from app.models.consets import Consent
from app.models.diagnoses import Diagnosis
from app.models.note import ClinicalNote    
from app.models.role import Role
from app.models.user_role import UserRole

app = create_app()
migrate = Migrate(app, db)

# Este diccionario permite que Flask-Migrate detecte los modelos
from flask.cli import FlaskGroup

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
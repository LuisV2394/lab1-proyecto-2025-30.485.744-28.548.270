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
from app.models.consents import Consent
from app.models.diagnoses import Diagnosis
from app.models.role import Role
from app.models.user_role import UserRole
from app.models.afiliation import Affiliation  
from app.models.authorization import Authorization
from app.models.coverage_plans import CoveragePlan
from app.models.credit_debit_note import CreditDebitNote
from app.models.orders import Order
from app.models.order_details import OrderDetail
from app.models.prescription import Prescription, PrescriptionItem
from app.models.payer import Payer
from app.models.payments import Payment
from app.models.result import Result
from app.models.prestation import Prestation
from app.models.clinical_versions import ClinicalVersion
from app.models.access_logs import AccessLog
from app.models.tariff import Tariff

app = create_app()
migrate = Migrate(app, db)

# Este diccionario permite que Flask-Migrate detecte los modelos
from flask.cli import FlaskGroup

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
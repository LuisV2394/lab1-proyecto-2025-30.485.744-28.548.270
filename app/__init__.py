from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
from .swagger_config import init_swagger
import os
from flask import request
from flask_jwt_extended import JWTManager

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    from app.models.professional import Professional
    from app.models.agenda import Block
    from app.models.unit import Unit
    from app.models.episodes import Episode
    from app.models.note import ClinicalNote
    from app.models.diagnoses import Diagnosis
    from app.models.consents import Consent
    from app.models.appointment import Appointment
    from app.models.orders import Order    
    from app.models.user import User
    from app.models.person import Person
    from app.models.prescription import Prescription
    from app.models.result import Result
    from app.models.coverage_plans import CoveragePlan
    from app.models.order_details import OrderDetail
    from app.models.authorization import Authorization
    from app.models.payer import Payer
    from app.models.afiliation import Affiliation

    from app.models.insurer import Insurer
    from app.models.invoice import Invoice
    from app.models.invoice_item import InvoiceItem
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    @app.before_request
    def fix_swagger_authorization_header():
        auth = request.headers.get("Authorization", "")

        if auth and not auth.startswith("Bearer "):
            request.environ["HTTP_AUTHORIZATION"] = "Bearer " + auth
    
    from app.main import main_bp
    app.register_blueprint(main_bp)
    
    try:
        from app.routes.auth_routes import auth_bp
        from app.routes.professionals_routes import professionals_bp
        from app.routes.users_routes import users_bp
        from app.routes.people_routes import people_bp
        from app.routes.agenda_routes import agenda_bp
        from app.routes.units_routes import units_bp
        from app.routes.episodes_routes import episode_bp
        from app.routes.note_routes import note_bp
        from app.routes.diagnosis_routes import diagnosis_bp
        from app.routes.consent_routes import consent_bp
        from app.routes.appointment_routes import appt_bp
        from app.routes.order_routes import orders_bp
        from app.routes.prescription_routes import prescriptions_bp
        from app.routes.prescription_item_routes import prescription_items_bp
        from app.routes.result_routes import results_bp
        from app.routes.coverage_plan_routes import plans_bp
        from app.routes.order_detail_routes import order_details_bp
        from app.routes.authorization_routes import authorization_bp
        from app.routes.affiliations_routes import affiliation_bp
        from app.routes.payment_routes import payments_bp
        from app.routes.credit_debit_note_routes import credit_debit_notes_bp
        
        from app.routes.invoice_routes import invoice_bp
        from app.routes.invoice_item_routes import invoice_item_bp
        from app.routes.notification_routes import notifications_bp
    
        app.register_blueprint(auth_bp)
        app.register_blueprint(professionals_bp)
        app.register_blueprint(users_bp)
        app.register_blueprint(people_bp)
        app.register_blueprint(units_bp)
        app.register_blueprint(episode_bp)
        app.register_blueprint(note_bp)
        app.register_blueprint(diagnosis_bp)
        app.register_blueprint(consent_bp)
        app.register_blueprint(agenda_bp)
        app.register_blueprint(appt_bp)
        app.register_blueprint(orders_bp)
        app.register_blueprint(prescriptions_bp)
        app.register_blueprint(results_bp)
        app.register_blueprint(plans_bp)
        app.register_blueprint(affiliation_bp)
        app.register_blueprint(order_details_bp)
        app.register_blueprint(authorization_bp)
        app.register_blueprint(invoice_bp)
        app.register_blueprint(invoice_item_bp)
        app.register_blueprint(notifications_bp)
        app.register_blueprint(payments_bp)
        app.register_blueprint(credit_debit_notes_bp)
        app.register_blueprint(prescription_items_bp)
        init_swagger(app)
    except Exception as e:
        print(f"Blueprint registration warning: {e}")
    
    # @app.route("/ping")
    # def ping():
    #     return {"status": "ok", "database": app.config["SQLALCHEMY_DATABASE_URI"]}
    
    # print("=== REGISTERED ROUTES ===")
    # for rule in app.url_map.iter_rules():
    #     print(rule)
    # print("==========================")
    
    return app
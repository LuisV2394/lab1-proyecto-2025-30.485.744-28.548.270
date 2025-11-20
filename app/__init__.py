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
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    init_swagger(app)
    @app.before_request
    def fix_swagger_authorization_header():
        auth = request.headers.get("Authorization", "")

        if auth and not auth.startswith("Bearer "):
            request.environ["HTTP_AUTHORIZATION"] = "Bearer " + auth

    try:
        from app.routes.auth_routes import auth_bp
        from app.models.person import Person
        from app.routes.professionals_routes import professionals_bp
        #from app.routes.units_routes import units_bp
    
        app.register_blueprint(auth_bp)
        app.register_blueprint(professionals_bp)
        #app.register_blueprint(units_bp)

    except Exception as e:
        print(f"Blueprint registration warning: {e}")

    
    @app.route("/ping")
    def ping():
        return {"status": "ok", "database": app.config["SQLALCHEMY_DATABASE_URI"]}
    
    print("=== REGISTERED ROUTES ===")
    for rule in app.url_map.iter_rules():
        print(rule)
    print("==========================")
    
    return app
from flasgger import Swagger

def init_swagger(app):
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "Healthcare API",
            "description": "API for managing professionals and medical units",
            "version": "1.0.0"
        },
        "securityDefinitions": {
            "BearerAuth": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: 'Authorization: Bearer {token}'"
            }
        },
        "definitions": {
            "Professional": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "person_id": {"type": "integer"},
                    "registration_number": {"type": "string"},
                    "specialty": {"type": "string"},
                    "sub_specialty": {"type": "string"},
                    "is_active": {"type": "boolean"},
                    "schedule_enabled": {"type": "boolean"},
                    "created_at": {"type": "string"},
                    "updated_at": {"type": "string"}
                },
                "required": ["person_id", "registration_number", "specialty"]
            }
        }
    }

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True
            }
        ],
        "swagger_ui": True,
        "specs_route": "/docs/"
    }

    Swagger(app, template=swagger_template, config=swagger_config)

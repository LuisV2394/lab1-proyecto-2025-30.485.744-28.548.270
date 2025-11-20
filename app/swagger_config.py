from flasgger import Swagger

def init_swagger(app):
    template = {
        "swagger": "2.0",
        "info": {
            "title": "Healthcare API",
            "description": "API documentation for Professionals and Medical Units management.",
            "version": "1.0.0"
        },
        "schemes": ["http"],
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Insert your JWT token here. Example: 'Bearer {token}'"
            }
        },
        "security": [
            {
                "Bearer": []
            }
        ]
    }

    app.config["SWAGGER"] = {
        "title": "Healthcare API",
        "uiversion": 3,
    }

    Swagger(app, template=template)

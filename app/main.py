from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return jsonify({
            "message": "API Médica en ejecución 🚀",
            "status": "ok",
            "version": "1.0.0"
        })

    return app

# Permite ejecutar directamente con: python app/main.py
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
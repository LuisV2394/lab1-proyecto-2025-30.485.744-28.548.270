from app.main import create_app

app = create_app()

# Permite iniciar la app con: python run.py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
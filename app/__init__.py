from flask import Flask
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(Path(__file__).parent.parent / 'project.env')

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-fallback-key')

    from .routes import routes  # ✅ importing the Blueprint
    app.register_blueprint(routes)

    return app

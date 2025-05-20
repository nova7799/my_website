
from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
from pathlib import Path
import os


load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'project.env'))
env_path = Path(__file__).parent.parent / 'project.env'
load_dotenv(env_path)


app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-fallback-key')



from .routes import register_routes
register_routes(app)

env_path = Path(__file__).parent.parent / 'project.env'
load_dotenv(env_path)

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-fallback-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import routes after db is initialized
    from .routes import register_routes
    register_routes(app)

    return app


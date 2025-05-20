from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
import os

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'project.env'))
env_path = Path(__file__).parent.parent / 'project.env'
load_dotenv(env_path)


app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-fallback-key')



from .routes import register_routes
register_routes(app)

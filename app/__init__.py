# from flask import Flask
# from dotenv import load_dotenv
# from pathlib import Path
# import os

# # Load environment variables
# load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'project.env'))
# env_path = Path(__file__).parent.parent / 'project.env'
# load_dotenv(env_path)


# app = Flask(__name__)
# app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-fallback-key')



# from .routes import register_routes
# register_routes(app)


# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from pathlib import Path
import os

# Load environment variables
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

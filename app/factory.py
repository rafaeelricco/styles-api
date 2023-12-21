import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)


# Create Flask app and register blueprints
def create_app():
    app = Flask(__name__)

    from app.api.base import api_todos

    app.register_blueprint(api_todos)

    return app

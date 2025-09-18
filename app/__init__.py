from flask import Flask
from .routes import main_bp
import os


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Config
    env = os.environ.get("FLASK_ENV", "development")
    try:
        from config import config_by_name  # type: ignore
    except Exception:
        # Fallback if run in a different package context
        from ..config import config_by_name  # type: ignore
    app.config.from_object(config_by_name.get(env, config_by_name["development"]))

    # Blueprints
    app.register_blueprint(main_bp)

    return app



"""
Flask application factory module.

This module contains the `create_app` function, which is responsible for creating
and configuring the Flask application instance. The function performs the following
tasks:

- Initializes the Flask application.
- Creates the instance folder if it doesn't exist.
- Configures the application settings.
- Registers the views (blueprints).
- Registers the context processors.

The `create_app` function returns the configured Flask application instance, which
can then be used to run the application or perform additional setup tasks.
"""

import os
from flask import Flask
from app.routes import routes
from app.config import get_config
from app.context_processors import context_processors


def create_app() -> Flask:
    """Create and configure the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(get_config().flask.model_dump(mode="json"))

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    configure_app(app)
    register_blueprints(app)
    register_context_processors(app)

    return app


def configure_app(app: Flask) -> None:
    """Configure the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    app.static_folder = os.path.join(app.root_path, "static")
    app.template_folder = os.path.join(app.root_path, "templates")


def register_blueprints(app: Flask) -> None:
    """Register the views (blueprints) with the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    app.register_blueprint(routes.bp)


def register_context_processors(app: Flask) -> None:
    """Register the context processors with the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    app.context_processor(context_processors.common_settings)

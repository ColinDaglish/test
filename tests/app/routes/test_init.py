import os
import pytest

from flask import Flask, Blueprint
from app import create_app, configure_app, register_blueprints


@pytest.fixture
def app():
    """Create a temporary instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    yield app


def test_create_app():
    """Test the create_app function."""
    app = create_app()
    assert isinstance(app, Flask)


def test_configure_app(app):
    """Test the configure_app function."""
    configure_app(app)
    assert app.static_folder == os.path.join(app.root_path, "static")
    assert app.template_folder == os.path.join(app.root_path, "templates")


def test_register_blueprints(app):
    """Test the register_blueprints function."""
    test_blueprint = Blueprint("test_blueprint", __name__)
    app.register_blueprint(test_blueprint)
    register_blueprints(app)
    assert "test_blueprint" in app.blueprints

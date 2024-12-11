import unittest
from app.config.flask import FlaskConfig


class TestFlaskConfig(unittest.TestCase):
    def setUp(self):
        self.config = FlaskConfig()

    def test_attributes_exist(self):
        expected_attributes = [
            "model_config",
            "DEBUG",
            "SECRET_KEY",
            "SESSION_COOKIE_HTTPONLY",
            "SESSION_COOKIE_SECURE",
            "SESSION_COOKIE_SAMESITE",
            "PERMANENT_SESSION_LIFETIME",
        ]

        for attr in expected_attributes:
            self.assertTrue(
                hasattr(self.config, attr),
                f"Attribute '{attr}' does not exist in AppConfig",
            )

import unittest
from app.config.app import AppConfig


class TestAppConfig(unittest.TestCase):
    def setUp(self):
        self.config = AppConfig()

    def test_attributes_exist(self):
        expected_attributes = [
            "model_config",
            "ENVIRONMENT",
            "ORGANISATION_NAME",
            "SERVICE_NAME",
            "DEVELOPER_CONTACT",
            "environment_lower",
        ]

        for attr in expected_attributes:
            self.assertTrue(
                hasattr(self.config, attr),
                f"Attribute '{attr}' does not exist in AppConfig",
            )

    def test_environment_lower(self):
        ENVIRONMENT = self.config.ENVIRONMENT
        self.assertEqual(self.config.environment_lower, ENVIRONMENT.lower())

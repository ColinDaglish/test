import unittest
from unittest.mock import patch, Mock
from app.config.core import get_config
from app.context_processors.context_processors import common_settings


class TestCommonSettings(unittest.TestCase):
    @patch("app.context_processors.context_processors.get_config")
    def test_common_settings(self, mock_get_config):
        get_config.cache_clear()
        # Create a mock Config instance and set the mocked AppConfig instance
        mock_config = Mock()
        mock_config.app.environment_lower = "test"
        mock_config.app.ORGANISATION_NAME = "Test Org"
        mock_config.app.SERVICE_NAME = "Test Service"
        mock_config.app.DEVELOPER_CONTACT = "test@example.com"

        mock_get_config.return_value = mock_config
        result = common_settings()

        # Assert the returned values
        self.assertEqual(result["environment"], "test")
        self.assertEqual(result["org_name"], "Test Org")
        self.assertEqual(result["service_name"], "Test Service")
        self.assertEqual(result["developer_contact"], "test@example.com")

import unittest
from app.config.core import Config, get_config
from app.config.flask import FlaskConfig
from app.config.app import AppConfig


class TestConfig(unittest.TestCase):
    def test_config_class(self):
        """Test that the Config class has the expected attributes"""
        config = Config()
        self.assertTrue(hasattr(config, "model_config"))
        self.assertTrue(hasattr(config, "app"))
        self.assertTrue(hasattr(config, "flask"))

    def test_get_config_function(self):
        """Test that the get_config function returns an instance of Config"""
        config = get_config()
        self.assertIsInstance(config, Config)

    def test_get_config_caching(self):
        """Test that the get_config function caches the instance"""
        config1 = get_config()
        config2 = get_config()
        self.assertIs(config1, config2)

    def test_config_instances(self):
        """Test that the Config instance has instances of AppConfig and FlaskConfig"""
        config = Config()
        self.assertIsInstance(config.app, AppConfig)
        self.assertIsInstance(config.flask, FlaskConfig)


if __name__ == "__main__":
    unittest.main()

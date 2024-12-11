"""
Configuration module for the application.

This module provides a centralized way to manage and access the application's
configuration settings. It combines the application-specific settings from the
AppConfig class and the Flask-specific settings from the FlaskConfig class into
a single Config object.

The `get_config` function is exposed as the public interface for obtaining a
cached instance of the Config object.
"""

from app.config.core import get_config

__all__ = [
    "get_config",
]

"""This module combines the app and flask configs into one config"""

from functools import lru_cache
from pydantic import BaseModel, ConfigDict
from app.config.app import AppConfig
from app.config.flask import FlaskConfig


class Config(BaseModel):
    """
    Configuration class that combines application and Flask configurations.

    This class inherits from Pydantic's BaseModel and provides a combined
    configuration object that includes both application-specific settings
    (from AppConfig) and Flask-specific settings (from FlaskConfig).

    Attributes:
        model_config (ConfigDict): Configuration for the Pydantic model.
        app (AppConfig): An instance of the AppConfig class.
        flask (FlaskConfig): An instance of the FlaskConfig class.
    """

    model_config = ConfigDict(case_sensitive=True, extra="ignore")

    app: AppConfig = AppConfig()
    flask: FlaskConfig = FlaskConfig()


@lru_cache
def get_config() -> Config:
    """
    Function to get a cached instance of the Config class.

    This function creates an instance of the Config class and caches it
    using the lru_cache decorator from the functools module. Subsequent
    calls to this function will return the cached instance.

    Returns:
        Config: An instance of the Config class.
    """
    return Config()

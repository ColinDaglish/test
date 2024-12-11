"""Module containing the custom configuration settings for the application.
This is different to the FlaskConfig which is designed to only accept built-in flask attributes."""

import pathlib
from functools import cached_property
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    """
    Class to hold base configuration settings for the application. These values can be overridden by environment
    variables. This is different to the FlaskConfig which is designed to only accept built-in flask attributes.

    Attributes:
        model_config (SettingsConfigDict): Configuration for the Pydantic model.
        ENVIRONMENT (str): The environment in which the application is running (e.g. 'local', 'development', 'production').
        ORGANISATION_NAME (str): The name of the organisation running the application.
        SERVICE_NAME (str): The name of the service or application.
        DEVELOPER_CONTACT (str): Email contact information for your development team
    """

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=pathlib.Path(__file__).resolve().parent.parent.parent.joinpath(".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    ENVIRONMENT: str = "local"
    ORGANISATION_NAME: str = "ONS"
    SERVICE_NAME: str = "Flask template app"
    DEVELOPER_CONTACT: str = "your_developer_team@ons.gov.uk"

    @computed_field
    @cached_property
    def environment_lower(self) -> str:
        return self.ENVIRONMENT.lower()

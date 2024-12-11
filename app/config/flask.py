"""Module containing the Flask configuration settings for the application.
This is different to the AppConfig which is designed for broader array of configuration settings"""

import pathlib
from pydantic import SecretStr, field_serializer
from pydantic_settings import BaseSettings, SettingsConfigDict


# https://flask.palletsprojects.com/en/3.0.x/config/#builtin-configuration-values
class FlaskConfig(BaseSettings):
    """
    Configuration settings for a Flask application.

    This class inherits from Pydantic's BaseSettings and provides configuration
    options specific to Flask applications. The configuration values are loaded
    from environment variables with the prefix "FLASK_".

    Note: The SECRET_KEY attribute is serialized to its plain text value when
    the configuration is serialized to JSON. This behavior is controlled by the
    `dump_secret_key` field serializer.

    Attributes:
        model_config (SettingsConfigDict): Configuration for the Pydantic model.
        DEBUG (bool): Whether to run the Flask application in debug mode.
        SECRET_KEY (SecretStr): A secret key used for cryptographic operations in Flask.
        SESSION_COOKIE_HTTPONLY (bool): Whether to set the HttpOnly flag on session cookies.
        SESSION_COOKIE_SECURE (bool): Whether to set the Secure flag on session cookies.
        SESSION_COOKIE_SAMESITE (str): The SameSite policy for session cookies.
        PERMANENT_SESSION_LIFETIME (int): The lifetime of permanent sessions in seconds.
    """

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=pathlib.Path(__file__).resolve().parent.parent.parent.joinpath(".env"),
        env_file_encoding="utf-8",
        env_prefix="FLASK_",
        extra="ignore",
    )

    DEBUG: bool = True
    SECRET_KEY: SecretStr = SecretStr(
        "fake-key-f985bd5e2e34feb60c7c0823eab3c7e2d5ce41aaa2f948edaf36916359b65a3d"
    )

    SESSION_COOKIE_HTTPONLY: bool = True
    SESSION_COOKIE_SECURE: bool = False
    SESSION_COOKIE_SAMESITE: str = "Strict"
    PERMANENT_SESSION_LIFETIME: int = 1209600  # 2 weeks in seconds

    @field_serializer("SECRET_KEY", when_used="json")
    def dump_secret_key(self, secret_key: SecretStr):
        """
        Field serializer for the SECRET_KEY attribute.

        This method is used to serialize the SECRET_KEY attribute when the
        configuration is serialized to JSON. It returns the plain text value
        of the secret key.

        Args:
            secret_key (SecretStr): The SecretStr instance containing the secret key.

        Returns:
            str: The plain text value of the secret key.
        """
        return secret_key.get_secret_value()

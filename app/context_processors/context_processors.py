"""This module contains context processor functions that inject data into the
template context for use in Jinja templates. Context processors are automatically
called when rendering a template, and their return values are merged into the
template context.
"""

from app.config.core import get_config


def common_settings() -> dict:
    """
    Context processor function to inject common settings into the template context.

    This function retrieves the application configuration from the `get_config` function
    and creates a dictionary with common settings that can be accessed in templates.

    Returns:
        dict: A dictionary containing the following common settings:
            - environment (str): The environment in which the application is running (lowercase).
            - org_name (str): The name of the organization who developed the application.
            - service_name (str): The name of the service or application.
            - developer_contact(str): The central email address contact of your development team.
    """
    config = get_config()
    return dict(
        environment=config.app.environment_lower,
        org_name=config.app.ORGANISATION_NAME,
        service_name=config.app.SERVICE_NAME,
        developer_contact=config.app.DEVELOPER_CONTACT,
    )

from django.apps import AppConfig


class SeaConfig(AppConfig):
    """
    Configuration of the sea app
    Defines size of id field on app model with default_auto_field
    Defines the name of the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sea'

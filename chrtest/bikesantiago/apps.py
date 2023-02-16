from django.apps import AppConfig


class BikesantiagoConfig(AppConfig):
    """
    Configuration of the bikesantiago app
    Defines size of id field on app model with default_auto_field
    Defines the name of the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bikesantiago'

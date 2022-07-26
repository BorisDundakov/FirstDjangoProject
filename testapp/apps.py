from django.apps import AppConfig


class TestappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testapp'

# it is where the app will the configured (misleading name)

from django.apps import AppConfig


class PeruExpAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'peru_exp_app'

    def ready(self):
        import peru_exp_app.signals

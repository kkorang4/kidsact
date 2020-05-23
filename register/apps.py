from django.apps import AppConfig


class RegistersConfig(AppConfig):
    name = 'register'

    def ready(self):
        import register.signals

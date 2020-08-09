from django.apps import AppConfig


class IflameConfig(AppConfig):
    name = 'iflame'

    def ready(self):
        import iflame.signals

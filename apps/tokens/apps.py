from django.apps import AppConfig


class TokenAppConfig(AppConfig):
    name = 'apps.tokens'
    label = 'tokens'

    def ready(self):
        import apps.tokens.receivers

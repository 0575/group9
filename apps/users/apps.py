from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'apps.users'

    def ready(self):
        import users.signals
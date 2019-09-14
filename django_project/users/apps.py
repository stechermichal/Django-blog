from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #method imports signals to avoid trouble with imports
    def ready(self):
        import users.signals

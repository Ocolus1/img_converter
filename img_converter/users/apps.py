from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "img_converter.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import img_converter.users.signals  # noqa F401
        except ImportError:
            pass

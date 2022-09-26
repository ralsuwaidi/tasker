from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TasksConfig(AppConfig):
    name = "tasker.tasks"
    verbose_name = _("Tasks")

    def ready(self):
        try:
            import tasker.tasks.signals  # noqa F401
        except ImportError:
            pass

from django.apps import AppConfig


class RobotConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "robot"
    verbose_name = "Bot"

    def ready(self):
        import robot.signals

from enums.colors import Colors
from views.components.notification import Notification


class NotificationFactory:

    @staticmethod
    def success(message: str) -> Notification:
        return Notification(
            message=message,
            bgcolor=Colors.GREEN.value
        )

    @staticmethod
    def error(message: str) -> Notification:
        return Notification(
            message=message,
            bgcolor=Colors.RED.value
        )

    @staticmethod
    def warning(message: str) -> Notification:
        return Notification(
            message=message,
            bgcolor=Colors.ORANGE.value
        )

    @staticmethod
    def info(message: str) -> Notification:
        return Notification(
            message=message,
            bgcolor=Colors.CYAN.value
        )

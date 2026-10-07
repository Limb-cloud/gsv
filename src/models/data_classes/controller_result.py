from dataclasses import dataclass

from views.components.notification import Notification


@dataclass
class ControllerResult[T]:
    data: T | None = None
    notification: Notification | None = None
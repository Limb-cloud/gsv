from dataclasses import field

import flet as ft
from flet import SnackBar

from enums.colors import Colors


@ft.control
class Notification(SnackBar):

    message: str = ""

    content: ft.Control = field(
        default_factory=lambda: ft.Text("")
    )

    def init(self):
        self.content = ft.Text(
            self.message,
            color=Colors.TEXT_PRIMARY.value,
        )
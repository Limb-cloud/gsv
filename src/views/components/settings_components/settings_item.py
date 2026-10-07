import flet as ft

from enums.colors import Colors


@ft.control
class SettingsItem(ft.Row):

    title: str = ""
    value: str = ""

    def init(self):
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN

        self.controls = [
            ft.Text(
                self.title,
                size=13,
                color=Colors.TEXT_SECONDARY.value,
            ),

            ft.Text(
                self.value,
                size=13,
                weight=ft.FontWeight.W_600,
                color=Colors.TEXT_PRIMARY.value,
            ),
        ]
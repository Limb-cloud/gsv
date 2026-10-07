import flet as ft

from enums.colors import Colors


@ft.control
class SidebarFooter(ft.Column):

    def init(self):
        self.spacing = 2

        self.controls = [
            ft.Text(
                "Game Settings Vault",
                size=11,
                color=Colors.TEXT_SECONDARY.value,
            ),

            ft.Text(
                "v1.0.0",
                size=11,
                color=Colors.TEXT_SECONDARY.value,
            )
        ]
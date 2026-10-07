import flet as ft
from flet import Row

from enums.colors import Colors
from enums.paths import Paths


@ft.control
class Logo(Row):

    def init(self):
        self.spacing = 10
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER

        self.controls = [
            ft.Container(
                width=50,
                height=50,
                alignment=ft.Alignment.CENTER,
                content=ft.Image(
                    src=Paths.APPLICATION_ICON.value,
                    width=50,
                    height=50,
                    fit=ft.BoxFit.CONTAIN
                )
            ),

            ft.Column(
                spacing=0,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "Game",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=Colors.TEXT_PRIMARY.value
                    ),

                    ft.Text(
                        "Settings Vault",
                        size=11,
                        color=Colors.TEXT_SECONDARY.value
                    )
                ]
            )
        ]
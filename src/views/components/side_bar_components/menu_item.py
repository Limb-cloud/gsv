import flet as ft
from flet import Container

from enums.colors import Colors


@ft.control
class MenuItem(Container):

    title: str = ""
    icon: str | None = None
    selected_index: bool = False

    def init(self):
        self.height = 48
        self.border_radius = 10
        self.padding = ft.Padding.symmetric(
            horizontal=14
        )

        self.bgcolor = (
            Colors.SURFACE.value
            if self.selected_index
            else None
        )

        self.on_click = self.on_click

        self.content = ft.Row(
            spacing=12,
            controls=[
                ft.Icon(
                    self.icon,
                    size=20,
                    color=(
                        Colors.PURPLE.value
                        if self.selected_index
                        else Colors.TEXT_SECONDARY.value
                    ),
                ),

                ft.Text(
                    self.title,
                    size=14,
                    weight=(
                        ft.FontWeight.W_600
                        if self.selected_index
                        else ft.FontWeight.NORMAL
                    ),
                    color=(
                        Colors.TEXT_PRIMARY.value
                        if self.selected_index
                        else Colors.TEXT_SECONDARY.value
                    ),
                ),
            ],
        )
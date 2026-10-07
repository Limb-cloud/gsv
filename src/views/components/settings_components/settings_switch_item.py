from typing import Callable

import flet as ft

from enums.colors import Colors


@ft.control
class SettingsSwitchItem(ft.Row):

    title: str = ""
    subtitle: str = ""
    value: bool = False

    on_change: Callable | None = None

    def init(self):
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN

        self.switch = ft.Switch(
            value=self.value,
            active_color=Colors.PURPLE.value,
            on_change=self._on_change,
        )

        self.controls = [
            ft.Column(
                spacing=2,
                controls=[
                    ft.Text(
                        self.title,
                        size=14,
                        color=Colors.TEXT_PRIMARY.value,
                    ),

                    ft.Text(
                        self.subtitle,
                        size=12,
                        color=Colors.TEXT_SECONDARY.value,
                    ),
                ],
            ),

            self.switch,
        ]

    def _on_change(self, e):
        self.value = self.switch.value

        if self.on_change:
            self.on_change(e)
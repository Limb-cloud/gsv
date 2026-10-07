from dataclasses import field

import flet as ft

from enums.colors import Colors


@ft.control
class SettingsSection(ft.Container):

    title: str = ""
    section_icon: ft.IconData | None = None
    section_controls: list[ft.Control] = field(
        default_factory=list
    )

    def init(self):
        self.padding = 18
        self.border_radius = 14
        self.bgcolor = Colors.SURFACE.value

        self.border = ft.Border.all(
            1,
            Colors.BORDER.value,
        )

        self.content = ft.Column(
            spacing=14,
            controls=[
                ft.Row(
                    spacing=8,
                    controls=[
                        ft.Icon(
                            self.section_icon,
                            size=19,
                            color=Colors.PURPLE.value,
                        ),

                        ft.Text(
                            self.title,
                            size=16,
                            weight=ft.FontWeight.W_600,
                            color=Colors.TEXT_PRIMARY.value,
                        ),
                    ],
                ),

                ft.Divider(
                    height=1,
                    color=Colors.BORDER.value,
                ),

                *self.section_controls,
            ],
        )
from dataclasses import field

import flet as ft

from enums.colors import Colors


@ft.control
class PresetSection(ft.Container):

    title: str = ""
    section_icon: ft.IconData | None = None
    section_content: ft.Control = field(
        default_factory=ft.Container
    )

    def init(self):
        self.padding = 16
        self.border_radius = 12
        self.bgcolor = Colors.BACKGROUND.value

        self.border = ft.Border.all(
            1,
            Colors.BORDER.value,
        )

        self.content = ft.Column(
            spacing=12,
            controls=[
                ft.Row(
                    spacing=8,
                    controls=[
                        ft.Icon(
                            self.section_icon,
                            size=18,
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

                self.section_content,
            ],
        )
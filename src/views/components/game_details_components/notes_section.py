import flet as ft

from enums.colors import Colors


@ft.control
class NotesSection(ft.Container):

    notes: str = ""

    def init(self):
        self.padding = 18
        self.border_radius = 14
        self.bgcolor = Colors.SURFACE.value

        self.border = ft.Border.all(
            1,
            Colors.BORDER.value,
        )

        self.content = ft.Column(
            spacing=10,
            controls=[
                ft.Row(
                    spacing=8,
                    controls=[
                        ft.Icon(
                            ft.Icons.NOTES_ROUNDED,
                            size=19,
                            color=Colors.PURPLE.value,
                        ),

                        ft.Text(
                            "Заметки",
                            size=16,
                            weight=ft.FontWeight.W_600,
                            color=Colors.TEXT_PRIMARY.value,
                        ),
                    ],
                ),

                ft.Text(
                    self.notes,
                    size=13,
                    color=Colors.TEXT_SECONDARY.value,
                )
            ]
        )
import flet as ft

from enums.colors import Colors


@ft.control
class TextField(ft.TextField):

    def init(self):
        self.bgcolor = Colors.SURFACE.value
        self.color = Colors.TEXT_PRIMARY.value

        self.border = {
            ft.ControlState.DEFAULT: ft.OutlineInputBorder(
                border_radius=10,
                side=ft.BorderSide(
                    width=1,
                    color=Colors.BORDER.value,
                ),
            ),

            ft.ControlState.FOCUSED: ft.OutlineInputBorder(
                border_radius=10,
                side=ft.BorderSide(
                    width=2,
                    color=Colors.PURPLE.value,
                )
            )
        }
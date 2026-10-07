import flet as ft

from enums.colors import Colors


@ft.control
class GameInfoItem(ft.Row):

    item_icon: ft.IconData | None = None
    text: str = ""
    item_color: str = ""

    def init(self):
        self.spacing = 6

        self.controls = [
            ft.Icon(
                self.item_icon,
                size=17,
                color=self.item_color,
            ),

            ft.Text(
                self.text,
                size=13,
                color=Colors.TEXT_SECONDARY.value,
            ),
        ]
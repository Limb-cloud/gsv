import flet as ft

from enums.colors import Colors


@ft.control
class GameCardStat(ft.Row):

    stat_icon: str | None = None
    value: str = ""

    def init(self):
        self.spacing = 5

        self.controls = [
            ft.Icon(
                self.stat_icon,
                size=15,
                color=Colors.CYAN.value,
            ),

            ft.Text(
                self.value,
                size=12,
                color=Colors.TEXT_SECONDARY.value,
            ),
        ]
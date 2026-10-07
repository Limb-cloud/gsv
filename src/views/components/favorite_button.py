from typing import Callable

import flet as ft

from enums.colors import Colors


@ft.control
class FavoriteButton(ft.IconButton):

    is_favorite: bool = False
    on_favorite_click: Callable | None = None

    def init(self):
        self.icon = (
            ft.Icons.FAVORITE
            if self.is_favorite
            else ft.Icons.FAVORITE_BORDER
        )

        self.icon_color = (
            Colors.PINK.value
            if self.is_favorite
            else Colors.TEXT_PRIMARY.value
        )

        self.bgcolor = Colors.BACKGROUND.value
        self.on_click = self.on_favorite_click
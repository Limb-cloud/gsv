from typing import Callable

import flet as ft

from enums.colors import Colors
from views.components.favorite_button import FavoriteButton


@ft.control
class GameDetailsHeader(ft.Row):

    game_name: str = ""
    is_favorite: bool = False
    on_back: Callable | None = None
    on_favorite: Callable | None = None

    def init(self):
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN

        self.controls = [
            ft.Row(
                spacing=12,
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK_ROUNDED,
                        icon_color=Colors.TEXT_PRIMARY.value,
                        tooltip="Назад",
                        on_click=self.on_back,
                    ),

                    ft.Column(
                        spacing=2,
                        controls=[
                            ft.Text(
                                self.game_name,
                                size=28,
                                weight=ft.FontWeight.BOLD,
                                color=Colors.TEXT_PRIMARY.value
                            ),

                            ft.Text(
                                "Настройки игры",
                                size=13,
                                color=Colors.TEXT_SECONDARY.value
                            )
                        ]
                    )
                ]
            ),

            FavoriteButton(
                is_favorite=self.is_favorite,
                on_favorite_click=self.on_favorite
            )
        ]
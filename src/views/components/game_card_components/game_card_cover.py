from typing import Callable

import flet as ft

from views.components.favorite_button import FavoriteButton


@ft.control
class GameCardCover(ft.Container):

    cover_path: str = ""
    is_favorite: bool = False
    on_favorite_click: Callable | None = None

    def init(self):
        self.height = 180

        self.content = ft.Stack(
            controls=[
                ft.Image(
                    src=self.cover_path,
                    width=float("inf"),
                    height=180,
                    fit=ft.BoxFit.CONTAIN,
                ),

                ft.Container(
                    right=10,
                    top=10,
                    content=FavoriteButton(
                        is_favorite=self.is_favorite,
                        on_favorite_click=self.on_favorite_click,
                    )
                )
            ]
        )
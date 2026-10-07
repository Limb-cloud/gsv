from typing import Callable

import flet as ft

from enums.colors import Colors
from views.components.game_card_components.game_form import GameForm


@ft.control
class GameDialog(ft.AlertDialog):

    on_save: Callable | None = None
    on_cancel: Callable | None = None

    def init(self):
        self.form = GameForm()

        self.modal = True

        self.title = ft.Text(
            "Добавить игру",
            size=22,
            weight=ft.FontWeight.BOLD,
            color=Colors.TEXT_PRIMARY.value,
        )

        self.content = ft.Container(
            width=500,
            content=self.form,
        )

        self.actions = [
            ft.TextButton(
                "Отмена",
                on_click=self.on_cancel,
            ),

            ft.Button(
                content="Добавить",
                icon=ft.Icons.ADD_ROUNDED,
                bgcolor=Colors.PURPLE.value,
                color=Colors.BACKGROUND.value,
                on_click=self.on_save,
            ),
        ]

        self.actions_alignment = (
            ft.MainAxisAlignment.END
        )
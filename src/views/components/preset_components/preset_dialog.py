from typing import Callable

import flet as ft

from enums.colors import Colors
from views.components.preset_components.preset_form import PresetForm


@ft.control
class PresetDialog(ft.AlertDialog):

    on_save: Callable | None = None
    on_cancel: Callable | None = None

    def init(self):
        self.form = PresetForm()

        self.modal = True

        self.title = ft.Text(
            "Добавить пресет",
            size=22,
            weight=ft.FontWeight.BOLD,
            color=Colors.TEXT_PRIMARY.value,
        )

        self.content = ft.Container(
            width=420,
            height=720,
            border_radius=10,
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

        self.actions_alignment = ft.MainAxisAlignment.END
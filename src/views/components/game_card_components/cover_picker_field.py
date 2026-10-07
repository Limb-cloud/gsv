from typing import Callable

import flet as ft

from views.components.text_field import TextField


@ft.control
class CoverPickerField(ft.Row):

    on_select: Callable | None = None

    def init(self):
        self.spacing = 8
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER

        self.cover_field = TextField(
            label="Обложка",
            hint_text="Путь к изображению",
            read_only=True,
            expand=True,
            width=420
        )

        self.controls = [
            self.cover_field,

            ft.IconButton(
                icon=ft.Icons.FOLDER_OPEN_ROUNDED,
                tooltip="Выбрать изображение",
                on_click=self.on_select
            )
        ]

    @property
    def cover_value(self) -> str:
        return self.cover_field.value or ""

    @cover_value.setter
    def cover_value(self, value: str):
        self.cover_field.value = value
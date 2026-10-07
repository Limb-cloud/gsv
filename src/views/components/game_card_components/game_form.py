import flet as ft

from views.components.text_field import TextField
from views.components.game_card_components.cover_picker_field import (
    CoverPickerField,
)


@ft.control
class GameForm(ft.Column):

    def init(self):
        self.tight = True
        self.spacing = 16
        self.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

        self.name_field = TextField(
            label="Название игры *",
            hint_text="Например, Cyberpunk 2077",
            autofocus=True,

        )

        self.description_field = TextField(
            label="Описание",
            hint_text="Краткое описание игры",
            multiline=True,
            min_lines=3,
            max_lines=5,
        )

        self.cover_picker = CoverPickerField(
            on_select=self._select_cover,
        )

        self.favorite_checkbox = ft.Checkbox(
            label="Добавить в избранное",
            value=False,
        )

        self.controls = [
            self.name_field,
            self.description_field,
            self.cover_picker,
            self.favorite_checkbox,
        ]

    def _select_cover(self, e):
        print("Выбрать обложку")

    def validate(self) -> bool:
        if not self.name_field.value.strip():
            self.name_field.error = "Обязательное поле"
            self.name_field.update()

            return False

        self.name_field.error = None
        self.name_field.update()

        return True
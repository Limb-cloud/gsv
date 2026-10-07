import flet as ft

from views.components.text_field import TextField


@ft.control
class DisplaySettingsForm(ft.Column):

    def init(self):
        self.spacing = 12
        self.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

        self.resolution_field = TextField(
            label="Разрешение",
            hint_text="2560x1440",
        )

        self.display_mode_field = TextField(
            label="Режим экрана",
            hint_text="Fullscreen",
        )

        self.refresh_rate_field = TextField(
            label="Частота обновления",
            hint_text="240",
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        self.fps_limit_field = TextField(
            label="Ограничение FPS",
            hint_text="90",
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        self.controls = [
            self.resolution_field,
            self.display_mode_field,
            self.refresh_rate_field,
            self.fps_limit_field,
        ]
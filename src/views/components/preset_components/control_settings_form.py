import flet as ft

from views.components.text_field import TextField


@ft.control
class ControlSettingsForm(ft.Column):

    def init(self):
        self.spacing = 12
        self.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

        self.dpi_field = TextField(
            label="DPI",
            hint_text="800",
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        self.sensitivity_field = TextField(
            label="Чувствительность",
            hint_text="1.25",
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        self.fov_field = TextField(
            label="FOV",
            hint_text="100",
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        self.controls = [
            self.dpi_field,
            self.sensitivity_field,
            self.fov_field,
        ]
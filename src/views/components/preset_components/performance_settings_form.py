import flet as ft

from views.components.text_field import TextField


@ft.control
class PerformanceSettingsForm(ft.Column):

    def init(self):
        self.spacing = 12
        self.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

        self.average_fps_field = TextField(
            label="Средний FPS",
            hint_text="94",
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        self.gpu_temperature_field = TextField(
            label="Температура GPU",
            hint_text="67",
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        self.cpu_temperature_field = TextField(
            label="Температура CPU",
            hint_text="58",
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        self.controls = [
            self.average_fps_field,
            self.gpu_temperature_field,
            self.cpu_temperature_field,
        ]
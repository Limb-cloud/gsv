import flet as ft

from views.components.text_field import TextField


@ft.control
class GraphicsSettingsForm(ft.Column):

    def init(self):
        self.spacing = 12
        self.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

        self.preset_field = TextField(
            label="Графический пресет",
            hint_text="High",
        )

        self.textures_field = TextField(
            label="Текстуры",
            hint_text="Ultra",
        )

        self.shadows_field = TextField(
            label="Тени",
            hint_text="Medium",
        )

        self.ray_tracing_field = TextField(
            label="Ray Tracing",
            hint_text="Off",
        )

        self.upscaler_field = TextField(
            label="Upscaler",
            hint_text="DLSS Quality",
        )

        self.controls = [
            self.preset_field,
            self.textures_field,
            self.shadows_field,
            self.ray_tracing_field,
            self.upscaler_field,
        ]
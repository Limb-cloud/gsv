import flet as ft

from views.components.text_field import TextField
from views.components.preset_components.preset_section import PresetSection

from views.components.preset_components.display_settings_form import DisplaySettingsForm
from views.components.preset_components.graphics_settings_form import GraphicsSettingsForm
from views.components.preset_components.control_settings_form import ControlSettingsForm
from views.components.preset_components.performance_settings_form import PerformanceSettingsForm


@ft.control
class PresetForm(ft.Column):

    def init(self):
        self.width = 420
        self.spacing = 10
        self.scroll = ft.ScrollMode.AUTO
        self.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

        self.name_field = TextField(
            label="Название пресета *",
            hint_text="Например, Balanced",
            autofocus=True,
        )

        self.display_form = DisplaySettingsForm()
        self.graphics_form = GraphicsSettingsForm()
        self.control_form = ControlSettingsForm()
        self.performance_form = PerformanceSettingsForm()

        self.notes_field = TextField(
            label="Заметки",
            hint_text="Дополнительная информация...",
            multiline=True,
            min_lines=3,
            max_lines=5,
        )

        self.controls = [
            self.name_field,

            PresetSection(
                title="Экран",
                section_icon=ft.Icons.MONITOR_ROUNDED,
                section_content=self.display_form,
            ),

            PresetSection(
                title="Графика",
                section_icon=ft.Icons.AUTO_AWESOME_ROUNDED,
                section_content=self.graphics_form,
            ),

            PresetSection(
                title="Управление",
                section_icon=ft.Icons.MOUSE_ROUNDED,
                section_content=self.control_form,
            ),

            PresetSection(
                title="Производительность",
                section_icon=ft.Icons.SPEED_ROUNDED,
                section_content=self.performance_form,
            ),

            self.notes_field,
        ]

    def validate(self) -> bool:
        if not self.name_field.value or not self.name_field.value.strip():
            self.name_field.error = "Обязательное поле"
            self.name_field.update()
            return False

        self.name_field.error = None
        self.name_field.update()

        return True

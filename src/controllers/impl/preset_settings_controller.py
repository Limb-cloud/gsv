from sqlalchemy.exc import SQLAlchemyError

from controllers.preset_settings_controller_interface import PresetSettingsControllerInterface
from models.data_classes.control_settings import ControlSettings
from models.data_classes.controller_result import ControllerResult
from models.data_classes.display_settings import DisplaySettings
from models.data_classes.graphics_settings import GraphicsSettings
from models.data_classes.performance_settings import PerformanceSettings
from models.preset import Preset
from repositories.preset_repository import PresetRepository
from views.factories.notification_factory import NotificationFactory


class PresetSettingsController(PresetSettingsControllerInterface):

    def __init__(self, preset_repository: PresetRepository):
        self._preset_repository = preset_repository

    def load_presets(self, game_id: int) -> ControllerResult[list[Preset]]:
        try:
            presets = self._preset_repository.get_by_game_id(game_id)

            if presets is None:
                return ControllerResult(
                    notification=NotificationFactory.info("Список пресетов пуст")
                )

            return ControllerResult(
                data=presets
            )

        except SQLAlchemyError:
            return ControllerResult(
                notification=NotificationFactory.error("Не удалось загрузить пресеты игры")
            )

    def get_preset(self, preset_id: int) -> ControllerResult[Preset]:
        try:
            preset = self._preset_repository.get_by_id(preset_id)

            if preset is None:
                return ControllerResult(
                    notification=NotificationFactory.info("Пресет не найден")
                )

            return ControllerResult(
                data=preset
            )

        except SQLAlchemyError:
            return ControllerResult(
                notification=NotificationFactory.error("Не удалось загрузить пресет")
            )

    def on_add_preset(
            self,
            game_id: int,
            name: str,
            resolution: str | None,
            display_mode: str | None,
            refresh_rate: str | int | None,
            fps_limit: str | int | None,
            graphics_preset: str | None,
            textures: str | None,
            shadows: str | None,
            ray_tracing: str | None,
            upscaler: str | None,
            dpi: str | int | None,
            sensitivity: str | float | None,
            fov: str | int | None,
            average_fps: str | int | None,
            gpu_temperature: str | int | None,
            cpu_temperature: str | int | None,
            notes: str | None,
    ) -> ControllerResult[Preset]:
        try:
            display = DisplaySettings(
                resolution=resolution,
                display_mode=display_mode,
                refresh_rate=self._to_int(refresh_rate),
                fps_limit=self._to_int(fps_limit),
            )

            graphics = GraphicsSettings(
                preset=graphics_preset,
                textures=textures,
                shadows=shadows,
                ray_tracing=ray_tracing,
                upscaler=upscaler,
            )

            control = ControlSettings(
                dpi=self._to_int(dpi),
                sensitivity=self._to_float(sensitivity),
                fov=self._to_int(fov),
            )

            performance = PerformanceSettings(
                average_fps=self._to_int(average_fps),
                gpu_temperature=self._to_int(gpu_temperature),
                cpu_temperature=self._to_int(cpu_temperature),
            )

            preset = Preset(
                game_id=game_id,
                name=name,
                display=display,
                graphics=graphics,
                control=control,
                performance=performance,
                notes=notes,
            )

            preset = self._preset_repository.add(preset)

            return ControllerResult(
                data=preset,
                notification=NotificationFactory.success("Пресет успешно добавлен")
            )

        except (TypeError, ValueError) as error:
            return ControllerResult(
                notification=NotificationFactory.warning(str(error))
            )

        except SQLAlchemyError:
            return ControllerResult(
                notification=NotificationFactory.error("Не удалось добавить пресет")
            )

    def on_update_preset(
            self,
            preset: Preset,
            name: str,
            resolution: str | None,
            display_mode: str | None,
            refresh_rate: str | int | None,
            fps_limit: str | int | None,
            graphics_preset: str | None,
            textures: str | None,
            shadows: str | None,
            ray_tracing: str | None,
            upscaler: str | None,
            dpi: str | int | None,
            sensitivity: str | float | None,
            fov: str | int | None,
            average_fps: str | int | None,
            gpu_temperature: str | int | None,
            cpu_temperature: str | int | None,
            notes: str | None,
    ) -> ControllerResult[Preset]:
        try:
            preset.name = name

            preset.display = DisplaySettings(
                resolution=resolution,
                display_mode=display_mode,
                refresh_rate=self._to_int(refresh_rate),
                fps_limit=self._to_int(fps_limit),
            )

            preset.graphics = GraphicsSettings(
                preset=graphics_preset,
                textures=textures,
                shadows=shadows,
                ray_tracing=ray_tracing,
                upscaler=upscaler,
            )

            preset.control = ControlSettings(
                dpi=self._to_int(dpi),
                sensitivity=self._to_float(sensitivity),
                fov=self._to_int(fov),
            )

            preset.performance = PerformanceSettings(
                average_fps=self._to_int(average_fps),
                gpu_temperature=self._to_int(gpu_temperature),
                cpu_temperature=self._to_int(cpu_temperature),
            )

            preset.notes = notes

            preset = self._preset_repository.update(preset)

            return ControllerResult(
                data=preset,
                notification=NotificationFactory.success("Пресет сохранён")
            )

        except (TypeError, ValueError) as error:
            return ControllerResult(
                notification=NotificationFactory.warning(str(error))
            )

        except SQLAlchemyError:
            return ControllerResult(
                notification=NotificationFactory.error("Не удалось сохранить пресет")
            )

    def on_delete_preset(self, preset: Preset) -> ControllerResult[bool]:
        try:
            self._preset_repository.delete(preset)

            return ControllerResult(
                data=True,
                notification=NotificationFactory.success("Пресет удалён")
            )

        except SQLAlchemyError:
            return ControllerResult(
                notification=NotificationFactory.error("Не удалось удалить пресет")
            )

    @staticmethod
    def _to_int(value: str | int | None) -> int | None:
        if value is None:
            return None

        if isinstance(value, str):
            value = value.strip()

            if not value:
                return None

        try:
            return int(value)

        except (TypeError, ValueError):
            raise ValueError("Проверьте корректность числовых полей")

    @staticmethod
    def _to_float(value: str | float | None) -> float | None:
        if value is None:
            return None

        if isinstance(value, str):
            value = value.strip().replace(",", ".")

            if not value:
                return None

        try:
            return float(value)

        except (TypeError, ValueError):
            raise ValueError("Проверьте корректность числовых полей")

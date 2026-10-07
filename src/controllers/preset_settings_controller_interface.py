from abc import ABC, abstractmethod

from models.data_classes.controller_result import ControllerResult
from models.preset import Preset


class PresetSettingsControllerInterface(ABC):

    @abstractmethod
    def load_presets(self, game_id: int) -> ControllerResult[list[Preset]]:
        pass

    @abstractmethod
    def get_preset(self, preset_id: int) -> ControllerResult[Preset]:
        pass

    @abstractmethod
    def on_add_preset(
            self,
            game_id: int,
            name: str,
            resolution: str | None,
            display_mode: str | None,
            refresh_rate: int | None,
            fps_limit: int | None,
            graphics_preset: str | None,
            textures: str | None,
            shadows: str | None,
            ray_tracing: str | None,
            upscaler: str | None,
            dpi: int | None,
            sensitivity: float | None,
            fov: int | None,
            average_fps: int | None,
            gpu_temperature: int | None,
            cpu_temperature: int | None,
            notes: str | None,
    ) -> ControllerResult[Preset]:
        pass

    @abstractmethod
    def on_update_preset(
            self,
            preset: Preset,
            name: str,
            resolution: str | None,
            display_mode: str | None,
            refresh_rate: int | None,
            fps_limit: int | None,
            graphics_preset: str | None,
            textures: str | None,
            shadows: str | None,
            ray_tracing: str | None,
            upscaler: str | None,
            dpi: int | None,
            sensitivity: float | None,
            fov: int | None,
            average_fps: int | None,
            gpu_temperature: int | None,
            cpu_temperature: int | None,
            notes: str | None,
    ) -> ControllerResult[Preset]:
        pass

    @abstractmethod
    def on_delete_preset(self, preset: Preset) -> ControllerResult[bool]:
        pass
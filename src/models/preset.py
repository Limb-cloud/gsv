from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import (
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import (
    Mapped,
    composite,
    mapped_column,
    relationship,
)

from models.abstract.base import Base
from models.data_classes.control_settings import ControlSettings
from models.data_classes.display_settings import DisplaySettings
from models.data_classes.graphics_settings import GraphicsSettings
from models.data_classes.performance_settings import PerformanceSettings


if TYPE_CHECKING:
    from models.game import Game


class Preset(Base):
    __tablename__ = "presets"

    _id: Mapped[int] = mapped_column(
        "id",
        primary_key=True,
        autoincrement=True,
    )

    _game_id: Mapped[int] = mapped_column(
        "game_id",
        ForeignKey("games.id"),
        nullable=False,
    )

    _name: Mapped[str] = mapped_column(
        "name",
        String(255),
        nullable=False,
    )

    _display: Mapped[DisplaySettings] = composite(
        mapped_column(
            "display_resolution",
            String(30),
            nullable=True,
        ),
        mapped_column(
            "display_mode",
            String(30),
            nullable=True,
        ),
        mapped_column(
            "display_refresh_rate",
            Integer,
            nullable=True,
        ),
        mapped_column(
            "display_fps_limit",
            Integer,
            nullable=True,
        ),
    )

    _graphics: Mapped[GraphicsSettings] = composite(
        mapped_column(
            "graphics_preset",
            String(30),
            nullable=True,
        ),
        mapped_column(
            "graphics_textures",
            String(30),
            nullable=True,
        ),
        mapped_column(
            "graphics_shadows",
            String(30),
            nullable=True,
        ),
        mapped_column(
            "graphics_ray_tracing",
            String(30),
            nullable=True,
        ),
        mapped_column(
            "graphics_upscaler",
            String(50),
            nullable=True,
        ),
    )

    _control: Mapped[ControlSettings] = composite(
        mapped_column(
            "control_dpi",
            Integer,
            nullable=True,
        ),
        mapped_column(
            "control_sensitivity",
            Float,
            nullable=True,
        ),
        mapped_column(
            "control_fov",
            Integer,
            nullable=True,
        ),
    )

    _performance: Mapped[PerformanceSettings] = composite(
        mapped_column(
            "performance_average_fps",
            Integer,
            nullable=True,
        ),
        mapped_column(
            "performance_gpu_temperature",
            Integer,
            nullable=True,
        ),
        mapped_column(
            "performance_cpu_temperature",
            Integer,
            nullable=True,
        ),
    )

    _notes: Mapped[str | None] = mapped_column(
        "notes",
        Text,
        nullable=True,
    )

    game: Mapped[Game] = relationship(
        "Game",
        back_populates="presets",
    )

    def __init__(
        self,
        game_id: int,
        name: str,
        display: DisplaySettings | None = None,
        graphics: GraphicsSettings | None = None,
        control: ControlSettings | None = None,
        performance: PerformanceSettings | None = None,
        notes: str | None = None,
    ):
        self.game_id = game_id
        self.name = name

        self.display = (
            display
            if display is not None
            else DisplaySettings()
        )

        self.graphics = (
            graphics
            if graphics is not None
            else GraphicsSettings()
        )

        self.control = (
            control
            if control is not None
            else ControlSettings()
        )

        self.performance = (
            performance
            if performance is not None
            else PerformanceSettings()
        )

        self.notes = notes

    @hybrid_property
    def id(self) -> int | None:
        return self._id

    @hybrid_property
    def game_id(self) -> int:
        return self._game_id

    @game_id.inplace.setter
    def _game_id_setter(
        self,
        value: int,
    ) -> None:
        if not isinstance(value, int):
            raise TypeError(
                "game_id должен иметь тип int"
            )

        if value <= 0:
            raise ValueError(
                "ID игры должен быть больше нуля"
            )

        self._game_id = value

    @hybrid_property
    def name(self) -> str:
        return self._name

    @name.inplace.setter
    def _name_setter(
        self,
        value: str,
    ) -> None:
        if not isinstance(value, str):
            raise TypeError(
                "Название пресета должно иметь тип str"
            )

        value = value.strip()

        if not value:
            raise ValueError(
                "Название пресета не может быть пустым"
            )

        self._name = value

    @property
    def display(self) -> DisplaySettings:
        return self._display

    @display.setter
    def display(
        self,
        value: DisplaySettings,
    ) -> None:
        if not isinstance(value, DisplaySettings):
            raise TypeError(
                "display должен иметь тип DisplaySettings"
            )

        self._display = value

    @property
    def graphics(self) -> GraphicsSettings:
        return self._graphics

    @graphics.setter
    def graphics(
        self,
        value: GraphicsSettings,
    ) -> None:
        if not isinstance(value, GraphicsSettings):
            raise TypeError(
                "graphics должен иметь тип GraphicsSettings"
            )

        self._graphics = value

    @property
    def control(self) -> ControlSettings:
        return self._control

    @control.setter
    def control(
        self,
        value: ControlSettings,
    ) -> None:
        if not isinstance(value, ControlSettings):
            raise TypeError(
                "control должен иметь тип ControlSettings"
            )

        self._control = value

    @property
    def performance(
        self,
    ) -> PerformanceSettings:
        return self._performance

    @performance.setter
    def performance(
        self,
        value: PerformanceSettings,
    ) -> None:
        if not isinstance(
            value,
            PerformanceSettings,
        ):
            raise TypeError(
                "performance должен иметь тип "
                "PerformanceSettings"
            )

        self._performance = value

    @hybrid_property
    def notes(self) -> str | None:
        return self._notes

    @notes.inplace.setter
    def _notes_setter(
        self,
        value: str | None,
    ) -> None:
        if value is None:
            self._notes = None
            return

        if not isinstance(value, str):
            raise TypeError(
                "notes должен иметь тип str или None"
            )

        value = value.strip()

        self._notes = value or None

    def _comparison_key(
        self,
    ) -> tuple[int, str]:
        return (
            self.game_id,
            self.name.casefold(),
        )

    def __eq__(
        self,
        other: object,
    ) -> bool:
        if not isinstance(other, Preset):
            return NotImplemented

        return (
            self._comparison_key()
            == other._comparison_key()
        )

    def __lt__(
        self,
        other: object,
    ) -> bool:
        if not isinstance(other, Preset):
            return NotImplemented

        return (
            self._comparison_key()
            < other._comparison_key()
        )

    def __le__(
        self,
        other: object,
    ) -> bool:
        if not isinstance(other, Preset):
            return NotImplemented

        return (
            self._comparison_key()
            <= other._comparison_key()
        )

    def __gt__(
        self,
        other: object,
    ) -> bool:
        if not isinstance(other, Preset):
            return NotImplemented

        return (
            self._comparison_key()
            > other._comparison_key()
        )

    def __ge__(
        self,
        other: object,
    ) -> bool:
        if not isinstance(other, Preset):
            return NotImplemented

        return (
            self._comparison_key()
            >= other._comparison_key()
        )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return (
            f"Preset("
            f"id={self.id}, "
            f"game_id={self.game_id}, "
            f"name='{self.name}'"
            f")"
        )
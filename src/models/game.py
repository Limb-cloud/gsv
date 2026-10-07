from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, Text
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.abstract.base import Base
from models.preset import Preset


class Game(Base):
    __tablename__ = "games"

    _id: Mapped[int] = mapped_column(
        "id",
        primary_key=True,
        autoincrement=True,
    )

    _name: Mapped[str] = mapped_column(
        "name",
        String(255),
        unique=True,
        nullable=False,
    )

    _description: Mapped[str | None] = mapped_column(
        "description",
        Text,
        nullable=True,
    )

    _cover_path: Mapped[str | None] = mapped_column(
        "cover_path",
        String(500),
        nullable=True,
    )

    _favorite: Mapped[bool] = mapped_column(
        "favorite",
        Boolean,
        default=False,
        nullable=False,
    )

    _created_at: Mapped[datetime] = mapped_column(
        "created_at",
        DateTime,
        default=datetime.now,
        nullable=False,
    )

    presets: Mapped[list[Preset]] = relationship(
        "Preset",
        back_populates="game",
        cascade="all, delete-orphan",
    )

    def __init__(
        self,
        name: str,
        description: str | None = None,
        cover_path: str | None = None,
        favorite: bool = False,
    ):
        self.name = name
        self.description = description
        self.cover_path = cover_path
        self.favorite = favorite

    @hybrid_property
    def id(self) -> int | None:
        return self._id

    @hybrid_property
    def name(self) -> str:
        return self._name

    @name.inplace.setter
    def _name_setter(
        self,
        value: str,
    ) -> None:
        value = value.strip()

        if not value:
            raise ValueError(
                "Название игры не может быть пустым"
            )

        self._name = value

    @hybrid_property
    def description(self) -> str | None:
        return self._description

    @description.inplace.setter
    def _description_setter(
        self,
        value: str | None,
    ) -> None:
        if value is None:
            self._description = None
            return

        value = value.strip()

        self._description = value or None

    @hybrid_property
    def cover_path(self) -> str | None:
        return self._cover_path

    @cover_path.inplace.setter
    def _cover_path_setter(
        self,
        value: str | None,
    ) -> None:
        if value is None:
            self._cover_path = None
            return

        value = value.strip()

        self._cover_path = value or None

    @hybrid_property
    def favorite(self) -> bool:
        return self._favorite

    @favorite.inplace.setter
    def _favorite_setter(
        self,
        value: bool,
    ) -> None:
        if not isinstance(value, bool):
            raise TypeError(
                "favorite должен иметь тип bool"
            )

        self._favorite = value

    @hybrid_property
    def created_at(self) -> datetime | None:
        return self._created_at

    @property
    def preset_count(self) -> int:
        return len(self.presets)

    def toggle_favorite(self) -> None:
        self.favorite = not self.favorite

    def _comparison_key(self) -> str:
        return self.name.casefold()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Game):
            return NotImplemented

        return (
            self._comparison_key()
            == other._comparison_key()
        )

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Game):
            return NotImplemented

        return (
            self._comparison_key()
            < other._comparison_key()
        )

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Game):
            return NotImplemented

        return (
            self._comparison_key()
            <= other._comparison_key()
        )

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Game):
            return NotImplemented

        return (
            self._comparison_key()
            > other._comparison_key()
        )

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Game):
            return NotImplemented

        return (
            self._comparison_key()
            >= other._comparison_key()
        )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return (
            f"Game("
            f"id={self.id}, "
            f"name='{self.name}'"
            f")"
        )
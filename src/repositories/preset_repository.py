from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database.database import Database
from models.preset import Preset
from repositories.intarfaces.base_repository import BaseRepository


class PresetRepository(BaseRepository):

    def __init__(self, database: Database):
        self._database = database

    def get_all(self) -> list[Preset]:
        with self._database.create_session() as session:
            statement = (
                select(Preset)
                .order_by(Preset.name)
            )

            return list(session.scalars(statement).all())

    def get_by_id(self, preset_id: int) -> Preset | None:
        with self._database.create_session() as session:
            statement = (
                select(Preset)
                .where(Preset.id == preset_id)
            )

            return session.scalars(statement).first()

    def add(self, preset: Preset) -> Preset:
        with self._database.create_session() as session:
            try:
                session.add(preset)
                session.commit()
                session.refresh(preset)

                return preset

            except SQLAlchemyError:
                session.rollback()
                raise

    def update(self, preset: Preset) -> Preset:
        with self._database.create_session() as session:
            try:
                preset = session.merge(preset)

                session.commit()
                session.refresh(preset)

                return preset

            except SQLAlchemyError:
                session.rollback()
                raise

    def delete(self, preset: Preset) -> None:
        with self._database.create_session() as session:
            try:
                preset = session.merge(
                    preset
                )

                session.delete(preset)
                session.commit()

            except SQLAlchemyError:
                session.rollback()
                raise

    def get_by_game_id(self, game_id: int) -> list[Preset]:
        with self._database.create_session() as session:
            statement = (
                select(Preset)
                .where(
                    Preset.game_id == game_id
                )
                .order_by(Preset.name)
            )

            return list(session.scalars(statement).all())
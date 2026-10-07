from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload

from database.database import Database
from models.game import Game
from repositories.intarfaces.base_repository import BaseRepository


class GameRepository(BaseRepository):

    def __init__(self, database: Database):
        self._database = database

    def get_all(self) -> list[Game]:
        with self._database.create_session() as session:
            statement = (
                select(Game)
                .options(
                    selectinload(Game.presets)
                )
                .order_by(Game.name)
            )

            return list(session.scalars(statement).all())


    def get_by_id(self, game_id: int) -> Game | None:
        with self._database.create_session() as session:
            statement = (
                select(Game)
                .options(
                    selectinload(Game.presets)
                )
                .where(Game.id == game_id)
            )

            return session.scalars(statement).first()

    def add(self, game: Game) -> Game:
        with self._database.create_session() as session:
            try:
                session.add(game)
                session.commit()
                session.refresh(game)

                return game

            except SQLAlchemyError:
                session.rollback()
                raise

    def update(self, game: Game) -> Game:
        with self._database.create_session() as session:
            try:
                game = session.merge(game)
                session.commit()
                session.refresh(game)

                return game

            except SQLAlchemyError:
                session.rollback()
                raise

    def delete(self, game: Game) :
        with self._database.create_session() as session:
            try:
                game = session.merge(game)

                session.delete(game)
                session.commit()

            except SQLAlchemyError:
                session.rollback()
                raise

    def search(self, query: str) -> list[Game]:
        with self._database.create_session() as session:
            statement = (
                select(Game)
                .options(
                    selectinload(Game.presets)
                )
                .where(
                    Game.name.ilike(
                        f"%{query}%"
                    )
                )
                .order_by(Game.name)
            )

            return list(
                session.scalars(statement).all()
            )

    def get_favorites(self) -> list[Game]:
        with self._database.create_session() as session:
            statement = (
                select(Game)
                .options(
                    selectinload(Game.presets)
                )
                .where(
                    Game.favorite.is_(True)
                )
                .order_by(Game.name)
            )

            return list(session.scalars(statement).all())
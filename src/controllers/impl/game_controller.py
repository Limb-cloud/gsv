from sqlalchemy.exc import SQLAlchemyError

from controllers.game_controller_interface import GameControllerInterface
from mappers.GameMapper import GameMapper
from models.data_classes.controller_result import ControllerResult
from models.game import Game
from repositories.game_repository import GameRepository
from views.components.game_card_components.game_card import GameCard
from views.factories.notification_factory import NotificationFactory


class GameController(GameControllerInterface):

    def __init__(self, game_repository: GameRepository):
        self._game_repository = game_repository

    def load_games(self, on_open, on_favorite, on_delete) -> ControllerResult[list[GameCard]]:
        try:
            games = self._game_repository.get_all()

            if games is None:
                return ControllerResult(
                    notification=NotificationFactory.info("Список игр пуст")
                )

            return ControllerResult(
                GameMapper.to_views(
                    games,
                    on_open,
                    on_favorite,
                    on_delete
                )
            )

        except SQLAlchemyError:
            return ControllerResult(
                NotificationFactory.error("Не удалось загрузить список игр")
            )

    def load_favorites(self, on_open, on_favorite, on_delete) -> ControllerResult[list[GameCard]]:
        try:
            games = self._game_repository.get_favorites()

            if games is None:
                return ControllerResult(
                    notification=NotificationFactory.info("Список избранных игр пуст")
                )

            return ControllerResult(
                GameMapper.to_views(
                    games,
                    on_open,
                    on_favorite
                )
            )

        except SQLAlchemyError:
            return ControllerResult(
                NotificationFactory.error("Не удалось загрузить список игр")
            )

    def get_game(self, game_id: int) -> ControllerResult[Game]:
        try:
            game = self._game_repository.get_by_id(game_id)

            if game is None:
                return ControllerResult(
                    notification=NotificationFactory.info("Игра не найдена")
                )

            return ControllerResult(
                data=game
            )

        except SQLAlchemyError:
            return ControllerResult(
                notification=NotificationFactory.error("Не удалось получить игру")
            )

    def on_add_game(
            self,
            name: str,
            description: str | None,
            cover_path: str | None,
            favorite: bool,
    ) -> ControllerResult[Game]:
        try:
            game = Game(
                name=name,
                description=description,
                cover_path=cover_path,
                favorite=favorite,
            )

            game = self._game_repository.add(game)

            return ControllerResult(
                data=game,
                notification=NotificationFactory.success("Игра успешно добавлена")
            )

        except ValueError as error:
            return ControllerResult(
                notification=NotificationFactory.warning(str(error))
            )

        except SQLAlchemyError:
            return ControllerResult(
                notification=NotificationFactory.error("Не удалось добавить игру")
            )

    def on_update_game(
            self,
            game: Game,
            name: str,
            description: str | None,
            cover_path: str | None,
            favorite: bool,
    ) -> ControllerResult[Game]:
        try:
            game.name = name
            game.description = description
            game.cover_path = cover_path
            game.favorite = favorite

            game = self._game_repository.update(game)

            return ControllerResult(
                data=game,
                notification=NotificationFactory.success("Игра успешно изменена")
            )

        except ValueError as error:
            return ControllerResult(
                notification=NotificationFactory.warning(str(error))
            )

        except SQLAlchemyError:
            return ControllerResult(
                notification=NotificationFactory.error("Не удалось изменить игру")
            )

    def on_delete_game(self, game: Game) -> ControllerResult[bool]:
        try:
            self._game_repository.delete(game)

            return ControllerResult(
                data=True,
                notification=NotificationFactory.success("Игра успешно удалена")
            )

        except SQLAlchemyError:
            return ControllerResult(
                notification=NotificationFactory.error("Не удалось удалить игру")
            )

    def on_toggle_favorite(self, game: Game) -> ControllerResult[Game]:
        try:
            game.toggle_favorite()

            game = self._game_repository.update(game)

            return ControllerResult(
                data=game
            )

        except SQLAlchemyError:
            game.toggle_favorite()

            return ControllerResult(
                notification=NotificationFactory.error("Не удалось изменить избранное")
            )

    def on_search(
            self,
            query: str,
            on_open,
            on_favorite
    ) -> ControllerResult[list[GameCard]]:
        try:
            games = self._game_repository.search(query)

            return ControllerResult(
                data=GameMapper.to_views(
                    games,
                    on_open,
                    on_favorite
                )
            )

        except SQLAlchemyError:
            return ControllerResult(
                notification=NotificationFactory.error("Не удалось выполнить поиск")
            )

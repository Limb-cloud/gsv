from abc import ABC, abstractmethod

from models.data_classes.controller_result import ControllerResult
from models.game import Game
from views.components.game_card_components.game_card import GameCard


class GameControllerInterface(ABC):

    @abstractmethod
    def load_games(self, on_open, on_favorite, on_delete) -> ControllerResult[list[GameCard]]:
        pass

    @abstractmethod
    def load_favorites(self, on_open, on_favorite, on_delete) -> ControllerResult[list[GameCard]]:
        pass

    @abstractmethod
    def get_game(self, game_id: int) -> ControllerResult[Game]:
        pass

    @abstractmethod
    def on_add_game(
            self,
            name: str,
            description: str | None,
            cover_path: str | None,
            favorite: bool,
    ) -> ControllerResult[Game]:
        pass

    @abstractmethod
    def on_update_game(
            self,
            game: Game,
            name: str,
            description: str | None,
            cover_path: str | None,
            favorite: bool,
    ) -> ControllerResult[Game]:
        pass

    @abstractmethod
    def on_delete_game(self, game: Game) -> ControllerResult[bool]:
        pass

    @abstractmethod
    def on_toggle_favorite(self, game: Game) -> ControllerResult[Game]:
        pass

    @abstractmethod
    def on_search(
            self,
            query: str,
            on_open,
            on_favorite,
            on_delete
    ) -> ControllerResult[list[GameCard]]:
        pass
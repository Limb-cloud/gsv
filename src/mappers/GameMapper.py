from typing import Callable

from models.game import Game
from views.components.game_card_components.game_card import GameCard


class GameMapper:

    @staticmethod
    def to_view(
        game: Game,
        on_open: Callable,
        on_favorite: Callable,
        on_edit: Callable | None = None,
        on_delete: Callable | None = None,
    ) -> GameCard:
        return GameCard(
            game=game,
            on_click=lambda e: on_open(game),
            on_favorite_click=on_favorite,
            on_edit=on_edit,
            on_delete=on_delete
        )

    @staticmethod
    def to_views(
        games: list[Game],
        on_open: Callable,
        on_favorite: Callable,
        on_edit: Callable | None = None,
        on_delete: Callable | None = None,
    ) -> list[GameCard]:
        return [
            GameMapper.to_view(
                game=game,
                on_open=on_open,
                on_favorite=on_favorite,
                on_edit=on_edit,
                on_delete=on_delete
            )
            for game in games
        ]

    @staticmethod
    def to_game(
        game_view: GameCard,
    ) -> Game:
        return game_view.game
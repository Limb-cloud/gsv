import os
from pathlib import Path

from platformdirs import user_data_dir
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from enums.paths import Paths


class Database:
    def __init__(self):
        self._data_dir = self._get_data_directory()
        self._db_path = self._data_dir / "game_settings.db"

        self._engine = create_engine(
            f"sqlite+pysqlite:///{self._db_path.as_posix()}",
            echo=False,
        )

        self._session_factory = sessionmaker(
            bind=self._engine,
            autoflush=False,
            expire_on_commit=False,
        )

    def _get_data_directory(self) -> Path:
        data_dir = Path(
            user_data_dir(
                "Game Settings Vault"
            )
        )

        data_dir.mkdir(
            parents=True,
            exist_ok=True,
        )
        return data_dir

    @property
    def engine(self):
        return self._engine

    @property
    def session_factory(self):
        return self._session_factory

    @property
    def db_path(self) -> Path:
        return self._db_path

    def create_session(self):
        return self._session_factory()
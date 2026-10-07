from sqlalchemy.orm import DeclarativeBase


from abc import ABCMeta, abstractmethod

from sqlalchemy.orm import DeclarativeBaseNoMeta


class Base(DeclarativeBaseNoMeta, metaclass=ABCMeta):

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass

    @abstractmethod
    def __lt__(self, other) -> bool:
        pass

    @abstractmethod
    def __le__(self, other) -> bool:
        pass

    @abstractmethod
    def __gt__(self, other) -> bool:
        pass

    @abstractmethod
    def __ge__(self, other) -> bool:
        pass

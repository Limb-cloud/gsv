from abc import ABC, abstractmethod


class AbstractReport(ABC):

    @abstractmethod
    def save(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
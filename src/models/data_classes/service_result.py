from dataclasses import dataclass


@dataclass
class ServiceResult[T]:
    data: T | None = None
    error: Exception | None = None

    @property
    def success(self) -> bool:
        return self.error is None
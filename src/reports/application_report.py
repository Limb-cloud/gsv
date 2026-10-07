from datetime import datetime
from pathlib import Path

from reports.abstract_application_report import AbstractReport


class ApplicationReport(AbstractReport):

    DATE_FORMAT = "%d.%m.%Y %H:%M:%S"

    def __init__(
            self,
            login: str,
            report_path: Path
    ):
        self.login = login
        self.time_in = datetime.now()
        self.time_out = None
        self.report_path = report_path

    @property
    def login(self) -> str:
        return self._login

    @login.setter
    def login(self, value: str):
        if not value.strip():
            raise ValueError("Логин не может быть пустым")

        self._login = value.strip()

    @property
    def time_in(self) -> datetime:
        return self._time_in

    @time_in.setter
    def time_in(self, value: datetime):
        self._time_in = value

    @property
    def time_out(self) -> datetime | None:
        return self._time_out

    @time_out.setter
    def time_out(self, value: datetime | None):
        self._time_out = value

    @property
    def report_path(self) -> Path:
        return self._report_path

    @report_path.setter
    def report_path(self, value: Path):
        self._report_path = value

    def save(self) -> None:
        self.time_out = datetime.now()

        self.report_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with self.report_path.open(
                "w",
                encoding="utf-8"
        ) as file:
            file.write(
                str(self)
            )

    @staticmethod
    def _format_datetime(value: datetime | None) -> str:
        if value is None:
            return ""

        return value.strftime(
            ApplicationReport.DATE_FORMAT
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ApplicationReport):
            return NotImplemented

        return self.time_in == other.time_in

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, ApplicationReport):
            return NotImplemented

        return self.time_in < other.time_in

    def __le__(self, other: object) -> bool:
        if not isinstance(other, ApplicationReport):
            return NotImplemented

        return self.time_in <= other.time_in

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, ApplicationReport):
            return NotImplemented

        return self.time_in > other.time_in

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, ApplicationReport):
            return NotImplemented

        return self.time_in >= other.time_in

    def __str__(self) -> str:
        login_width = max(
            len(self.login),
            len("login")
        )

        time_width = 19

        border = (
            f"+-{'-' * login_width}-"
            f"+-{'-' * time_width}-"
            f"+-{'-' * time_width}-+"
        )

        header = (
            f"| {'login':<{login_width}} "
            f"| {'time_in':<{time_width}} "
            f"| {'time_out':<{time_width}} |"
        )

        separator = (
            f"|-{'-' * login_width}-"
            f"|-{'-' * time_width}-"
            f"|-{'-' * time_width}-|"
        )

        values = (
            f"| {self.login:<{login_width}} "
            f"| {self._format_datetime(self.time_in):<{time_width}} "
            f"| {self._format_datetime(self.time_out):<{time_width}} |"
        )

        return (
            f"{border}\n"
            f"{header}\n"
            f"{separator}\n"
            f"{values}\n"
            f"{border}"
        )

    def __repr__(self) -> str:
        return (
            f"ApplicationReport("
            f"login='{self.login}', "
            f"time_in='{self._format_datetime(self.time_in)}', "
            f"time_out='{self._format_datetime(self.time_out)}'"
            f")"
        )
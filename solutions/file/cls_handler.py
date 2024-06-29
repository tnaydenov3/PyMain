from solutions.classes.loggable import Loggable
from solutions.path.path import Path

_ERR_FILE_MISSING = "File {path} does not exist!"


class FileHandler(Loggable):

    @classmethod
    def _log_prefix(cls) -> str:
        return cls.__class__.__name__

    __slots__ = ("_target_path",)

    def __init__(self, target_path: Path) -> None:
        self._target_path = target_path

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._target_path})"

    @property
    def target_path(self) -> Path:
        return self._target_path

    @property
    def os_path(self) -> str:
        return self._target_path.os_path

    @Loggable.logfunction
    def _log_missing(self) -> None:
        path = self._target_path.os_path
        self._log_msg(message=_ERR_FILE_MISSING.format(path=path))

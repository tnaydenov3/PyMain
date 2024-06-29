from solutions.classes.loggable import Loggable
from solutions.path.path import Path

_ERR_FILE_MISSING = "File {path} does not exist!"

_MSG_DELETE_FILE = "{path} deleted."


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

    @property
    def path(self) -> str:
        return str(object=self._target_path)

    def delete_target_path(self) -> None:
        self._target_path.delete_path()
        self._log_deleted()

    def exists(self) -> bool:
        return self._target_path.exists()

    def target_filename(self) -> str:
        return self._target_path.filename

    def target_path_suffix(self) -> str:
        return self._target_path.suffix

    @Loggable.logfunction
    def _log_missing(self) -> str:
        path = self._target_path.os_path
        return _ERR_FILE_MISSING.format(path=path)

    @Loggable.logfunction
    def _log_deleted(self) -> str:
        path = self._target_path.os_path
        return _MSG_DELETE_FILE.format(path=path)

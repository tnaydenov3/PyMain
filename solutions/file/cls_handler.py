from solutions.classes.loggable import Loggable
from solutions.path.path import Path


class FileHandler(Loggable):

    @classmethod
    def _log_prefix(cls) -> str:
        return cls.__class__.__name__

    __slots__ = ("_target_path",)

    def __init__(self, target_path: Path) -> None:
        self._target_path = target_path

    @property
    def target_path(self) -> Path:
        return self._target_path

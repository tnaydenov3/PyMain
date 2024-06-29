import os


class Path:
    _DEFAULT_SEP = "/"

    __slots__ = ("_path_parts",)

    def __init__(self, path_parts: list[str]) -> None:
        self._path_parts = path_parts

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self._path_parts})>"

    def __str__(self) -> str:
        return self._DEFAULT_SEP.join(self._path_parts)

    @property
    def path_parts(self) -> list[str]:
        return self._path_parts

    @property
    def os_path(self) -> str:
        return os.sep.join(self._path_parts)

    @property
    def suffix(self) -> str:
        return self._path_parts[-1].split(".")[-1]

from contextlib import contextmanager
from io import TextIOWrapper
import os
from typing import Generator

UNIX_SEP = "/"
WINDOWS_SEP = "\\"


class Path:

    _DEFAULT_SEP = UNIX_SEP

    @classmethod
    def _str_to_default_sep(cls, path_str: str) -> str:
        norm_path = os.path.normpath(path=path_str)
        norm_path = norm_path.replace(UNIX_SEP, cls._DEFAULT_SEP)
        norm_path = norm_path.replace(WINDOWS_SEP, cls._DEFAULT_SEP)

        return norm_path

    __slots__ = ("_path_parts",)

    def __init__(self, *, path_parts: list[str]) -> None:
        self._path_parts = path_parts

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self._path_parts})>"

    def __str__(self) -> str:
        return self._DEFAULT_SEP.join(self._path_parts)

    @property
    def path_parts(self) -> list[str]:
        return self._path_parts

    @property
    def dir_parts(self) -> list[str]:
        return self._path_parts[:-1]

    @property
    def os_path(self) -> str:
        return os.sep.join(self._path_parts)

    @property
    def os_dir(self) -> str:
        return os.sep.join(self._path_parts[:-1])

    @property
    def filename(self) -> str:
        return self._path_parts[-1]

    @property
    def suffix(self) -> str:
        return self._path_parts[-1].split(sep=".")[-1]

    def delete_path(self) -> None:
        os.remove(self.os_path)

    def exists(self) -> bool:
        return os.path.exists(self.os_path)

    def is_dir(self) -> bool:
        return os.path.isdir(self.os_path)

    def dir_path(self) -> "Path":
        return Path(path_parts=self.dir_parts)

    def join(self, *path_parts: str) -> "Path":
        return Path(path_parts=self._path_parts + list(path_parts))

    @contextmanager
    def open(
        self, mode: str = "r", encoding: str = "utf-8"
    ) -> Generator[TextIOWrapper, None, None]:
        with open(file=self.os_path, mode=mode, encoding=encoding) as file:
            yield file

    def write(self, content: str, encoding: str = "utf-8") -> None:
        with open(file=self.os_path, mode="w", encoding=encoding) as file:
            file.write(content=content)

    def read(self, encoding: str = "utf-8") -> str:
        with open(file=self.os_path, mode="r", encoding=encoding) as file:
            return file.read()

    def list_dir(self) -> list["Path"]:
        if self.is_dir():
            subpaths = os.listdir(path=self.os_path)
            return [Path(path_parts=self.path_parts + [path]) for path in subpaths]
        else:
            return []

    @classmethod
    def from_string(cls, path_str: str) -> "Path":
        normalized_path = cls._str_to_default_sep(path_str=path_str)
        path_parts = normalized_path.split(sep=cls._DEFAULT_SEP)

        return cls(path_parts=path_parts)

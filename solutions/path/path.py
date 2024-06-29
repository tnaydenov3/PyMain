import os


class Path:
    UNIX_SEP = "/"
    WINDOWS_SEP = "\\"

    _DEFAULT_SEP = UNIX_SEP

    @classmethod
    def _str_to_default_sep(cls, path_str: str) -> str:
        norm_path = os.path.normpath(path=path_str)
        norm_path = norm_path.replace(cls.UNIX_SEP, cls._DEFAULT_SEP)
        norm_path = norm_path.replace(cls.WINDOWS_SEP, cls._DEFAULT_SEP)

        return norm_path

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
        os.remove(path=self.os_path)

    def exists(self) -> bool:
        return os.path.exists(path=self.os_path)

    def is_dir(self) -> bool:
        return os.path.isdir(s=self.os_path)

    @classmethod
    def from_string(cls, path_str: str) -> "Path":
        normalized_path = cls._str_to_default_sep(path_str=path_str)
        path_parts = normalized_path.split(sep=cls._DEFAULT_SEP)

        return cls(path_parts=path_parts)

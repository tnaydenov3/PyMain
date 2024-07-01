from contextlib import contextmanager
from io import TextIOWrapper
import os
from typing import Generator, Union

UNIX_SEP = "/"
WINDOWS_SEP = "\\"


class Path:

    _DEFAULT_SEP = UNIX_SEP

    @staticmethod
    def _normalize_case(path: str) -> str:
        return os.path.normcase(path)

    @classmethod
    def _str_to_default_sep(cls, path_str: str) -> str:
        norm_path = os.path.normpath(path=path_str)
        norm_path = norm_path.replace(UNIX_SEP, cls._DEFAULT_SEP)
        norm_path = norm_path.replace(WINDOWS_SEP, cls._DEFAULT_SEP)

        return norm_path

    @classmethod
    def _normalize_path(cls, path: str) -> str:
        norm_case = cls._normalize_case(path=path)
        norm_sep = cls._str_to_default_sep(path_str=norm_case)
        return norm_sep

    @classmethod
    def from_string(cls, path_str: str) -> "Path":
        normalized_path = cls._normalize_path(path=path_str)
        path_parts = normalized_path.split(sep=cls._DEFAULT_SEP)

        return Path(path_parts=path_parts)

    @classmethod
    def from_path_w_diff_suffix(cls, *, path: "Path", suffix: str) -> "Path":
        new_filename = f"{path.filename_nosuffix}.{suffix}"
        return path.dir_path().join(new_filename)

    __slots__ = ("_path_parts",)

    def __init__(self, *, path_parts: list[str]) -> None:
        self._path_parts = path_parts

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self._path_parts})>"

    def __str__(self) -> str:
        return self._DEFAULT_SEP.join(self._path_parts)

    def __len__(self) -> int:
        return len(self._path_parts)

    def __getitem__(self, index: int) -> "Path":
        sub_parts = self._path_parts[index]
        sub_parts_list = sub_parts if isinstance(sub_parts, list) else [sub_parts]
        return Path(path_parts=sub_parts_list)

    def __eq__(self, other: Union["Path", list[str]]) -> bool:
        other_obj = other.path_parts if isinstance(other, Path) else other
        return self._path_parts == other_obj

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
    def filename_nosuffix(self) -> str:
        return self._path_parts[-1].rsplit(sep=".", maxsplit=1)[0]

    @property
    def suffix(self) -> str:
        return self._path_parts[-1].split(sep=".")[-1]

    @property
    def is_module(self) -> bool:
        return self.suffix == "py"

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

    def without_suffix(self) -> "Path":
        return self.dir_path().join(self.filename_nosuffix)

    def relative(self, *, root: "Path") -> Union["Path", None]:
        if root == self[: len(root)]:
            return self[len(root) :]

    def module_form(self, *, root: "Path") -> str | None:
        if self.is_module and not self.is_dir():
            rel_path = self.relative(root=root)
            rel_no_suffix = rel_path.without_suffix()
            return ".".join(rel_no_suffix.path_parts)

    @contextmanager
    def open(
        self, mode: str = "r", encoding: str = "utf-8"
    ) -> Generator[TextIOWrapper, None, None]:
        kwargs = {"file": self.os_path, "mode": mode, "encoding": encoding}
        match mode:
            case "rb" | "wb" | "ab":
                kwargs.pop("encoding")
            case _:
                pass

        with open(**kwargs) as file:
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

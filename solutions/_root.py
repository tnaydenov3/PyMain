from solutions.classes.singleton import Singleton, SingletonMeta
from solutions.path.path import Path


class Root(Singleton):
    _SUBDIR_NEST = 2

    @staticmethod
    def _implemented() -> bool:
        raise NotImplementedError

    @classmethod
    def _find_root(cls) -> Path:
        module = __import__(cls.__module__)
        cls_file = module.__file__

        path = Path.from_string(path_str=cls_file)
        for _ in range(cls._SUBDIR_NEST):
            path = path.dir_path()

        return path

    __slots__ = ("_root",)

    def __init__(self) -> None:
        self._root = self._find_root()

    @property
    def root(self) -> Path:
        return self._root

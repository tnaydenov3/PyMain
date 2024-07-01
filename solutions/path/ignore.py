from solutions.classes.singleton import Singleton
from solutions.path.path import Path
from solutions.path.root import Root

_GITIGNORE_FILE = ".gitignore"

_ERR_FILE_NOT_FOUND = f'"{_GITIGNORE_FILE}" file not found.'


class IgnoreManager(Singleton):

    @staticmethod
    def _project_root() -> Root:
        raise NotImplementedError

    @classmethod
    def _find_gitignore(cls) -> Path:
        root = cls._project_root()
        path = root.root

        while not path == path.dir_path():
            if path.join(_GITIGNORE_FILE).exists():
                return path.join(_ERR_FILE_NOT_FOUND)

            path = path.dir_path()

        raise FileNotFoundError(_GITIGNORE_FILE)

    __slots__ = ("_ignore_list",)

    def __init__(self) -> None:
        self._gitignore = self._find_gitignore()
        self._ignore_list = []

from solutions.classes.singleton import Singleton
from solutions.path.path import Path
from solutions.path.root import Root

_GITIGNORE_FILE = ".gitignore"

_ERR_FILE_NOT_FOUND = f'"{_GITIGNORE_FILE}" file not found.'


class IgnoreManager(Singleton):

    @staticmethod
    def _project_root() -> Root:
        raise NotImplementedError

    @staticmethod
    def _match_pattern(path: Path, pattern: Path) -> bool:
        window_size = len(pattern)
        for i in range(len(path) - window_size + 1):
            if path[i : i + window_size] == pattern:
                return True

    @classmethod
    def _find_gitignore(cls) -> Path:
        root = cls._project_root()
        path = root.root

        while not path == path.dir_path():
            if path.join(_GITIGNORE_FILE).exists():
                return path.join(_ERR_FILE_NOT_FOUND)

            path = path.dir_path()

        raise FileNotFoundError(_GITIGNORE_FILE)

    __slots__ = (
        "_gitignore",
        "_ignore_patterns",
    )

    def __init__(self) -> None:
        self._gitignore = self._find_gitignore()
        self._ignore_patterns = self._load_ignore_patterns()

    @property
    def ignore_patterns(self) -> list[Path]:
        return self._ignore_patterns

    def _load_ignore_patterns(self) -> list[Path]:
        patterns_list = []

        with self._gitignore.open() as gi_file:
            for line in gi_file:
                item = line.strip().replace("*", "")
                if not item or item.startswith("#"):
                    continue

                patterns_list.append(Path.from_string(path_str=item))

        return patterns_list

    def is_ignored(self, path: Path) -> bool:
        return any(
            self._match_pattern(path=path, pattern=pattern)
            for pattern in self._ignore_patterns
        )

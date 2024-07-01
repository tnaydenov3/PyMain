from solutions.path.path import Path


class Tree:

    @classmethod
    def from_file_string(cls, path_str: str) -> "Tree":
        root = Path.from_string(path_str=path_str)
        return cls(root=root)

    __slots__ = ("_root", "_tree")

    def __init__(self, root: Path) -> None:
        self._root = root
        self._tree = None

    @property
    def root(self) -> Path:
        return self._root

    @property
    def tree(self) -> list[Path]:
        return self._tree

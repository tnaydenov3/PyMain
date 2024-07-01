import os
from solutions.path.path import Path


class Tree:

    @staticmethod
    def _get_tree(root: Path) -> list[Path]:
        tree = []
        for dirpath_str, _, file_names in os.walk(top=root.os_path):
            dirpath = Path.from_string(path_str=dirpath_str)
            for file in file_names:
                tree.append(dirpath.join(file))
        return tree

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

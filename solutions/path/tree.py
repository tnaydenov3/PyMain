import os
from solutions.path.path import Path
from solutions.path.root import Root


class Tree:

    @classmethod
    def _project_root(cls) -> Root:
        raise NotImplementedError

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
        self._tree = self._get_tree(root=root)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self._root})>"

    def __str__(self) -> str:
        title = f"{self.__class__.__name__} (root: {self._root})"
        tree_str = "\n".join([str(path) for path in self._tree])

        return f"{title}\n{tree_str}"

    @property
    def root(self) -> Path:
        return self._root

    @property
    def tree(self) -> list[Path]:
        return self._tree

    def get_modules(self) -> list[Path]:
        return [path for path in self._tree if path.is_module()]

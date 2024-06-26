import os
from solutions.path.ignore import IgnoreManager
from solutions.path.path import Path
from solutions.path.root import Root


class Tree:

    _INDENT = " " * 4

    @staticmethod
    def _project_root() -> Root:
        raise NotImplementedError

    @staticmethod
    def _project_ignore_manager() -> IgnoreManager:
        raise NotImplementedError

    @classmethod
    def _is_ignored(cls, *, path: Path) -> bool:
        return cls._project_ignore_manager().is_ignored(path=path)

    @classmethod
    def _get_tree(cls, *, root: Path) -> list[Path]:
        tree = []
        for dirpath_str, _, file_names in os.walk(top=root.os_path):
            dirpath = Path.from_string(path_str=dirpath_str)

            if cls._is_ignored(path=dirpath):
                continue

            tree.append(dirpath)
            for file in file_names:
                filepath = dirpath.join(file)
                if cls._is_ignored(path=filepath):
                    continue

                tree.append(filepath)
        return tree

    @classmethod
    def get_project_tree(cls) -> "Tree":
        root = cls._project_root().root
        return cls(root=root)

    @classmethod
    def from_file_string(cls, *, path_str: str) -> "Tree":
        root = Path.from_string(path_str=path_str)
        return cls(root=root)

    __slots__ = ("_root", "_tree")

    def __init__(self, *, root: Path) -> None:
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
        return [path for path in self._tree if path.is_module]

    def get_module_forms(self) -> list[str]:
        return [
            path.module_form(root=self._root) for path in self._tree if path.is_module
        ]

    def _get_modules_str(self) -> str:
        return "\n".join([mod_form for mod_form in self.get_module_forms()])

    def _get_tree_str(self) -> str:
        root = self._root
        rel_branches = []

        for path in self._tree[1:]:
            indent = len(path) - len(root)
            branch = f"{self._INDENT * indent}{path._DEFAULT_SEP}{path.filename}"
            rel_branches.append(branch)

        return f'{root}\n{"\n".join(rel_branches)}'

    def print_tree_paths(self) -> None:
        print(self)

    def print_modules(self) -> None:
        print(self._get_modules_str())

    def print_tree(self) -> None:
        print(self._get_tree_str())

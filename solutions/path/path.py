class Path:

    __slots__ = ("_path_parts",)

    def __init__(self, path_parts: list[str]) -> None:
        self._path_parts = path_parts

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self._path_parts})>"

from solutions.classes.singleton import Singleton


class IgnoreManager(Singleton):
    __slots__ = ("_ignore_list",)

    def __init__(self) -> None:
        self._ignore_list = []

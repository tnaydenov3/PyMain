from typing import Any


class Debug:

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError

    def __call__(self, debug_msg: str | Any) -> None:
        pass

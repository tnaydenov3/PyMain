_COLOR_RESET = "\033[0m"
_COLOR_BLACK = "\033[30m"
_COLOR_RED = "\033[31m"
_COLOR_GREEN = "\033[32m"
_COLOR_YELLOW = "\033[33m"
_COLOR_BLUE = "\033[34m"
_COLOR_MAGENTA = "\033[35m"
_COLOR_CYAN = "\033[36m"
_COLOR_WHITE = "\033[37m"


class LogColors:

    RED = _COLOR_RED
    GREEN = _COLOR_GREEN
    YELLOW = _COLOR_YELLOW

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError

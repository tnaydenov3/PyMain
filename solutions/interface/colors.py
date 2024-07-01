_COLOR_RESET = "\033[0m"
_COLOR_BLACK = "\033[30m"
_COLOR_RED = "\033[31m"
_COLOR_GREEN = "\033[32m"
_COLOR_YELLOW = "\033[33m"
_COLOR_BLUE = "\033[34m"
_COLOR_MAGENTA = "\033[35m"
_COLOR_CYAN = "\033[36m"
_COLOR_WHITE = "\033[37m"

_RED = "RED"
_GREEN = "GREEN"
_YELLOW = "YELLOW"

_COLOR_DICT = {
    _RED: _COLOR_RED,
    _GREEN: _COLOR_GREEN,
    _YELLOW: _COLOR_YELLOW,
}


class TextColors:

    _RED = _RED
    _GREEN = _GREEN
    _YELLOW = _YELLOW

    @staticmethod
    def _get_color_mod_str(*, color: str) -> str:
        return _COLOR_DICT.get(color, _COLOR_RESET)

    @classmethod
    def _color_placeholders_args(cls, text: str, /, *args: str) -> str:
        colors = list(args)
        last_color = ""
        colored_text = ""

        for char in text:
            if char == "{":
                last_color = colors.pop(index=0) if colors else last_color
                color_mod = cls._get_color_mod_str(color=last_color)
                colored_text += f"{color_mod}{char}"
            elif char == "}":
                colored_text += f"{char}{_COLOR_RESET}"
            else:
                colored_text += char

        return colored_text

    @classmethod
    def _color_placeholders_kwargs(cls, *, text: str, **kwargs) -> str:
        for placeholder_name, color in kwargs.items():
            placeholder = f"{{{placeholder_name}}}"
            placeholder_colored = cls._color_text(text=placeholder, color=color)
            text = text.replace(placeholder, placeholder_colored)

        return text

    @classmethod
    def _color_text(cls, text: str, /, *, color: str) -> str:
        color_mod_str = cls._get_color_mod_str(color=color)
        return f"{color_mod_str}{text}{_COLOR_RESET}"

    @classmethod
    def red(cls, text: str, /) -> str:
        return cls._color_text(text, color=cls._RED)

    @classmethod
    def green(cls, text: str, /) -> str:
        return cls._color_text(text, color=cls._GREEN)

    @classmethod
    def yellow(cls, text: str, /) -> str:
        return cls._color_text(text, color=cls._YELLOW)

    @classmethod
    def col_templ(cls, template: str, /, *args, **kwargs) -> str:
        if args:
            template = cls._color_placeholders_args(template, *args)
        if kwargs:
            template = cls._color_placeholders_kwargs(text=template, **kwargs)

        return template

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError

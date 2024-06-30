from solutions.interface.util_file import SizeBytesUtil

_FILE_SIZE_PATTERN = "{size_num} {unit}"


class ConsoleUtil:

    @staticmethod
    def size_bytes_to_human_readable(size_bytes: int) -> str:
        size_num, unit = SizeBytesUtil.format_bytes(size_bytes=size_bytes)

        return _FILE_SIZE_PATTERN.format(size_num=size_num, unit=unit)

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError

FILE_SIZE_UNITS = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
FILE_SIZE_MULTIPLE = 1024

_FILE_SIZE_ROUNDING_DECIMALS = 2


class SizeBytesUtil:

    @staticmethod
    def format_bytes(size_bytes: int) -> tuple[float, str]:
        size_num = size_bytes

        for unit in FILE_SIZE_UNITS:
            if size_num < FILE_SIZE_MULTIPLE:
                break
            size_num /= FILE_SIZE_MULTIPLE

        size_num = round(number=size_num, ndigits=_FILE_SIZE_ROUNDING_DECIMALS)

        return size_num, unit

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError

class SingletonMeta(type):

    _instances = {}

    __slots__ = tuple()

    def __call__(cls, *args, **kwargs) -> "SingletonMeta":
        if not cls in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError

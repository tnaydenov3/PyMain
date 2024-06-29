class AnimTrackable:

    __slots__ = ("_value", "_val_type")

    def __init__(self, value: object) -> None:
        self._value = value
        self._val_type = type(self._value)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self._value}: {self._val_type})>"

    @property
    def value(self) -> object:
        return self._value

    @property
    def val_type(self) -> type:
        return self._val_type

    @value.setter
    def value(self, value: object) -> None:
        if not isinstance(value, self._val_type):
            raise TypeError(f"Value must be of type {self._val_type}")
        self._value = value

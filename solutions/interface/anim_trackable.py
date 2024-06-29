class AnimTrackable:

    __slots__ = ("_value",)

    def __init__(self, value: object) -> None:
        self._value = value

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self._value}: {type(self._value)})>"

_ERR_VALTYPE = "Value must be of type {val_type}"
_ERR_VALVALUE = "Illegal value."


class Trackable:

    @staticmethod
    def _check_type(*, value: object, val_type: type) -> bool:
        return isinstance(value, val_type)

    @staticmethod
    def _check_constraints(*, value: object) -> bool:
        raise NotImplementedError

    @classmethod
    def _assert_value(cls, *, value: object) -> None:
        if not cls._check_type(value=value, val_type=cls._val_type):
            raise TypeError(_ERR_VALTYPE.format(val_type=cls._val_type))

        if not cls._check_constraints(value=value):
            raise ValueError(_ERR_VALVALUE)

    __slots__ = ("_value", "_val_type")

    def __init__(self, *, value: object, val_type: type) -> None:
        self._check_type(value=value, val_type=val_type)
        self._value = value
        self._val_type = val_type

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self._value}: {self._val_type})>"

    def __str__(self) -> str:
        return str(object=self._value)

    @property
    def value(self) -> object:
        return self._value

    @property
    def val_type(self) -> type:
        return self._val_type

    @value.setter
    def value(self, value: object) -> None:
        self._check_type(value=value, val_type=self._val_type)
        self._value = value

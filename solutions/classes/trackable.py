_ERR_VALTYPE_MSG = "Value must be of type {val_type}."


class Trackable:

    __slots__ = ("_value", "_val_type", "_err_value_msg")

    def __init__(self, *, val_type: type, value: object, err_value_msg: str) -> None:
        self._val_type = val_type
        self._err_value_msg = err_value_msg

        self._assert_value(value=value)
        self._value = value

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self._value}: {self._val_type})>"

    def __str__(self) -> str:
        return str(object=self._value)

    @property
    def value(self) -> object:
        return self._value

    @value.setter
    def value(self, value: object) -> None:
        self._assert_value(value=value)
        self._value = value

    def _check_constraints(self, *, value: object) -> bool:
        raise NotImplementedError

    def _assert_value(self, *, value: object) -> None:
        if not isinstance(value, self._val_type):
            raise TypeError(_ERR_VALTYPE_MSG.format(val_type=self._val_type))

        if not self._check_constraints(value=value):
            raise ValueError(self._err_value_msg)

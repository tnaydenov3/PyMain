from types import FrameType
from solutions.project import PyMainTestRunner
from solutions.testing.testcase import PyMainTestCase
from solutions.util.traceback import Tracebacks


def _raise_error() -> None:
    raise ValueError


@PyMainTestCase
def test_get_error_frame() -> None:
    try:
        _raise_error()

    except Exception as error:
        error_frame = Tracebacks.get_error_frame(error=error)
        assert isinstance(error_frame, FrameType)


@PyMainTestCase
def test_get_error_funcname() -> None:
    try:
        _raise_error()

    except Exception as error:
        error_funcname = Tracebacks.get_error_funcname(error=error)
        assert error_funcname == _raise_error.__name__


if __name__ == "__main__":
    PyMainTestRunner().run_local(file=__file__)

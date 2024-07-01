from solutions.interface.debug import Debug
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
        Debug.log(Tracebacks.get_error_frame(error=error))
        assert Tracebacks.get_error_frame(error=error) == None



if __name__ == "__main__":
    PyMainTestRunner().run_local(file=__file__)

from solutions.path.ignore import IgnoreManager
from solutions.path.path import Path
from solutions.project import PyMainTestRunner
from solutions.testing.testcase import PyMainTestCase


def _init_test() -> tuple[list[Path], ...]:
    ignore_paths = [
        "solutions/__pycache__",
        r"C:\_GitHub\PyMain\.vscode\launch.json",
        ".test/foo.py",
        r"C:\_GitHub\PyMain\.env",
    ]

    not_ignore_paths = [
        "solutions/path/path.py",
        "solutions/path/test",
        r"C:\_GitHub\PyMain\solutions\interface\debug.py",
    ]

    ignore_paths = [Path.from_string(path_str=path) for path in ignore_paths]
    not_ignore_paths = [Path.from_string(path_str=path) for path in not_ignore_paths]

    return ignore_paths, not_ignore_paths


@PyMainTestCase
def test_ignored() -> None:
    ignore_paths, _ = _init_test()

    for path in ignore_paths:
        assert IgnoreManager().is_ignored(path=path)


@PyMainTestCase
def test_not_ignored() -> None:
    _, not_ignore_paths = _init_test()

    for path in not_ignore_paths:
        assert not IgnoreManager().is_ignored(path=path)


if __name__ == "__main__":
    PyMainTestRunner().run_local(file=__file__)

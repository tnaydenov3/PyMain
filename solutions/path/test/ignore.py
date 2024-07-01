def _init_test() -> None:
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

    return ignore_paths, not_ignore_paths

from solutions.interface.colors import TextColors
from solutions.interface.console import ConsoleLogger
from solutions.project import PyMainTestRunner, PyMainTree

_LOG_PREFIX = "COMMAND"

_MSG_INVALID_COMMAND = 'Invalid command "{command}".'
_T_INVALID_COMMAND = TextColors.temp_red(_MSG_INVALID_COMMAND)


class Commands:

    TEST = "test"

    @staticmethod
    def run_project_tests() -> None:
        PyMainTestRunner().run_tree(tree=PyMainTree.get_project_tree())

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError


class CommandCall:

    _COMMANDS = {Commands.TEST: Commands.run_project_tests}

    @staticmethod
    def _log_invalid_command(*, command: str) -> None:
        log_msg = _T_INVALID_COMMAND.format(command=command)
        ConsoleLogger.log(log_msg, prefix=_LOG_PREFIX)

    @classmethod
    def call(cls, *args: str) -> None:
        command = args[0]
        
        if not command in cls._COMMANDS:
            cls._log_invalid_command(command=command)

        else:
            func = cls._COMMANDS[command]
            func()

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError

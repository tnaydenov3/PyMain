from solutions.classes.loggable import Loggable
from solutions.path.path import Path

_ERR_FILE_MISSING = "File {path} does not exist!"

_SKIP_FILE_ALRD_EXISTS = "File {path} already exists, skipping."

_MSG_DELETE_FILE = "{path} deleted."
_MSG_ABORT_FILE = "File {path} aborted. (error: {error})"
_MSG_WORK_BEGIN = "Beginning {action} on <{main_attr}>..."
_MSG_WORK_FINISHED = "Finished {action} on <{main_attr}>."


class FileHandler(Loggable):

    @staticmethod
    def _cl_action() -> str:
        raise NotImplementedError

    @classmethod
    def _log_prefix(cls) -> str:
        return cls.__name__

    __slots__ = ("_target_path",)

    def __init__(self, *, target_path: Path) -> None:
        self._target_path = target_path

    def _main_attr() -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._main_attr()})"

    @property
    def target_path(self) -> Path:
        return self._target_path

    @property
    def os_path(self) -> str:
        return self._target_path.os_path

    @property
    def path(self) -> str:
        return str(object=self._target_path)

    def exists(self) -> bool:
        return self._target_path.exists()

    def target_filename(self) -> str:
        return self._target_path.filename

    def target_path_suffix(self) -> str:
        return self._target_path.suffix

    def delete_target_path(self) -> None:
        self._target_path.delete_path()
        self._log_deleted()

    def _abort_target_path(self, error: Exception) -> None:
        self._target_path.delete_path()
        self._log_aborted(error=error)

    def _handle_work(self) -> None:
        raise NotImplementedError

    def _handle(self, force: bool = False) -> None:
        if self.exists() and not force:
            self._log_skipping()
            return

        try:
            self._log_work_begin()
            self._handle_work()
            self._log_work_finished()

        except Exception as error:
            self._log_aborted(error=error)

    @Loggable.logfunction
    def _log_missing(self) -> str:
        path = self._target_path.os_path
        return _ERR_FILE_MISSING.format(path=path)

    @Loggable.logfunction
    def _log_skipping(self) -> str:
        path = self._target_path.os_path
        return _SKIP_FILE_ALRD_EXISTS.format(path=path)

    @Loggable.logfunction
    def _log_deleted(self) -> str:
        path = self._target_path.os_path
        return _MSG_DELETE_FILE.format(path=path)

    @Loggable.logfunction
    def _log_aborted(self, error: Exception) -> str:
        path = self._target_path.os_path
        return _MSG_ABORT_FILE.format(path=path, error=error)

    @Loggable.logfunction
    def _log_work_begin(self) -> str:
        action = self._cl_action()
        main_attr = self._main_attr()
        return _MSG_WORK_BEGIN.format(action=action, main_attr=main_attr)

    @Loggable.logfunction
    def _log_work_finished(self) -> str:
        action = self._cl_action()
        main_attr = self._main_attr()
        return _MSG_WORK_FINISHED.format(action=action, main_attr=main_attr)

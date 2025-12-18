import traceback
from types import TracebackType
from classes.exceptions.engine_exception import EngineError

class ScriptError(EngineError):
    def __init__(self, script_path: str, exc: Exception, tb: TracebackType):
        
        self.script_path = script_path
        self.exc = exc

        self.frame = self._extract_script_frame(tb)
        self.location = self._format_frame(self.frame)

        super().__init__(str(exc))

    def _extract_script_frame(self, tb: TracebackType):
        frames = traceback.extract_tb(tb)
        script = self.script_path

        res = None

        for frame in frames:
            if frame.filename == script:
                res = frame

        return res

    def _format_frame(self, frame):
        if frame is None:
            return "Unknown script location"

        return (
            f'File "{frame.filename}", '
            f"line {frame.lineno}, "
            f"in {frame.name}\n"
            f"  >> {frame.line}"
        )

    def __str__(self):
        return (
            f"[SCRIPT ERROR]\n"
            f"{self.location}\n\n"
            f"{type(self.exc).__name__}: {self.exc}"
        )
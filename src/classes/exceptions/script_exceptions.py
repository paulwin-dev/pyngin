from classes.exceptions.engine_exception import EngineError


class ScriptError(EngineError):
    def __init__(self, script: str, message: str, traceback: str):
        super().__init__(message)

        self.script = script
        self.message = message
        self.traceback = traceback

    def __str__(self) -> str:
        return (
            f"[SCRIPT ERROR]\n"
            f"Script: {self.script}\n"
            f"Message: {self.message}\n"
            f"Traceback:\n{self.traceback}"
        )
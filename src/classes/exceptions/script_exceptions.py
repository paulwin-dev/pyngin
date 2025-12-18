from classes.exceptions.engine_exception import EngineError


class ScriptError(EngineError):
    def __init__(self, script: str, error_name: str, message: str, traceback: str):
        super().__init__(message)

        self.script = script
        self.error_name = error_name
        self.message = message
        self.traceback = None

        tb_index = traceback.find('File "<string>", line')

        i = tb_index + 1
        while True:
            if traceback[i] == "\n":
                break
            i += 1

        self.traceback = traceback[tb_index:i]
                


    def __str__(self) -> str:
        return (
            f"{self.script}\n"
            f"{self.error_name}: {self.message}\n"
            f"\t{self.traceback}"
        )
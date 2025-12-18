import os
import threading

from pathlib import Path
import traceback

from classes.exceptions.engine_exception import EngineError
from classes.exceptions.script_exceptions import ScriptError
from constants import SCRIPT_DIRECTORY_PATH
from classes.base.engine_base import EngineBase
from core import logger

class ScriptLoader(EngineBase):
    def __init__(self, root) -> None:
        super().__init__()

        self._scripts_dir_abs_path = os.getcwd() + f"\\{SCRIPT_DIRECTORY_PATH}"
        self._scripts_dir = Path(self._scripts_dir_abs_path)

        self._root = root

    def _load_scripts(self):
        py_files = list(self._scripts_dir.glob("*.py"))

        for file in py_files:
            with open(file, "r", encoding="utf8") as f:
                contents = f.read()

            self._run_script(str(file) ,contents)

    def _run_script(self, script_path: str, script_contents: str):
        thread = threading.Thread(target=self._script_worker, args=(script_path, script_contents))
        thread.start()

    def _script_worker(self, script_path: str, script_contents: str):
        local_env = {}
        code = compile(script_contents, str(script_path), "exec")
        
        try:
            exec(code, local_env)
        except Exception as e:
            err = ScriptError(script_path, e, e.__traceback__)
            logger.error(str(err))
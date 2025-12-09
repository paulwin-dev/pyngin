import os
import threading

from pathlib import Path

from constants import SCRIPT_DIRECTORY_PATH
from classes.base.engine_base import EngineBase

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

            self._run_script(contents)

    def _run_script(self, scriptContents: str):
        local_env = {}
        thread = threading.Thread(target=exec, args=(scriptContents, local_env))
        thread.start()
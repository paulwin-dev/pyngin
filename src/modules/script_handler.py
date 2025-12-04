import importlib
import os
import config

scriptsDirectoryAbsolutePath = os.getcwd() + f"\\{config.SCRIPT_DIRECTORY_NAME}"

for file in os.listdir(scriptsDirectoryAbsolutePath):
    if os.path.isdir(file) or not file.endswith("py"): 
        continue

    module_name = file[:-3]
    module = importlib.import_module(f"scripts.{module_name}")
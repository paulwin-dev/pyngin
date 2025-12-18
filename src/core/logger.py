from datetime import datetime
from enum import Enum

class LogLevel(Enum):
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"

COLORS = {
    "INFO": "\033[32m",   # green
    "WARN": "\033[33m",   # yellow
    "ERROR": "\033[31m",  # red
}
RESET = "\033[0m"

def log(level: LogLevel, msg: str):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{COLORS.get(level.value, "")}[{timestamp}] [{level.value}] {msg} {RESET}")

def info(msg: str):
    log(LogLevel.INFO, msg)

def warn(msg: str):
    log(LogLevel.WARN, msg)

def error(msg: str):
    log(LogLevel.ERROR, msg)
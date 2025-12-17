from datetime import datetime

def log(level: str, msg: str):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{level}] {msg}")

def info(msg: str):
    log("INFO", msg)

def warn(msg: str):
    log("WARN", msg)

def error(msg: str):
    log("ERROR", msg)
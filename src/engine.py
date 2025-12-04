from pathlib import Path
import sys
import threading
import pygame

from gameloop import gameloop
from classes.Nodes.DataModel import DataModel
from modules import window

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from modules import script_handler

game: DataModel = DataModel()
window = window

window._init()
gameloop.init()
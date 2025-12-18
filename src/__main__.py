from classes.nodes.node import Node
from classes.nodes.core.root import Root

from core import logger
import engine

root = Root()
engine.root = root

root._init()

engine.window = root.systems.graphics.window

root.systems._load_scripts()
root.systems._start_gameloop()
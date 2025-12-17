from classes.nodes.node import Node
from classes.nodes.root import Root

import engine

root = Root()
engine.root = root

root._init()

engine.window = root.systems.graphics.window

root.systems._load_scripts()
root.systems._start_gameloop()
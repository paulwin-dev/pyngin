from classes.nodes.drawable.rect import Rect
from classes.types.color import Color
from engine import root, window

print("Hey!")

r = Rect(parent=root, name="test")
print(root.get_node("test", Color))
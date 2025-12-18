from classes.nodes.drawable.ui.rect import Rect
from classes.types.color import Color
from engine import root, window

rect = Rect(parent=root)
rect._draw(window._surface)


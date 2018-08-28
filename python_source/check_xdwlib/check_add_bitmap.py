import types
import os
import enum
print(repr(types))   # should point to the `types` module in the standard library
print(repr(os))
print(repr(enum))

from xdwlib.document import Document
from types import MappingProxyType
from xdwlib import xdwopen, Point

#print("test")

file = "D:\\sourcetree\\python_source\\check_xdwlib\\a.xdw"
#symbol = b"D:\\sourcetree\\python_source\\check_xdwlib\\b.PNG"
symbol = "D:\sourcetree\python_source\check_xdwlib\\b.png"

with xdwopen(file, autosave=True) as doc:
    pg = doc.page(0)
    pg.add_bitmap(position=Point(0,0), path=symbol)
    #ann = pg.add_text(position=Point(1, 1), text="test")
    #ann.position = Point(0.0, 0.0)

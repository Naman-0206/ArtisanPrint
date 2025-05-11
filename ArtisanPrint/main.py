import shutil
import time
from widgets.text import TextWidget
from widgets.lists import ListWidget
from widgets.box import BoxWidget
from widgets.padding import PaddingWidget

if __name__ == "__main__":

    width = shutil.get_terminal_size().columns

    tw1 = TextWidget("Hello", align="left", padding=(0,1))
    tw2 = TextWidget("World!", align="left")

    l2 = ListWidget([tw1, tw2, tw1], direction="vertical", separator=" , ")
    l = ListWidget([tw1, tw2, tw1, tw2], direction="vertical", separator=" , ")
    lw = ListWidget([tw1, l, tw2, l2], direction="horizontal", separator=" , ")
    
    # BoxWidget(lw, title= "Hello  World", art=None, title_align="left").render(width)
    box = BoxWidget(lw, title= "Hello  World", art=None, title_align="left", padding=(1,3))
    box.render(width)


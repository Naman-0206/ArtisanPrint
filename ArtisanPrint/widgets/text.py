import textwrap
from .widget import Widget
from .padding import apply_padding, PaddingType, unpack

class TextWidget(Widget):
    """
    A simple widget that displays a block of text, automatically wrapped to fit terminal width.
    """

    def __init__(self, text: str, align: str = "left", padding: PaddingType = 0):
        """
        :param text: The raw text content to display.
        :param align: Alignment of the text - 'left', 'center', or 'right'.
        """
        super().__init__()
        self.text = text
        self.align = align
        self.padding = unpack(padding)

    def getlines(self, max_width: int) -> list[str]:
        """
        Wraps the text to the given width and aligns each line accordingly.
        """
        max_width -= self.padding[1] + self.padding[3]
        wrapped = textwrap.wrap(self.text, width=max_width)
        if self.align == "center":
            return [line.center(max_width) for line in wrapped]
        elif self.align == "right":
            return [line.rjust(max_width) for line in wrapped]
        
        return apply_padding(wrapped, self.padding)  # Default to left alignment

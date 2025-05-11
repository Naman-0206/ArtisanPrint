import textwrap
from .widget import Widget


class TextWidget(Widget):
    """
    A simple widget that displays a block of text, automatically wrapped to fit terminal width.
    """

    def __init__(self, text: str, align: str = "left"):
        """
        :param text: The raw text content to display.
        :param align: Alignment of the text - 'left', 'center', or 'right'.
        """
        super().__init__()
        self.text = text
        self.align = align

    def getlines(self, max_width: int) -> list[str]:
        """
        Wraps the text to the given width and aligns each line accordingly.
        """
        wrapped = textwrap.wrap(self.text, width=max_width)
        if self.align == "center":
            return [line.center(max_width) for line in wrapped]
        elif self.align == "right":
            return [line.rjust(max_width) for line in wrapped]
        return wrapped  # Default to left alignment

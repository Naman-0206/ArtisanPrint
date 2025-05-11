from .widget import Widget
from typing import Tuple, Union


PaddingType = Union[int, Tuple[int], Tuple[int, int], Tuple[int, int, int, int]]


class PaddingWidget(Widget):
    """
    A widget that adds padding around another widget.
    """

    def __init__(
        self,
        widget: Widget,
        padding: int | tuple[int, int, int, int] = 1
    ):
        """
        :param widget: The inner widget to be padded.
        :param padding: Padding around the widget. Can be:
            - int: applies the same padding on all sides.
            - tuple of 2 ints: (vertical, horizontal) → top/bottom and left/right.
            - tuple of 4 ints: (top, right, bottom, left).
        """
        super().__init__(widget, padding)
        self.widget = widget

        if isinstance(padding, int):
            self.top = self.right = self.bottom = self.left = padding

        elif isinstance(padding, (tuple, list)):
            if len(padding) == 4:
                self.top, self.right, self.bottom, self.left = padding
            elif len(padding) == 2:
                self.top = self.bottom = padding[0]
                self.right = self.left = padding[1]
            elif len(padding) == 1:
                self.top = self.right = self.bottom = self.left = padding[0]
            else:
                raise ValueError(
                    "Padding must be an int or a tuple of 1, 2, or 4 ints")

        else:
            raise ValueError("Padding must be an int or a tuple/list of ints")

    def getlines(self, max_width: int) -> list[str]:

        inner_max_width = max(0, max_width - self.left - self.right)
        inner_lines = self.widget.getlines(inner_max_width)

        # Add horizontal padding to each line
        padded_lines = [
            (" " * self.left) + line + (" " * self.right)
            for line in inner_lines
        ]

        max_content_width = len(max(padded_lines, default=""))

        # Add vertical padding
        empty_line = " " * max_content_width
        top_padding = [empty_line] * self.top
        bottom_padding = [empty_line] * self.bottom

        return top_padding + padded_lines + bottom_padding


def unpack(padding: PaddingType):
    if isinstance(padding, int):
        return padding, padding, padding, padding

    elif isinstance(padding, (tuple, list)):
        if len(padding) == 4:
            return padding
        elif len(padding) == 2:
            return padding[0], padding[1], padding[0], padding[1]
        elif len(padding) == 1:
            return padding[0], padding[0], padding[0], padding[0]
        else:
            raise ValueError(
                "Padding must be an int or a tuple of 1, 2, or 4 ints")

    else:
        raise ValueError("Padding must be an int or a tuple/list of ints")


def apply_padding(lines, padding: PaddingType):
    if not padding: return lines
    top, right, bottom, left = unpack(padding)
    max_width = len(max(lines, default=""))
    empty_line = " " * max_width

    return [empty_line]*top+[
        (" " * left) + line + (" " * right)
        for line in lines
    ]+[empty_line]*bottom

class BoxArt:
    """Defines characters to render boxes.

    ┌─┬┐ top
    │ ││ head
    ├─┼┤ head_row
    │ ││ mid
    ├─┼┤ row
    ├─┼┤ foot_row
    │ ││ foot
    └─┴┘ bottom

    Args:
        box (str): Characters making up box.
    """

    def __init__(self, box: str) -> None:
        self._box = box
        line1, line2, line3, line4, line5, line6, line7, line8 = box.splitlines()
        # top
        self.top_left, self.top, self.top_divider, self.top_right = iter(line1)
        # head
        self.head_left, _, self.head_vertical, self.head_right = iter(line2)
        # head_row
        (
            self.head_row_left,
            self.head_row_horizontal,
            self.head_row_cross,
            self.head_row_right,
        ) = iter(line3)

        # mid
        self.mid_left, _, self.mid_vertical, self.mid_right = iter(line4)
        # row
        self.row_left, self.row_horizontal, self.row_cross, self.row_right = iter(line5)
        # foot_row
        (
            self.foot_row_left,
            self.foot_row_horizontal,
            self.foot_row_cross,
            self.foot_row_right,
        ) = iter(line6)
        # foot
        self.foot_left, _, self.foot_vertical, self.foot_right = iter(line7)
        # bottom
        self.bottom_left, self.bottom, self.bottom_divider, self.bottom_right = iter(
            line8
        )


ROUNDED = BoxArt(
    """\
╭─┬╮
│ ││
├─┼┤
│ ││
├─┼┤
├─┼┤
│ ││
╰─┴╯
"""
)

from .widget import Widget


class BoxWidget(Widget):
    """
    A widget that draws a border box around a single child widget.
    Supports an optional title, customizable BoxArt, and title alignment.
    """

    def __init__(
        self,
        widget: Widget,
        title: str = "",
        art=None,
        title_align: str = "center"  # 'left', 'center', 'right'
    ):
        """
        :param widget: Inner widget to render inside the box.
        :param title: Optional string displayed on the top border.
        :param art: BoxArt instance specifying box style.
        :param title_align: Alignment of title: 'left', 'center', or 'right'.
        """
        super().__init__(widget, title, art)
        self.widget = widget
        self.title = title
        self.art = art or ROUNDED
        self.title_align = title_align

    def getlines(self, max_width: int) -> list[str]:
        # Reserve 2 columns for left and right borders
        inner_max_width = max_width - 2
        inner_lines = self.widget.getlines(inner_max_width)

        # Prepare title text
        title_text = f" {self.title} " if self.title else ""
        content_width = max((len(line) for line in inner_lines), default=0)
        box_width = min(max(content_width, len(title_text)) + 2, max_width)
        title_text = title_text[:box_width - 2]  # Trim if title is too long

        # Calculate padding based on alignment
        space = box_width - 2 - len(title_text)
        if self.title_align == "left":
            title_line = f"{self.art.top_left}{title_text}{self.art.top * space}{self.art.top_right}"
        elif self.title_align == "right":
            title_line = f"{self.art.top_left}{self.art.top * space}{title_text}{self.art.top_right}"
        else:  # default center
            left_pad = space // 2
            right_pad = space - left_pad
            title_line = f"{self.art.top_left}{self.art.top * left_pad}{title_text}{self.art.top * right_pad}{self.art.top_right}"

        # Build side content lines
        middle_lines = [
            f"{self.art.mid_left}{line.ljust(box_width - 2)}{self.art.mid_right}"
            for line in inner_lines
        ]

        # Build bottom line
        bottom_line = f"{self.art.bottom_left}{self.art.bottom * (box_width - 2)}{self.art.bottom_right}"

        return [title_line] + middle_lines + [bottom_line]


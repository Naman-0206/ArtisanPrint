from .widget import Widget


class ListWidget(Widget):
    """
    A widget that holds multiple child widgets and arranges them
    either in a vertical or horizontal layout, depending on available width.
    """

    def __init__(self, widgets: list[Widget], direction: str = "auto", separator: str = " "):
        """
        :param widgets: List of Widget instances to be rendered.
        :param direction: 'vertical', 'horizontal', or 'auto' (chooses based on width).
        :param separator: String used to separate widgets in horizontal layout.
        """
        super().__init__(widgets, direction, separator)
        self.widgets = widgets
        self.direction = direction
        self.separator = separator

    def getlines(self, max_width: int) -> list[str]:
        """
        Returns the combined lines from all child widgets arranged in the specified direction.
        Aligns horizontally and vertically if direction is horizontal.

        :param max_width: Maximum width available for rendering the widget.
        """
        if not self.widgets:
            return []

        # Get each widget's lines within max_width
        child_lines_list = [w.getlines(max_width) for w in self.widgets]

        # Estimate how much width would be needed in horizontal layout
        max_horizontal_width = sum(
            [max((len(line) for line in lines), default=0) for lines in child_lines_list]
        ) + len(self.separator) * (len(child_lines_list) - 1)

        # Decide layout based on direction or width fit
        layout = self.direction
        if layout == "auto":
            layout = "horizontal" if max_horizontal_width <= max_width else "vertical"
        elif layout == "horizontal" and max_horizontal_width > max_width:
            layout = "vertical"

        if layout == "horizontal":
            # Determine the height of the tallest widget
            max_height = max((len(lines) for lines in child_lines_list), default=0)

            # Vertically pad all widgets to match max_height
            padded_lines_list = []
            for lines in child_lines_list:
                required_padding = max_height - len(lines)
                top_pad = [""] * (required_padding // 2)
                bottom_pad = [""] * ((required_padding + 1) // 2)
                padded_lines = top_pad + lines + bottom_pad
                padded_lines_list.append(padded_lines)

            # Horizontally pad each line in all widgets to align width
            for lines in padded_lines_list:
                max_line_length = max(len(line) for line in lines)
                for idx, line in enumerate(lines):
                    padding = max_line_length - len(line)
                    lines[idx] = line + " " * padding

            # Join all widgets line by line
            lines = []
            middle_line_index = (max_height - 1) // 2
            for idx, line_group in enumerate(zip(*padded_lines_list)):
                if idx == middle_line_index:
                    # Apply separator in the center line
                    lines.append(self.separator.join(line_group))
                else:
                    # Fill with spaces to maintain alignment
                    lines.append((" " * len(self.separator)).join(line_group))
            return lines

        else:  # vertical layout
            lines = []
            for child_lines in child_lines_list:
                lines.extend(child_lines)
            return lines

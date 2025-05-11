import sys


class Widget:
    """
    Base class for all terminal widgets.

    Subclasses must implement `getlines(max_width)` to return the lines
    they want to display, formatted within a given width.

    Handles rendering to the terminal and cleanup (removal) of the widget
    from the terminal screen using ANSI escape codes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the widget with optional positional and keyword arguments.

        These are stored for use by subclasses.
        """
        self.args = args
        self.kwargs = kwargs
        self._height = None  # Number of lines the widget occupies after rendering

    def getlines(self, max_width: int) -> list[str]:
        """
        Must be implemented by subclasses.

        Returns a list of strings representing the widget's display lines,
        constrained to the given maximum width.
        """
        raise NotImplementedError("Subclasses must implement getlines(max_width)")

    def render(self, screen_width: int):
        """
        Renders the widget to the terminal.

        - Calls `getlines(screen_width)` to get the output lines.
        - Prints the lines to the terminal.
        - Stores the number of lines printed for later cleanup.
        """
        lines = self.getlines(screen_width)
        self._height = len(lines)
        for line in lines:
            print(line)

    def clearlines(self, no_lines: int):
        """
        Clears the specified number of lines from the terminal above the cursor.

        This uses ANSI escape codes to:
        - Move the cursor up one line (`\033[F`)
        - Clear the line (`\033[2K`)
        """
        for _ in range(no_lines):
            sys.stdout.write("\033[F")  # Move cursor up one line
            sys.stdout.write("\033[2K")  # Clear entire line

    def cleanup(self):
        """
        Clears the widget's rendered lines from the terminal.

        Uses the stored `_height` to determine how many lines to erase.
        """
        if self._height is not None:
            self.clearlines(self._height)

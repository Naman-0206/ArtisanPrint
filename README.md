# ArtisanPrint

[![PyPI Version](https://img.shields.io/pypi/v/ArtisanPrint)](https://pypi.org/project/ArtisanPrint/)  
[![License](https://img.shields.io/pypi/l/ArtisanPrint)](LICENSE)

ArtisanPrint is a **Python library** for printing text with customizable **styles, colors, and backgrounds** in the terminal using ANSI escape codes. Perfect for making CLI output more readable and visually appealing.

## Installation

To install ArtisanPrint, simply use pip:

```bash
pip install ArtisanPrint
```

## Usage

Import the cprint function from the ArtisanPrint library and use it to print text with desired styles and colors.

```python
from artisanprint import cprint

cprint("Error: Something went wrong", color="red")
cprint("Warning: Proceed with caution", bg_color="yellow")
cprint("Important Message", style="bold")
```
## More Examples

```python
from artisanprint import cprint

# Red + bold
cprint("Hello, world!", color="red", style="bold")

# Green background + italic
cprint("Welcome to ArtisanPrint", bg_color="green", style="italic")

# Custom RGB + underlined
cprint("Custom Color", color=(255, 128, 0), style="underlined")

# Multiple styles + background
cprint("Formatted Text", style="bold italic", bg_color="blue")
```
---

## 📝 Supported Options

### Colors

* **Names**: `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `black`
* **RGB Tuples**: `(r, g, b)` values (0–255)

### Background Colors

* Same as `color`, via `bg_color` parameter

### Styles

* `bold`, `italic`, `underlined`, `strikethrough`

---

## 📌 Notes

* Uses **ANSI escape codes** — behavior may vary by terminal.
* Color and style names are **case-insensitive**.
* Works cross-platform in most modern terminals.

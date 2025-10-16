# ansi-colors

A small Python module for colored console output using ANSI escape codes.  
Works on Windows, macOS, and Linux terminals. Ideal for logging, CLI apps, or scripts where you want colorful, readable messages.

## Features
- Text colors: red, green, yellow, blue, magenta, cyan, white
- Bold text support
- Background colors
- Works on Windows with colorama (auto-initialized)
- Simple helper function `color_text(text, color)` for easy usage

## Installation

Clone the repository:

```bash
git clone https://github.com/DxrRin/ansi-colors.git
```

Install dependencies:

```bash
pip install colorama
```

Import the functions from ansi_colors.py:

```python
from ansi_colors import RED, GREEN, color_text

print(color_text("Success!", GREEN))
print(color_text("Warning!", RED))
```

## Usage
- Wrap console text with color codes for better readability
- Combine with logging or print statements in CLI apps

## File Structure

```
ansi-colors/
├── ansi_colors.py
├── README.md
└── LICENSE
```

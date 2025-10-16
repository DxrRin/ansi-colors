# ansi_colors.py
"""
ANSI Colors Helper
------------------
Lightweight Python module for colorful console output using ANSI escape codes.
Works on Windows, macOS, and Linux terminals.
"""

import colorama
colorama.init(autoreset=True)

# Text styles
RESET = "\033[0m"
BOLD = "\033[1m"

# Text colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

# Background colors
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"


def color_text(text: str, color: str) -> str:
    """
    Wrap text with a color and reset automatically.

    Example:
        print(color_text("Loaded successfully", GREEN))
    """
    return f"{color}{text}{RESET}"


# Optional: quick test if run directly
# You can remove or comment out this block if you just want to use the module in your projects
if __name__ == "__main__":
    print(color_text("This is red", RED))
    print(color_text("This is green", GREEN))
    print(color_text("This is yellow", YELLOW))
    print(color_text("Bold text", BOLD))

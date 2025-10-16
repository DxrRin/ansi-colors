# ansi_colors.py
"""
ANSI Colors Helper
------------------
A small module for colored console output using ANSI escape codes.
Works on most modern terminals (Windows, Linux, macOS, VS Code, etc.)
Includes auto-reset with colorama for Windows compatibility.

Usage Example:
    from ansi_colors import GREEN, RED, color_text

    print(GREEN + "This is green text")
    print(color_text("This is red", RED))
"""

import colorama

# Initialize colorama for Windows support
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
    
    Args:
        text (str): The string to color.
        color (str): ANSI color code (e.g., RED, GREEN).

    Returns:
        str: Colored string ready for printing.

    Example:
        print(color_text("Hello, world!", GREEN))
    """
    return f"{color}{text}{RESET}"


# Optional: quick test if run directly
if __name__ == "__main__":
    print(color_text("This is red", RED))
    print(color_text("This is green", GREEN))
    print(color_text("This is yellow", YELLOW))
    print(color_text("Bold text", BOLD))

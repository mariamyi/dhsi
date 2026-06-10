"""Cat-themed terminal UI: ASCII art, colors, prompts, boxes."""

import os
import sys


if os.name == "nt":
    os.system("")


class Colors:
    ORANGE = "\033[38;5;208m"
    YELLOW = "\033[38;5;220m"
    GREEN = "\033[38;5;82m"
    PINK = "\033[38;5;213m"
    PURPLE = "\033[38;5;141m"
    CYAN = "\033[38;5;87m"
    GRAY = "\033[90m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"


def c(text, color):
    return f"{color}{text}{Colors.RESET}"


CATS = {
    "pixel": r"""
         /\_/\
        ( o.o )
         > ^ <
        /     \
       (  PIXEL )
        \_____/
    """,
    "curious": r"""
         /\_/\
        ( o.o )
         > ? <
    """,
    "happy": r"""
         /\_/\
        ( ^.^ )
         > w <    *purr*
    """,
    "surprised": r"""
         /\_/\
        ( O_O )
         > ! <
    """,
    "sleeping": r"""
         /\_/\
        ( -.- )
         > _ <    zzz...
    """,
    "thinking": r"""
         /\_/\
        ( o.o )
         > . <    hmm
    """,
    "sage": r"""
        /\___/\
       (  *.*  )
       (  =w=  )
        \__v__/    "greetings, young one"
    """,
    "victory": r"""
         /\_/\      ___
        ( ^.^ )    | * |
         > w <     |___|
        /     \    trophy
    """,
}


def width():
    try:
        return min(os.get_terminal_size().columns, 72)
    except OSError:
        return 64


def print_cat(mood="curious", color=None):
    art = CATS.get(mood, CATS["curious"])
    color = color or Colors.ORANGE
    print(c(art, color))


def print_header(text):
    w = width()
    bar = "=" * w
    print()
    print(c(bar, Colors.ORANGE))
    print(c(f"  {text}".ljust(w), Colors.BOLD + Colors.ORANGE))
    print(c(bar, Colors.ORANGE))
    print()


def print_subheader(text):
    print()
    print(c(f"  ~~~ {text} ~~~", Colors.BOLD + Colors.YELLOW))
    print()


def _wrap(text, w):
    out = []
    for paragraph in text.split("\n"):
        if not paragraph.strip():
            out.append("")
            continue
        words = paragraph.split()
        line = ""
        for word in words:
            if line and len(line) + 1 + len(word) > w:
                out.append(line)
                line = word
            else:
                line = f"{line} {word}".strip()
        if line:
            out.append(line)
    return out


def print_box(text, color=None):
    color = color or Colors.YELLOW
    inner = width() - 6
    lines = _wrap(text, inner)
    bar_w = max((len(line) for line in lines), default=0)
    bar_w = max(bar_w, 20)
    print(c("  +" + "-" * (bar_w + 2) + "+", color))
    for line in lines:
        print(c("  | ", color) + line.ljust(bar_w) + c(" |", color))
    print(c("  +" + "-" * (bar_w + 2) + "+", color))


def print_story(text):
    for line in _wrap(text, width() - 4):
        print(c("  " + line, Colors.CYAN))
    print()


def print_lesson(text):
    for line in _wrap(text, width() - 4):
        print(c("  " + line, Colors.YELLOW))
    print()


def print_code(code):
    print(c("  +-- code " + "-" * (width() - 14), Colors.GREEN))
    for line in code.strip("\n").split("\n"):
        print(c("  | ", Colors.GREEN) + c(line, Colors.GREEN + Colors.BOLD))
    print(c("  +" + "-" * (width() - 5), Colors.GREEN))
    print()


def print_success(text):
    print()
    print(c(f"  *purr* {text}", Colors.GREEN + Colors.BOLD))
    print()


def print_error(text):
    print(c(f"  *hiss*  {text}", Colors.PINK))


def print_hint(text):
    print(c(f"  *whisker twitch*  {text}", Colors.PURPLE))


def print_info(text):
    print(c(f"  {text}", Colors.GRAY))


def prompt(label=">>>"):
    return input(c(f"  {label} ", Colors.ORANGE + Colors.BOLD))


def pause():
    try:
        input(c("  [press enter to continue]", Colors.GRAY))
    except EOFError:
        pass
    print()


def menu_option(num, text):
    print(c(f"   {num}. ", Colors.ORANGE) + c(text, Colors.YELLOW))

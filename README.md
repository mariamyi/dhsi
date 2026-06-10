# Pixel's Code Quest

A cat-themed Python learning game. Help Pixel the cat find their way home through the Whisker Woods by solving real Python challenges at the terminal.

```
         /\_/\
        ( o.o )
         > ^ <
        /     \
       (  PIXEL )
        \_____/
```

## Story

Pixel chased a butterfly into the magical Whisker Woods and got lost. To find their way home, they must master the ancient cat-language of Python — guided by Sage, an old gray cat with silver whiskers.

## Chapters

1. **The Ball of Yarn** — variables
2. **The Whispering Scrolls** — strings
3. **The Treat Decision** — if / elif / else
4. **The Great Mouse Hunt** — for and while loops
5. **The Cat Council** — lists
6. **Teaching Tricks** — functions

Each chapter has a short story, a lesson, an example, and a few challenges where you write real Python that gets executed and checked.

## Requirements

- Python 3.8 or newer
- A terminal that supports ANSI colors (most modern terminals do)

No external dependencies.

## Play

From the repo root:

```bash
python3 play.py
```

### In-game commands

While typing code at a challenge:

| Command  | What it does                              |
|----------|-------------------------------------------|
| `:run`   | Execute your code and check the challenge |
| `:show`  | Show the code you've typed so far         |
| `:clear` | Start over on this challenge              |
| `:hint`  | Get a hint (more hints on repeat)         |
| `:skip`  | Skip the current challenge                |
| `:quit`  | Save progress and exit                    |

### Progress

Your progress is saved at `~/.pixel_quest_progress.json`. From the main menu you can continue from the next unfinished chapter, replay a specific chapter, or reset everything.

## Project layout

```
play.py                  # Entry point
pixel_quest/
    __init__.py
    ui.py                # ASCII cat art, colors, themed prompts
    engine.py            # Menu, chapter runner, challenge evaluator
    checks.py            # Test helpers (has_var, func_returns, ...)
    chapters.py          # Story, lessons, and challenges
```

## Adding your own chapter

Append a new chapter dict to `CHAPTERS` in `pixel_quest/chapters.py`:

```python
{
    "id": "ch7_new",
    "title": "Chapter 7 — Your Adventure",
    "cat_mood": "curious",     # see CATS in ui.py
    "story": "...",
    "lesson": "...",
    "example": "x = 1",
    "challenges": [
        {
            "title": "Do the thing",
            "instructions": "Create a variable x equal to 42.",
            "hints": ["x = 42"],
            "checks": [checks.has_var("x", 42)],
            "success": "Nice work!",
        },
    ],
    "ending": "...",
}
```

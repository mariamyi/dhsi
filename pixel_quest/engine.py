"""Game engine: progress, menus, chapter runner, challenge runner."""

import json
import sys
from pathlib import Path

from . import ui


PROGRESS_FILE = Path.home() / ".pixel_quest_progress.json"


def load_progress():
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text())
        except Exception:
            return {}
    return {}


def save_progress(progress):
    try:
        PROGRESS_FILE.write_text(json.dumps(progress, indent=2))
    except Exception:
        pass


def reset_progress():
    if PROGRESS_FILE.exists():
        PROGRESS_FILE.unlink()


def _collect_code():
    """Collect multi-line Python from the player.

    Returns (action, lines). action is one of:
      ':run', ':hint', ':skip', ':quit', ':clear', ':show'
    """
    ui.print_info(
        "Type your Python. Commands: :run  :hint  :clear  :show  :skip  :quit"
    )
    lines = []
    while True:
        label = ">>>" if not lines else "..."
        try:
            line = ui.prompt(label)
        except (EOFError, KeyboardInterrupt):
            return ":quit", lines
        stripped = line.strip()
        if stripped in (":run", ":hint", ":skip", ":quit", ":clear", ":show"):
            return stripped, lines
        lines.append(line)


def _run_challenge(challenge):
    ui.print_subheader(challenge["title"])
    ui.print_box(challenge["instructions"])
    if challenge.get("starter"):
        ui.print_lesson("Starter code:")
        ui.print_code(challenge["starter"])

    hints_shown = 0
    while True:
        action, lines = _collect_code()

        if action == ":quit":
            return False
        if action == ":skip":
            ui.print_lesson("Pixel sighs and pads onward without solving it...")
            return True
        if action == ":hint":
            hints = challenge.get("hints", [])
            if hints_shown < len(hints):
                ui.print_hint(hints[hints_shown])
                hints_shown += 1
            else:
                ui.print_hint("No more hints. Trust your whiskers!")
            continue
        if action == ":clear":
            ui.print_info("(cleared your code)")
            continue
        if action == ":show":
            if not lines:
                ui.print_info("(nothing yet)")
            else:
                ui.print_code("\n".join(lines))
            continue

        code = "\n".join(lines)
        if not code.strip():
            ui.print_error("No code to run yet. Type some Python first.")
            continue

        namespace = dict(challenge.get("setup", {}))
        try:
            exec(compile(code, "<your code>", "exec"), namespace)
        except Exception as e:
            ui.print_error(f"{type(e).__name__}: {e}")
            continue

        all_passed = True
        for check in challenge["checks"]:
            passed, msg = check(namespace)
            if not passed:
                ui.print_error(msg)
                all_passed = False
                break

        if all_passed:
            ui.print_success(
                challenge.get("success", "You did it! Pixel chirps with joy.")
            )
            return True


def _run_chapter(chapter, progress):
    ui.print_header(chapter["title"])
    ui.print_cat(chapter.get("cat_mood", "curious"))
    ui.print_story(chapter["story"])
    ui.pause()

    if chapter.get("lesson"):
        ui.print_subheader("Sage's Lesson")
        ui.print_lesson(chapter["lesson"])
        if chapter.get("example"):
            ui.print_code(chapter["example"])
        ui.pause()

    for challenge in chapter["challenges"]:
        ok = _run_challenge(challenge)
        if not ok:
            return False

    if chapter.get("ending"):
        ui.print_story(chapter["ending"])
        ui.pause()

    progress[chapter["id"]] = "completed"
    save_progress(progress)
    return True


def run_from(chapters, start_id):
    progress = load_progress()
    started = False
    for chapter in chapters:
        if not started and chapter["id"] != start_id:
            continue
        started = True
        if not _run_chapter(chapter, progress):
            ui.print_story(
                "Pixel curls up in a sunbeam to rest. "
                "Your progress is saved — come back any time."
            )
            return
    ui.print_cat("victory")
    ui.print_success(
        "You finished Pixel's Code Quest! Pixel is safely home. "
        "Try the chapters again any time to sharpen your claws."
    )


def menu(chapters):
    progress = load_progress()
    ui.print_header("Pixel's Code Quest")
    ui.print_cat("pixel")
    ui.print_box(
        "A Python learning adventure.\n"
        "Help Pixel the cat find their way home by mastering "
        "the ancient cat-language of code."
    )
    print()

    completed = sum(
        1 for ch in chapters if progress.get(ch["id"]) == "completed"
    )
    if completed:
        ui.print_info(
            f"Progress: {completed} of {len(chapters)} chapters completed."
        )
        print()

    ui.menu_option(1, "Start a new game")
    ui.menu_option(2, "Continue from next chapter")
    ui.menu_option(3, "Choose a chapter")
    ui.menu_option(4, "Reset progress")
    ui.menu_option(5, "Quit")
    print()
    return ui.prompt("choose:").strip()


def main(chapters):
    while True:
        try:
            choice = menu(chapters)
        except (EOFError, KeyboardInterrupt):
            print()
            ui.print_story("Pixel scampers off into the woods...")
            return

        if choice == "1":
            run_from(chapters, chapters[0]["id"])
        elif choice == "2":
            progress = load_progress()
            next_ch = next(
                (ch for ch in chapters
                 if progress.get(ch["id"]) != "completed"),
                None,
            )
            if next_ch is None:
                ui.print_success(
                    "You've completed every chapter. Try choosing one to replay!"
                )
            else:
                run_from(chapters, next_ch["id"])
        elif choice == "3":
            print()
            for i, ch in enumerate(chapters, 1):
                progress = load_progress()
                done = "*" if progress.get(ch["id"]) == "completed" else " "
                ui.menu_option(i, f"[{done}] {ch['title']}")
            print()
            pick = ui.prompt("chapter number:").strip()
            try:
                idx = int(pick) - 1
                if 0 <= idx < len(chapters):
                    run_from(chapters, chapters[idx]["id"])
                else:
                    ui.print_error("That chapter doesn't exist.")
            except ValueError:
                ui.print_error("That's not a number Pixel recognizes.")
        elif choice == "4":
            confirm = ui.prompt("Erase all progress? (y/N):").strip().lower()
            if confirm == "y":
                reset_progress()
                ui.print_success("Progress reset. Fresh start!")
        elif choice in ("5", "q", "quit", "exit"):
            ui.print_cat("sleeping")
            ui.print_story("Pixel curls up for a nap. See you next time.")
            return
        else:
            ui.print_error("Pixel tilts their head. Try a number from the menu.")

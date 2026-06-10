"""Test helpers for evaluating player-submitted Python code.

A check is a callable that takes the player's namespace dict and returns
(passed: bool, message: str). The message is shown on failure.
"""


def has_var(name, expected):
    def check(ns):
        if name not in ns:
            return False, f"I can't find a variable called '{name}' in your code."
        actual = ns[name]
        if actual != expected:
            return False, (
                f"'{name}' should be {expected!r}, but I see {actual!r}."
            )
        return True, ""
    return check


def var_type(name, expected_type, type_name=None):
    type_name = type_name or expected_type.__name__
    def check(ns):
        if name not in ns:
            return False, f"I can't find a variable called '{name}'."
        if not isinstance(ns[name], expected_type):
            return False, (
                f"'{name}' should be a {type_name}, "
                f"but it's a {type(ns[name]).__name__}."
            )
        return True, ""
    return check


def func_returns(name, cases):
    """cases: list of (args_tuple, expected_return)."""
    def check(ns):
        if name not in ns or not callable(ns[name]):
            return False, f"I can't find a function called '{name}'."
        for args, expected in cases:
            try:
                result = ns[name](*args)
            except Exception as e:
                return False, (
                    f"{name}{args!r} raised {type(e).__name__}: {e}"
                )
            if result != expected:
                return False, (
                    f"{name}{args!r} should return {expected!r}, "
                    f"but it returned {result!r}."
                )
        return True, ""
    return check


def custom(predicate, message):
    """predicate: ns -> bool. message shown on failure."""
    def check(ns):
        try:
            if predicate(ns):
                return True, ""
        except Exception as e:
            return False, f"{message} ({type(e).__name__}: {e})"
        return False, message
    return check

from typing import Callable
import os
import re


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def normalize_unicode_powers(expression: str) -> str:
    EXPONENTS = {
        "⁰": "0",
        "¹": "1",
        "²": "2",
        "³": "3",
        "⁴": "4",
        "⁵": "5",
        "⁶": "6",
        "⁷": "7",
        "⁸": "8",
        "⁹": "9",
    }

    transformation: Callable[[re.Match], str] = lambda match: "^" + "".join(
        EXPONENTS[c] for c in match.group()
    )

    regex = r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+"
    return re.sub(regex, transformation, expression)


def normalize(expression: str) -> str:
    expression = expression.strip()
    expression = normalize_unicode_powers(expression)
    return expression


def interaction(
    menu_shower: Callable[[], None], action_processor: Callable[[str], bool]
):
    exit = False
    while not exit:
        clear_screen()
        menu_shower()
        action = input("Select the desired action: ").strip()
        exit = action_processor(action)


def pause() -> None:
    input("Press [Enter] to continue...")

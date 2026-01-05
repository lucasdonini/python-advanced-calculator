from math_func import Function
from io_utils import normalize, interaction, pause
from typing import Dict

functions: Dict[Function] = {}


def read_function() -> Function:
    print("Allowed function format: f(x) = ax+b; and similars")
    entry = input("Enter the desired function: ")
    normalized = normalize(entry)
    return Function(normalized)


def register_function() -> None:
    f = read_function()
    functions[f.name] = f


def show_registered_functions() -> None:
    [print(f" - {f}") for f in functions.values()]


def show_menu() -> None:
    print("=== Function Calculator ===")
    show_registered_functions()
    print(
        """
[0] -> Back to main menu
[1] -> Register function
[2] -> Evaluate function
[3] -> Generate function table
"""
    )


def process(action: str) -> bool:
    match action:
        case "":
            pass
        case "0":
            return True
        case "1":
            register_function()
        case "2":
            print("not implemented")
            pause()
        case "3":
            print("not implemented")
            pause()
        case _:
            print("Option not available")
            pause()
    return False


def main() -> None:
    interaction(show_menu, process)

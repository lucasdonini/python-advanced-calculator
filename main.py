from math_func import Function
from math_function_parser import parse_symbolic, evaluate_exact
from input_helpers import normalize
import math
import re
import os


def evaluate_expression() -> None:
    expression = input("Enter the expression: ")
    normalized = normalize(expression)
    is_simple = re.search(r"[a-zA-Z]", expression) is None
    solver = evaluate_exact if is_simple else parse_symbolic
    result = solver(normalized)
    print(f"{expression} = {result}")


def show_menu() -> None:
    print(
        """
=== Advanced Calculator ===
    [0] -> Exit
    [1] -> Evaluate expression
    [2] -> Use function
"""
    )


def process(action: str) -> bool:
    match action:
        case "0":
            return True
        case "1":
            evaluate_expression()
        case "2":
            print("Not implemented")
        case _:
            print("Action not supported")
    return False


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def main() -> None:
    exit = False
    while not exit:
        clear_screen()
        show_menu()
        action = input("Select the desired action: ").strip()
        exit = process(action)
        if not exit:
            input("Press [Enter] to continue...")


if __name__ == "__main__":
    main()

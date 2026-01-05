from math_function_parser import parse_symbolic, evaluate_exact
from io_utils import normalize, interaction, pause
from function_calculator import main as use_function
import re


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
[2] -> Use Funciton Calculator
"""
    )


def process(action: str) -> bool:
    match action:
        case "":
            pass
        case "0":
            return True
        case "1":
            evaluate_expression()
            pause()
        case "2":
            use_function()
        case _:
            print("Action not supported")
            pause()
    return False


def main() -> None:
    interaction(show_menu, process)


if __name__ == "__main__":
    main()

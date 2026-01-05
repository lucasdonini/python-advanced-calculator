from math_func import Function
from math_function_parser import parse
from input_helpers import normalize
import math


def normalize_result(num: float) -> float | str:
    if math.isnan(num):
        return "undefined"
    if num == math.inf:
        return "∞"
    if num == -math.inf:
        return "-∞"


def evaluate_expression() -> None:
    expression = input("Enter the expression: ")
    normalized = normalize(expression)
    function = parse(normalized, variables=[])
    result = normalize_result(function())
    print(f"{expression} = {result}")


def show_menu() -> None:
    print(
        """
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


def main() -> None:
    exit = False
    while not exit:
        show_menu()
        action = input("Select the desired action: ").strip()
        exit = process(action)


if __name__ == "__main__":
    main()

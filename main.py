from math_func import Function
from math_function_parser import parse
from input_helpers import read_expression


def evaluate_expression() -> None:
    expression = read_expression()
    function = parse(expression, variables=[])
    print(f"{expression} = {function()}")


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
            return False
        case "1":
            evaluate_expression()
        case "2":
            print("Not implemented")
        case _:
            print("Action not supported")
    return True


def main() -> None:
    exit = False
    while not exit:
        show_menu()
        action = input("Select the desired action: ").strip()
        exit = process(action)


if __name__ == "__main__":
    main()

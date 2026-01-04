from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations as std_trasnform,
    implicit_multiplication_application as implicit_multiplcation,
    convert_xor,
)
import sympy as sp
import operator
import re


def find_extremum(function, critical_points, operator):
    extremum = (critical_points[0], function(critical_points[0]))
    for x in critical_points[1:]:
        y = function(x)
        if operator(y, extremum[1]):
            extremum = (x, y)

    return extremum


def read_points():
    entry = input("Input critial points separated by spaces: ")
    points = list(map(float, entry.split()))
    return points


def normalize_unicode_powers(expression: str) -> str:
    SUPERSCRIPTS = {
        '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
        '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'
    }
    replacement = lambda match: '^' + ''.join(SUPERSCRIPTS[c] for c in match.group())
    return re.sub(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+", replacement, expression)

def read_function():
    entry = input("Input function in terms of x: ")
    entry = normalize_unicode_powers(entry)
    x = sp.symbols("x")
    transformations = std_trasnform + (implicit_multiplcation, convert_xor)

    try:
        expr = parse_expr(
            entry, evaluate=True, local_dict={"x": x}, transformations=transformations
        )

        function = sp.lambdify(x, expr, "math")
        return function

    except Exception as e:
        print("Sorry but we couldn't understand the function")
        return None


menu = """
[0] -> Exit
[1] -> Find absolute maximum
[2] -> Find absolute minimum
"""


def main():
    exit = False
    while not exit:
        print(menu)
        action = input("Choose the desired option: ").strip()
        match action:
            case "0":
                exit = True
            case "1" | "2":
                is_max = action == "1"
                function = read_function()
                if not function:
                    continue

                points = read_points()
                operation = operator.gt if is_max else operator.lt

                result = find_extremum(function, points, operation)
                print(f"The absolute {'maximum' if is_max else 'minimum'} is {result}")

            case _:
                print("Option not supported")


if __name__ == "__main__":
    main()

import sympy.parsing.sympy_parser as parser
import sympy as sp
from typing import Callable, List

TRANSFORMATIONS = parser.standard_transformations + (
    parser.implicit_multiplication_application,
    parser.convert_xor,
    parser.function_exponentiation,
)


def parse_symbolic(expression: str, variables: List[str] = []) -> sp.Expr:
    params = sp.symbols(variables)
    parsed = parser.parse_expr(
        expression,
        transformations=TRANSFORMATIONS,
        local_dict={v: p for v, p in zip(variables, params)},
    )

    parsed = sp.nsimplify(parsed)
    parsed = sp.simplify(parsed)
    return parsed


def evaluate_exact(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(expr)

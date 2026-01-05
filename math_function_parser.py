import sympy.parsing.sympy_parser as parser
import sympy as sp
from typing import Callable, List


def parse(expression: str, variables: List[str]) -> Callable[..., float]:
    params = sp.symbols(variables)
    transformations = parser.standard_transformations + (
        parser.implicit_multiplication_application,
        parser.convert_xor,
    )

    parsed = parser.parse_expr(expression, transformations=transformations)
    return sp.lambdify(params, parsed, modules=["math"])

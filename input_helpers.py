from typing import Callable
import re


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
        match.group()
    )

    regex = r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+"
    return re.sub(regex, transformation, expression)


def read_expression(message: str = "Input the expression: ") -> str:
    entry = input(message).strip()
    normalized = normalize_unicode_powers(entry)
    return normalized

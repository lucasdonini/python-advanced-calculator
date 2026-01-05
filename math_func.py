from math_function_parser import parse_symbolic
import re


class Function:
    def __init__(self, raw_math_function: str):
        raw_math_function = raw_math_function.strip()
        regex_pattern = r"(?P<name>[a-zA-Z_]\w*)\((?P<variables>[a-zA-Z_]\w*(?:,\s?[a-zA-Z_]\w*)*)\)\s*=\s*(?P<expression>.+)"

        match = re.fullmatch(regex_pattern, raw_math_function)

        if not match:
            raise ValueError(f"Invalid math funcion: {raw_math_function}")

        function_parts = match.groupdict()
        self.name = function_parts["name"].strip()
        self.variables = [v.strip() for v in function_parts["variables"].split(",")]
        self.expression = function_parts["expression"].strip()
        self.expression = parse_symbolic(self.expression, self.variables)
        self._raw = raw_math_function

    def __call__(self, *args):
        n_args = len(self.variables)
        if len(args) != n_args:
            raise TypeError(
                f"The function {self.name} expects {n_args}, but got {len(args)}"
            )

        values = {variable: value for variable, value in zip(self.variables, args)}
        result = self.expression.subs(values)
        return result

    def __str__(self):
        return self._raw

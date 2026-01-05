from math_func import Function
from itertools import combinations
import pytest


def test__creation__successfull():
    raw_function = "f(x) = x+1"
    f = Function(raw_function)
    assert f is not None
    assert f.name == "f"
    assert f.expression == "x+1"
    assert f._raw == raw_function
    assert f.variables == ["x"]


def test__creation__failed():
    invalid_expressions = ["(x) = x", "f() = x", "f(x)", "f(x) = "]
    for expression in invalid_expressions:
        with pytest.raises(ValueError):
            Function(expression)


def test__evaluation__one_arg__successfull():
    f = Function("f(x) = x+1")
    for x in range(-10, 11):
        expected = x + 1
        assert f(x) == expected


def test__evaluation__two_args__successfull():
    g = Function("g(x,y) = x^2+y^2")
    for x, y in combinations(range(-10, 10), 2):
        expected = x**2 + y**2
        assert g(x, y) == expected


def test__evaluation__failed__too_few_args():
    g = Function("g(x,y) = x^2+y^2")
    with pytest.raises(TypeError):
        g(2)


def test__evaluation__failed__too_many_args():
    f = Function("f(x) = x+1")
    with pytest.raises(TypeError):
        f(2, 3)

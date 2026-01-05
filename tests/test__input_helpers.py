from input_helpers import *


def test__normalize_unicode_exponents__successfull():
    raw = "3x²¹"
    normalized = normalize_unicode_powers(raw)
    assert normalized == "3x^21"

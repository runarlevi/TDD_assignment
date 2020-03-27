from calculator import Calculator

def test_add_empty_returns_zero() -> None:
    assert Calculator.Add("") == 0

def test_add_supports_single_number() -> int:
    assert Calculator.Add("9") == 9

def test_add_supports_two_numbers() -> int:
    assert Calculator.Add("1,2") == 3

def test_add_supports_unknown_numbers() -> int:
    assert Calculator.Add("1,2,3,4,5") == 15

def test_add_supports_newlines_as_delimiter() -> int:
    assert Calculator.Add("1\n2,3") == 6

def test_add_ignores_numbers_bigger_than_1000() -> int:
    assert Calculator.Add("1001,2") == 2
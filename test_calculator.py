from calculator import Calculator

def test_add_empty_returns_zero() -> None:
    assert Calculator.Add("") == 0

def test_add_supports_single_number() -> int:
    assert Calculator.Add("9") == 9

def test_add_supports_two_numbers() -> int:
    assert Calculator.Add("1,2") == 3
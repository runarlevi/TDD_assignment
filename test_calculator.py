from calculator import Calculator

def test_add_empty_returns_zero() -> None:
    assert Calculator.Add("") == 0
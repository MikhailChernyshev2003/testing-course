import pytest
from src.operations import Operations


class TestOperations:
    def test_add_positive_numbers(self):
        a, b = 2.5, 3.7
        expected = 6.2
        result = Operations.add(a, b)
        assert result == expected

    def test_divide_by_zero_raises_error(self):
        a, b = 10.0, 0.0
        with pytest.raises(ZeroDivisionError, match="Деление на ноль недопустимо"):
            Operations.divide(a, b)

    def test_sqrt_negative_number_raises_error(self):
        number = -9.0
        with pytest.raises(ValueError, match="Нельзя извлечь корень из отрицательного числа"):
            Operations.sqrt(number)

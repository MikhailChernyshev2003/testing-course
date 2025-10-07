import pytest
import math
from src.calculator import Calculator


class TestCalculator:
    def setup_method(self):
        self.calculator = Calculator()

    def test_add_positive_numbers(self):
        a, b = 2.5, 3.7
        expected = 6.2
        result = self.calculator.add(a, b)
        assert result == expected

    def test_divide_by_zero_raises_error(self):
        a, b = 10.0, 0.0
        with pytest.raises(ZeroDivisionError, match="Деление на ноль недопустимо"):
            self.calculator.divide(a, b)

    def test_sqrt_negative_number_raises_error(self):
        number = -9.0
        with pytest.raises(ValueError, match="Нельзя извлечь корень из отрицательного числа"):
            self.calculator.sqrt(number)

    def test_invalid_input_type_raises_error(self):
        with pytest.raises(ValueError, match="Ожидалось число"):
            self.calculator.add("1", 2)

    def test_nan_input_raises_error(self):
        with pytest.raises(ValueError, match="Число не может быть NaN"):
            self.calculator.add(math.nan, 1)

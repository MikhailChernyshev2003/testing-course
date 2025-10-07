import pytest
import math
from src.validators import Validators


class TestValidators:
    def test_validate_numbers_with_valid_numbers(self):
        numbers = (1, 2.5, -3.7, 0)
        Validators.validate_numbers(*numbers)

    def test_validate_numbers_with_invalid_type_raises_error(self):
        with pytest.raises(ValueError, match="Ожидалось число"):
            Validators.validate_numbers("1")

    def test_validate_numbers_with_nan_raises_error(self):
        with pytest.raises(ValueError, match="Число не может быть NaN"):
            Validators.validate_numbers(math.nan)

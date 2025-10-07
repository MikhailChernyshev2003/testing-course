import math
from typing import Union


class Validators:
    @staticmethod
    def validate_numbers(*numbers: Union[int, float]) -> None:
        for number in numbers:
            if not isinstance(number, (int, float)):
                raise ValueError(f"Ожидалось число, получен {type(number).__name__}")
            if math.isnan(number):
                raise ValueError("Число не может быть NaN")
            if math.isinf(number):
                raise ValueError("Число не может быть бесконечным")

    @staticmethod
    def validate_positive_number(number: Union[int, float]) -> None:
        Validators.validate_numbers(number)
        if number <= 0:
            raise ValueError("Число должно быть положительным")

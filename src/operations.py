import math


class Operations:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Деление на ноль недопустимо")
        return a / b

    @staticmethod
    def power(base: float, exponent: float) -> float:
        return base ** exponent

    @staticmethod
    def sqrt(number: float) -> float:
        if number < 0:
            raise ValueError("Нельзя извлечь корень из отрицательного числа")
        return math.sqrt(number)

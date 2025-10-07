from .operations import Operations
from .validators import Validators


class Calculator:
    def __init__(self):
        self.operations = Operations()
        self.validators = Validators()

    def add(self, a: float, b: float) -> float:
        self.validators.validate_numbers(a, b)
        return self.operations.add(a, b)

    def subtract(self, a: float, b: float) -> float:
        self.validators.validate_numbers(a, b)
        return self.operations.subtract(a, b)

    def multiply(self, a: float, b: float) -> float:
        self.validators.validate_numbers(a, b)
        return self.operations.multiply(a, b)

    def divide(self, a: float, b: float) -> float:
        self.validators.validate_numbers(a, b)
        return self.operations.divide(a, b)

    def power(self, base: float, exponent: float) -> float:
        self.validators.validate_numbers(base, exponent)
        return self.operations.power(base, exponent)

    def sqrt(self, number: float) -> float:
        self.validators.validate_numbers(number)
        return self.operations.sqrt(number)

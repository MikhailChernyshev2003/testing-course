import math
from typing import List, Union


class Statistics:
    @staticmethod
    def mean(numbers: List[float]) -> float:
        if not numbers:
            raise ValueError("Список чисел не может быть пустым")
        return sum(numbers) / len(numbers)

    @staticmethod
    def median(numbers: List[float]) -> float:
        if not numbers:
            raise ValueError("Список чисел не может быть пустым")
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        if n % 2 == 0:
            return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
        else:
            return sorted_numbers[n//2]

    @staticmethod
    def mode(numbers: List[float]) -> List[float]:
        if not numbers:
            raise ValueError("Список чисел не может быть пустым")
        frequency = {}
        for num in numbers:
            frequency[num] = frequency.get(num, 0) + 1
        max_freq = max(frequency.values())
        return [num for num, freq in frequency.items() if freq == max_freq]

    @staticmethod
    def standard_deviation(numbers: List[float]) -> float:
        if len(numbers) < 2:
            raise ValueError("Для вычисления стандартного отклонения нужно минимум 2 числа")
        mean_val = Statistics.mean(numbers)
        variance = sum((x - mean_val) ** 2 for x in numbers) / (len(numbers) - 1)
        return math.sqrt(variance)

    @staticmethod
    def variance(numbers: List[float]) -> float:
        if len(numbers) < 2:
            raise ValueError("Для вычисления дисперсии нужно минимум 2 числа")
        mean_val = Statistics.mean(numbers)
        return sum((x - mean_val) ** 2 for x in numbers) / (len(numbers) - 1)

    @staticmethod
    def range_value(numbers: List[float]) -> float:
        if not numbers:
            raise ValueError("Список чисел не может быть пустым")
        return max(numbers) - min(numbers)

    @staticmethod
    def percentile(numbers: List[float], p: float) -> float:
        if not numbers:
            raise ValueError("Список чисел не может быть пустым")
        if not 0 <= p <= 100:
            raise ValueError("Процентиль должен быть от 0 до 100")
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        k = (n - 1) * p / 100
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            return sorted_numbers[int(k)]
        d0 = sorted_numbers[int(f)] * (c - k)
        d1 = sorted_numbers[int(c)] * (k - f)
        return d0 + d1


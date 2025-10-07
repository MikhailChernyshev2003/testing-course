import math
from typing import Union


class Trigonometry:
    @staticmethod
    def sin(angle_degrees: float) -> float:
        return math.sin(math.radians(angle_degrees))

    @staticmethod
    def cos(angle_degrees: float) -> float:
        return math.cos(math.radians(angle_degrees))

    @staticmethod
    def tan(angle_degrees: float) -> float:
        angle_rad = math.radians(angle_degrees)
        if abs(math.cos(angle_rad)) < 1e-10:
            raise ValueError("Тангенс не определен для угла 90° + n*180°")
        return math.tan(angle_rad)

    @staticmethod
    def asin(value: float) -> float:
        if not -1 <= value <= 1:
            raise ValueError("Арксинус определен только для значений от -1 до 1")
        return math.degrees(math.asin(value))

    @staticmethod
    def acos(value: float) -> float:
        if not -1 <= value <= 1:
            raise ValueError("Арккосинус определен только для значений от -1 до 1")
        return math.degrees(math.acos(value))

    @staticmethod
    def atan(value: float) -> float:
        return math.degrees(math.atan(value))

    @staticmethod
    def atan2(y: float, x: float) -> float:
        return math.degrees(math.atan2(y, x))

    @staticmethod
    def degrees_to_radians(degrees: float) -> float:
        return math.radians(degrees)

    @staticmethod
    def radians_to_degrees(radians: float) -> float:
        return math.degrees(radians)

    @staticmethod
    def law_of_cosines(side_a: float, side_b: float, angle_c_degrees: float) -> float:
        if side_a < 0 or side_b < 0:
            raise ValueError("Стороны не могут быть отрицательными")
        angle_c_rad = math.radians(angle_c_degrees)
        return math.sqrt(side_a**2 + side_b**2 - 2*side_a*side_b*math.cos(angle_c_rad))

    @staticmethod
    def law_of_sines_side(side_a: float, angle_a_degrees: float, angle_b_degrees: float) -> float:
        if side_a < 0:
            raise ValueError("Сторона не может быть отрицательной")
        if angle_a_degrees <= 0 or angle_b_degrees <= 0:
            raise ValueError("Углы должны быть положительными")
        angle_a_rad = math.radians(angle_a_degrees)
        angle_b_rad = math.radians(angle_b_degrees)
        return side_a * math.sin(angle_b_rad) / math.sin(angle_a_rad)


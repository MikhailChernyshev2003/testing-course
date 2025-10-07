import math
from typing import Tuple, Union


class Geometry:
    @staticmethod
    def circle_area(radius: float) -> float:
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return math.pi * radius ** 2

    @staticmethod
    def circle_circumference(radius: float) -> float:
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return 2 * math.pi * radius

    @staticmethod
    def rectangle_area(length: float, width: float) -> float:
        if length < 0 or width < 0:
            raise ValueError("Длина и ширина не могут быть отрицательными")
        return length * width

    @staticmethod
    def rectangle_perimeter(length: float, width: float) -> float:
        if length < 0 or width < 0:
            raise ValueError("Длина и ширина не могут быть отрицательными")
        return 2 * (length + width)

    @staticmethod
    def triangle_area(base: float, height: float) -> float:
        if base < 0 or height < 0:
            raise ValueError("Основание и высота не могут быть отрицательными")
        return 0.5 * base * height

    @staticmethod
    def triangle_perimeter(side1: float, side2: float, side3: float) -> float:
        if side1 < 0 or side2 < 0 or side3 < 0:
            raise ValueError("Стороны не могут быть отрицательными")
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise ValueError("Треугольник с такими сторонами не существует")
        return side1 + side2 + side3

    @staticmethod
    def heron_formula(side1: float, side2: float, side3: float) -> float:
        if side1 < 0 or side2 < 0 or side3 < 0:
            raise ValueError("Стороны не могут быть отрицательными")
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise ValueError("Треугольник с такими сторонами не существует")
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    @staticmethod
    def distance_between_points(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    @staticmethod
    def sphere_volume(radius: float) -> float:
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return (4/3) * math.pi * radius ** 3

    @staticmethod
    def sphere_surface_area(radius: float) -> float:
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return 4 * math.pi * radius ** 2


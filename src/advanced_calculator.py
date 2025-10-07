from .calculator import Calculator
from .statistics import Statistics
from .geometry import Geometry
from .trigonometry import Trigonometry
from .validators import Validators


class AdvancedCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.statistics = Statistics()
        self.geometry = Geometry()
        self.trigonometry = Trigonometry()
        self.validators = Validators()

    def mean(self, numbers: list) -> float:
        self.validators.validate_numbers(*numbers)
        return self.statistics.mean(numbers)

    def median(self, numbers: list) -> float:
        self.validators.validate_numbers(*numbers)
        return self.statistics.median(numbers)

    def mode(self, numbers: list) -> list:
        self.validators.validate_numbers(*numbers)
        return self.statistics.mode(numbers)

    def standard_deviation(self, numbers: list) -> float:
        self.validators.validate_numbers(*numbers)
        return self.statistics.standard_deviation(numbers)

    def variance(self, numbers: list) -> float:
        self.validators.validate_numbers(*numbers)
        return self.statistics.variance(numbers)

    def range_value(self, numbers: list) -> float:
        self.validators.validate_numbers(*numbers)
        return self.statistics.range_value(numbers)

    def percentile(self, numbers: list, p: float) -> float:
        self.validators.validate_numbers(*numbers)
        return self.statistics.percentile(numbers, p)

    def circle_area(self, radius: float) -> float:
        self.validators.validate_numbers(radius)
        return self.geometry.circle_area(radius)

    def circle_circumference(self, radius: float) -> float:
        self.validators.validate_numbers(radius)
        return self.geometry.circle_circumference(radius)

    def rectangle_area(self, length: float, width: float) -> float:
        self.validators.validate_numbers(length, width)
        return self.geometry.rectangle_area(length, width)

    def rectangle_perimeter(self, length: float, width: float) -> float:
        self.validators.validate_numbers(length, width)
        return self.geometry.rectangle_perimeter(length, width)

    def triangle_area(self, base: float, height: float) -> float:
        self.validators.validate_numbers(base, height)
        return self.geometry.triangle_area(base, height)

    def triangle_perimeter(self, side1: float, side2: float, side3: float) -> float:
        self.validators.validate_numbers(side1, side2, side3)
        return self.geometry.triangle_perimeter(side1, side2, side3)

    def heron_formula(self, side1: float, side2: float, side3: float) -> float:
        self.validators.validate_numbers(side1, side2, side3)
        return self.geometry.heron_formula(side1, side2, side3)

    def distance_between_points(self, p1: tuple, p2: tuple) -> float:
        self.validators.validate_numbers(p1[0], p1[1], p2[0], p2[1])
        return self.geometry.distance_between_points(p1, p2)

    def sphere_volume(self, radius: float) -> float:
        self.validators.validate_numbers(radius)
        return self.geometry.sphere_volume(radius)

    def sphere_surface_area(self, radius: float) -> float:
        self.validators.validate_numbers(radius)
        return self.geometry.sphere_surface_area(radius)

    def sin(self, angle_degrees: float) -> float:
        self.validators.validate_numbers(angle_degrees)
        return self.trigonometry.sin(angle_degrees)

    def cos(self, angle_degrees: float) -> float:
        self.validators.validate_numbers(angle_degrees)
        return self.trigonometry.cos(angle_degrees)

    def tan(self, angle_degrees: float) -> float:
        self.validators.validate_numbers(angle_degrees)
        return self.trigonometry.tan(angle_degrees)

    def asin(self, value: float) -> float:
        self.validators.validate_numbers(value)
        return self.trigonometry.asin(value)

    def acos(self, value: float) -> float:
        self.validators.validate_numbers(value)
        return self.trigonometry.acos(value)

    def atan(self, value: float) -> float:
        self.validators.validate_numbers(value)
        return self.trigonometry.atan(value)

    def atan2(self, y: float, x: float) -> float:
        self.validators.validate_numbers(y, x)
        return self.trigonometry.atan2(y, x)

    def degrees_to_radians(self, degrees: float) -> float:
        self.validators.validate_numbers(degrees)
        return self.trigonometry.degrees_to_radians(degrees)

    def radians_to_degrees(self, radians: float) -> float:
        self.validators.validate_numbers(radians)
        return self.trigonometry.radians_to_degrees(radians)

    def law_of_cosines(self, side_a: float, side_b: float, angle_c_degrees: float) -> float:
        self.validators.validate_numbers(side_a, side_b, angle_c_degrees)
        return self.trigonometry.law_of_cosines(side_a, side_b, angle_c_degrees)

    def law_of_sines_side(self, side_a: float, angle_a_degrees: float, angle_b_degrees: float) -> float:
        self.validators.validate_numbers(side_a, angle_a_degrees, angle_b_degrees)
        return self.trigonometry.law_of_sines_side(side_a, angle_a_degrees, angle_b_degrees)


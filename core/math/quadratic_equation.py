import math
from typing import Optional, List


def solve_quadratic_equation(a: float, b: float, c: float) -> Optional[List[float]]:
	discriminant = get_discriminant(a, b, c)

	if discriminant > 0:
		discriminant = math.sqrt(discriminant)
		return get_two_components(a, b, discriminant)
	if discriminant == 0:
		discriminant = math.sqrt(discriminant)
		return get_one_component(a, b, discriminant)
	else:
		return None


def get_discriminant(a: float, b: float, c: float) -> float:
	return (b ** 2) - (4 * a * c)


def get_two_components(a: float, b: float, d: float) -> List[float]:
	x1 = (-b - d) / (2 * a)
	x2 = (-b + d) / (2 * a)

	return [x1, x2]


def get_one_component(a: float, b: float, d: float) -> List[float]:
	x = (-b - d) / (2 * a)
	return [x]

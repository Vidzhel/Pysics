import math
from typing import List

from core.math.vector2d import Vector2d


def get_one_inter_point_circle_circle(first_circle: "Circle", second_circle: "Circle") -> List[
	Vector2d]:
	point_direction = (second_circle.center - first_circle.center).normalize()
	point = first_circle.center.add_scaled_vector(point_direction, first_circle.radius)

	return [point]


def get_two_inter_points_circle_circle(first_circle: "Circle", second_circle: "Circle") \
		-> List[Vector2d]:
	# https://planetcalc.com/8098/
	r1 = first_circle.radius
	r2 = second_circle.radius
	d = r1 + r2

	center1 = first_circle.center
	center2 = second_circle.center

	a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
	h = math.sqrt(r1 ** 2 - a ** 2)
	middle_point = center1.add_vector(center1.subtract_vector(center2).scale(a / d))

	p1_x = middle_point.x + h / d * (center2.y - center1.y)
	p1_y = middle_point.x - h / d * (center2.x - center1.x)

	p2_x = middle_point.x - h / d * (center2.y - center1.y)
	p2_y = middle_point.x + h / d * (center2.x - center1.x)

	return [Vector2d(p1_x, p1_y), Vector2d(p2_x, p2_y)]

from typing import Tuple

from core.math.vector2d import Vector2d


def is_intersect_convex_convex(first_polygon: "ConvexPolygon", second_polygon: "ConvexPolygon") -> bool:
	"""Uses separated axis theorem to determinate ether two polygons are colliding or not"""

	if check_shadows(first_polygon, second_polygon) and check_shadows(second_polygon, first_polygon):
		return True

	return False


def is_intersect_convex_concave(convex: "ConvexPolygon", concave: "ConcavePolygon") -> bool:
	"""Uses separated axis theorem to determinate ether two polygons are colliding or not"""
	triangulated_concave = concave.triangles

	for concave_part in triangulated_concave:
		if not check_shadows(concave_part, convex) or not check_shadows(convex, concave_part):
			return False

	return True


def is_intersect_concave_concave(first_poly: "ConcavePolygon", second_poly: "ConcavePolygon") -> bool:
	"""Uses separated axis theorem to determinate ether two polygons are colliding or not"""
	first_parts = first_poly.triangles
	second_poly = second_poly.triangles

	for first_part in first_parts:
		for second_part in second_poly:
			if not check_shadows(first_part, second_part) or not check_shadows(second_part, first_part):
				return False

	return True


def check_shadows(first: "BaseGeometryObject", second: "BaseGeometryObject", get_first_shadow_func,
                  get_second_shadow_func) -> bool:
	polygons = (first, second)

	for poly in polygons:
		for side in first.sides:
			normal = side.get_perpendicular()
			normal_vector = normal.get_vector()

			first_min_shadow, first_max_shadow = get_first_shadow_func(first, normal_vector)
			second_min_shadow, second_max_shadow = get_second_shadow_func(second, normal_vector)

			if not (second_max_shadow >= first_min_shadow and first_max_shadow >= second_min_shadow):
				return False

	return True


def get_shadow_circle(circle: "")


def get_shadow_polygon(poly: "BasePolygon", normal: Vector2d) -> Tuple[float, float]:
	min_shadow = float("inf")
	max_shadow = -float("inf")
	for point in poly.points:
		product = normal.dot_product(point)

		min_shadow = min(min_shadow, product)
		max_shadow = max(min_shadow, product)

	return min_shadow, max_shadow


def get_distance_line_polygon(line: "Line", poly: "BasePolygon"):
	pass

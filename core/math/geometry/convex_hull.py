from typing import List, Set

from core.math.geometry.geometry_objects import ConvexPolygon, Line
from core.math.vector2d import Vector2d


def create_convex_hull(points: Set[Vector2d]) -> ConvexPolygon:
	"""Uses Graham scan algorithm to create a convex hull form the given points"""
	points = list(points)

	lower_point = get_lower_point(points)
	points = sort_clockwise(points, lower_point)

	convex_hull_points = [lower_point]
	points_count = len(points)

	# make the list of points starts from the lower_point
	lower_point_index = int()

	for i in range(points_count):
		if points[i] == lower_point:
			lower_point_index = i

	points = points[lower_point_index + 1:] + points[: lower_point_index]

	for i in range(points_count):
		last_last_point = convex_hull_points[-2]
		last_point = convex_hull_points[-1]

		next_point = points[i]

		first_line = last_point - last_last_point
		second_line = next_point - last_point

		cross_product = first_line.cross(second_line)
		if cross_product >= 0:
			del convex_hull_points[-1]

		convex_hull_points.append(next_point)

	return ConvexPolygon(convex_hull_points)


def sort_clockwise(points: List[Vector2d], lower_point: Vector2d = None) -> List[Vector2d]:
	if not lower_point:
		lower_point = get_lower_point(points)

	points.sort(key=lambda point: Line(lower_point, point).get_slope())

	return points


def get_lower_point(points: List[Vector2d]) -> Vector2d:
	lower_point = points[0]

	for point in points:

		if point.y < lower_point.y:
			lower_point = point

		elif point.y == lower_point.y and point.x < lower_point.x:
			lower_point = point

	return lower_point

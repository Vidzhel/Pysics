from typing import List, Set

from core.math.vector2d import Vector2d


def polygons_difference(first_polygon_points: List[Vector2d], second_polygons_points: List[Vector2d]) -> Set[
	Vector2d]:
	new_points = set()

	for first_point in first_polygon_points:
		for second_point in second_polygons_points:
			new_points.add(first_point - second_point)

	return new_points

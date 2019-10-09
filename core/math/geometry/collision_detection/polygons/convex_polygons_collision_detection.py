from typing import Optional, Tuple, List

from core.math.geometry.collision_detection.collision_data import CollisionData
from core.math.geometry.collision_detection.line_polygon.line_polygon_collision_detection import \
	get_inter_data_segment_convexpolygon
from core.math.vector2d import Vector2d


def get_inter_data_convexpolygon_convexpolygon(first_poly: "ConvexPolygon",
                                               second_poly: "ConvexPolygon") -> Optional[CollisionData]:
	penetration_length: float = 0.0
	points: List[Vector2d] = []

	# TODO delete the part if optimization is necessary
	for diagonal in first_poly.diagonals:
		diagonal_inter_data = get_inter_data_segment_convexpolygon(diagonal, second_poly)
		if diagonal_inter_data:
			penetration_length = diagonal_inter_data[1]

	for side in first_poly.sides:
		side_inter_data = get_inter_data_segment_convexpolygon(side, second_poly)
		if side_inter_data:
			points.extend(side_inter_data[0])
			if penetration_length == 0.0:
				penetration_length = side_inter_data[1]

	if len(points) == 0:
		return None

	return CollisionData(points, penetration_length)


def get_inter_data_convexpolygon_rectangle(poly: "ConvexPolygon", rect: "Rectangle") -> Optional[
	CollisionData]:
	return get_inter_data_convexpolygon_convexpolygon(rect, poly)


def get_inter_data_rectangle_convexpolygon(rect: "Rectangle", poly: "ConvexPolygon") -> Optional[
	CollisionData]:
	return get_inter_data_convexpolygon_convexpolygon(rect, poly)


def get_inter_data_convexpolygon_triangle(poly: "ConvexPolygon", triangle: "Triangle") -> Optional[
	CollisionData]:
	return get_inter_data_convexpolygon_convexpolygon(poly, triangle)


def get_inter_data_triangle_convexpolygon(triangle: "Triangle", poly: "ConvexPolygon") -> Optional[
	CollisionData]:
	return get_inter_data_convexpolygon_convexpolygon(poly, triangle)


def get_inter_data_rectangle_rectangle(first_rect: "Rectangle", second_rect: "Rectangle") -> \
		Optional[Tuple[List[Vector2d], float]]:
	return get_inter_data_convexpolygon_convexpolygon(first_rect, second_rect)


def get_inter_data_rectangle_triangle(rect: "Rectangle", triangle: "Triangle") -> Optional[CollisionData]:
	return get_inter_data_convexpolygon_convexpolygon(rect, triangle)


def get_inter_data_triangle_rectangle(triangle: "Triangle", rect: "Rectangle") -> Optional[CollisionData]:
	return get_inter_data_convexpolygon_convexpolygon(rect, triangle)


def get_inter_data_triangle_triangle(first_triangle: "Triangle",
                                     second_triangle: "Triangle") -> Optional[Tuple[List[Vector2d], float]]:
	return get_inter_data_convexpolygon_convexpolygon(first_triangle, second_triangle)

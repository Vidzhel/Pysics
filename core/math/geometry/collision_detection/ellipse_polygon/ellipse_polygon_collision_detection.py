from typing import Union, Optional, Tuple, List

from core.math.average import average
from core.math.geometry.collision_detection.line_ellipse.line_ellipse_collision_detection import \
	get_inter_data_line_circle
from core.math.vector2d import Vector2d


def get_inter_data_circle_polygon(circle: "Circle", poly: "ConvexPolygon") \
		-> Optional[Tuple[List[Vector2d], float]]:
	return get_inter_data_polygon(circle, poly)


def get_inter_data_polygon(ellipse: Union["Circle", "Ellipse"], poly: "ConvexPolygon") \
		-> Optional[Tuple[List[Vector2d], float]]:
	penetration_length: float = 0.0
	points: List[Vector2d] = []

	# TODO delete the part if optimization is necessary
	for diagonal in poly.diagonals:
		diagonal_inter_data = get_inter_data_line_circle(diagonal, ellipse)
		if diagonal_inter_data:
			penetration_length = diagonal_inter_data.penetration_depth

	for side in poly.sides:
		side_inter_data = get_inter_data_line_circle(side, ellipse)
		if side_inter_data:
			points.extend(side_inter_data.intersection_points)
			if penetration_length == 0.0:
				penetration_length = average(penetration_length, side_inter_data[1])

	if len(points) == 0:
		return None

	return points, penetration_length


def get_inter_data_circle_rectangle(circle: "Circle", rect: "Rectangle") -> Optional[
	Tuple[Vector2d, float, float]]:
	return get_inter_data_circle_polygon(circle, rect)


def get_inter_data_rectangle_circle(rect: "Rectangle", circle: "Circle") -> Optional[
	Tuple[Vector2d, float, float]]:
	return get_inter_data_circle_polygon(circle, rect)


def get_inter_data_polygon_circle(poly: "ConvexPolygon", circle: "Circle") -> Optional[
	Tuple[Vector2d, float, float]]:
	return get_inter_data_circle_polygon(circle, poly)


def get_inter_data_circle_triangle(circle: "Circle", triangle: "Triangle") -> Optional[
	Tuple[Vector2d, float, float]]:
	return get_inter_data_circle_polygon(circle, triangle)


def get_inter_data_triangle_circle(triangle: "Triangle", circle: "Circle") -> Optional[
	Tuple[Vector2d, float, float]]:
	return get_inter_data_circle_polygon(circle, triangle)


# "Ellipse"

def get_inter_data_ellipse_rectangle(ellipse: "Ellipse", rect: "Rectangle") -> Optional[
	Tuple[List[Vector2d], float]]:
	return get_inter_data_polygon(ellipse, rect)


def get_inter_data_rectangle_ellipse(rect: "Rectangle", ellipse: "Ellipse") -> Optional[
	Tuple[Vector2d, float, float]]:
	return get_inter_data_polygon(ellipse, rect)


def get_inter_data_ellipse_polygon(ellipse: "Ellipse", poly: "ConvexPolygon") -> Optional[
	Tuple[List[Vector2d], float]]:
	return get_inter_data_polygon(ellipse, poly)


def get_inter_data_polygon_ellipse(poly: "ConvexPolygon", ellipse: "Ellipse") -> Optional[
	Tuple[List[Vector2d], float]]:
	return get_inter_data_polygon(ellipse, poly)


def get_inter_data_ellipse_triangle(ellipse: "Ellipse", triangle: "Triangle") -> Optional[
	Tuple[Vector2d, float, float]]:
	return get_inter_data_polygon(ellipse, triangle)


def get_inter_data_triangle_ellipse(triangle: "Triangle", ellipse: "Ellipse") -> Optional[
	Tuple[Vector2d, float, float]]:
	return get_inter_data_polygon(ellipse, triangle)

"""Uses the ellipse and the circle equations to get points of intersection
between line and ellipse"""

from typing import Union, Optional, List

from core.math.quadratic_equation import solve_quadratic_equation
from core.math.vector2d import Vector2d


def get_circle_line_intersection_points(line: Union["Segment", "Line"], circle: "Circle") -> Optional[
	List[Vector2d]]:
	return get_ellipse_shape_line_intersection_points(line, circle, get_x_coord_line_circle)


def get_ellipse_line_intersection_points(line: Union["Segment", "Line"], ellipse: "Ellipse") -> Optional[
	List[Vector2d]]:
	return get_ellipse_shape_line_intersection_points(line, ellipse, get_x_coord_line_ellipse)


def get_ellipse_shape_line_intersection_points(line: Union["Segment", "Line"],
                                               ellipse: Union["Circle", "Ellipse"], get_x_coord_func) -> \
		Optional[List[Vector2d]]:
	inter_points_x_coordinates = get_x_coord_func(line, ellipse)
	if not inter_points_x_coordinates:
		return None

	int_points_y_coordinates = get_y_coordinates_line(line, inter_points_x_coordinates)

	points: List[Vector2d] = []
	for x, y in zip(inter_points_x_coordinates, int_points_y_coordinates):
		points.append(Vector2d(x, y))

	for i in range(len(points)):
		if not line.is_point_belongs(points[i]):
			del points[i]

	return points


def get_x_coord_line_circle(line: "Segment", circle: "Circle") -> Optional[List[float]]:
	line_slope = line.get_slope()
	line_y_intercept = line.get_y_intercept(line_slope)

	radius = circle.radius
	x_center = circle.center.x
	y_center = circle.center.y

	A = line_slope ** 2 + 1
	B = line_slope * line_y_intercept - line_slope * y_center - x_center
	C = y_center ** 2 - radius ** 2 + x_center ** 2 - 2 * line_y_intercept * y_center + y_center ** 2

	return solve_quadratic_equation(A, B, C)


def get_y_coordinates_line(line: "Segment", inter_points_x_coordinates: "List[float]") -> List[float]:
	int_points_y_coordinates: List[float] = []
	slope = line.get_slope()

	for x in inter_points_x_coordinates:
		y = slope * x + line.get_y_intercept(slope)
		int_points_y_coordinates.append(y)

	return int_points_y_coordinates


def get_x_coord_line_ellipse(line: Union["Segment", "Line"], ellipse: "Ellipse") -> Optional[List[float]]:
	line_slope = line.get_slope()
	line_y_intercept = line.get_y_intercept(line_slope)

	horizontal_radius = ellipse.horizontal_radius
	vertical_radius = ellipse.vertical_radius

	A = horizontal_radius ** 2 * line_slope ** 2 + vertical_radius ** 2
	B = 2 * horizontal_radius ** 2 * line_slope * line_y_intercept
	C = horizontal_radius ** 2 * (line_y_intercept ** 2 - vertical_radius ** 2)

	return solve_quadratic_equation(A, B, C)

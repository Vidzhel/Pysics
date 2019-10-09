from typing import Union, List

from core.math.geometry.geometry_objects import Segment
from core.math.vector2d import Vector2d
from .line_ellipse_inter_points import get_ellipse_line_intersection_points


def get_penttr_depth_one_point_line_ellipse(point_of_intersection: Vector2d, line: Union["Segment", "Line"],
                                            shape_center: Vector2d) -> float:
	first_point_to_center_dist = (shape_center - line.first_point).get_magnitude()
	second_point_to_center_dist = (shape_center - line.second_point).get_magnitude()

	if second_point_to_center_dist > first_point_to_center_dist:
		penetration_depth = (point_of_intersection - line.first_point).get_magnitude()
	else:
		penetration_depth = (point_of_intersection - line.second_point).get_magnitude()

	return penetration_depth


def get_penttr_depth_two_points_line_ellipse(point_of_intersection: List[Vector2d],
                                             ellipse: "Ellipse") -> float:
	# To get penetration of the line we will find middle point of line that inside the shape
	# and the distance from the middle point to a border
	#
	# To find the point on the border
	# we will draw the line from the middle point through the border,
	# the direction of the line will be the same as the direction of the
	# line from the center of the ellipse to the middle point,
	# than we will find another point of intersection
	middle_point = (Segment(point_of_intersection[0], point_of_intersection[1])).get_middle_point()

	direction_of_line = (Segment(middle_point, ellipse.center)).get_direction()
	scalar = max(ellipse.horizontal_radius, ellipse.vertical_radius)
	line_through_border = Segment(middle_point,
	                              middle_point.add_scaled_vector(direction_of_line, scalar))

	point_on_the_border = get_ellipse_line_intersection_points(line_through_border, ellipse)

	if len(point_on_the_border) != 1:
		raise Exception("Can't find line-ellipse penetration depth (when draw line through border" +
		                "get " + str(point_on_the_border) + " expected one point)")

	penetration_depth = (point_on_the_border[0] - middle_point).get_magnitude()
	return penetration_depth

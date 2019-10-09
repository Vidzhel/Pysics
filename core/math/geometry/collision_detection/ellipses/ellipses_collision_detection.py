from typing import Optional, Union, Tuple

from core.math.geometry.collision_detection.collision_data import CollisionData
from core.math.geometry.collision_detection.line_ellipse.line_ellipse_collision_detection import \
	(get_inter_data_segment_circle, get_inter_data_segment_ellipse)
from core.math.geometry.geometry_objects import Segment
from .ellipses_intersection_points import *


def get_inter_data_circle_circle(first_circle: "Circle", second_circle: "Circle") -> Optional[CollisionData]:
	distance_between_centres = (first_circle.center - second_circle.center).get_magnitude()
	radius = first_circle.radius + second_circle.radius
	penetration_depth = radius - distance_between_centres

	if penetration_depth < 0:
		return None
	elif penetration_depth == 0:
		points = get_one_inter_point_circle_circle(first_circle, second_circle)
	else:
		points = get_two_inter_points_circle_circle(first_circle, second_circle)

	return CollisionData(points, penetration_depth)


def get_inter_data_circle_ellipse(circle: "Circle", ellipse: "Ellipse") -> Optional[CollisionData]:
	data = get_inter_ellipse_ellipse(circle, ellipse, get_inter_data_segment_circle,
	                                 get_inter_data_segment_ellipse)
	return CollisionData([data[0]], data[2])


def get_inter_data_ellipse_circle(ellipse: "Ellipse", circle: "Circle") -> Optional[CollisionData]:
	data = get_inter_ellipse_ellipse(circle, ellipse, get_inter_data_segment_circle,
	                                 get_inter_data_segment_ellipse)

	return CollisionData([data[1]], data[2])


def get_inter_data_ellipse_ellipse(first_ellipse: "Ellipse", second_ellipse: "Ellipse") -> Optional[
	CollisionData]:
	data = get_inter_ellipse_ellipse(first_ellipse, second_ellipse, get_inter_data_segment_ellipse,
	                                 get_inter_data_segment_ellipse)

	return CollisionData([data[0]], data[2])


def get_inter_ellipse_ellipse(first_shape: Union["Circle", "Ellipse"],
                              second_shape: Union["Circle", "Ellipse"], segment_first_inter_func,
                              segment_second_inter_func) -> Tuple[Vector2d, Vector2d, float]:
	segment_through_centers = Segment(first_shape.center, second_shape.center)

	circle_inter_data = segment_first_inter_func(segment_through_centers, first_shape)
	ellipse_inter_data = segment_second_inter_func(segment_through_centers, second_shape)

	circle_inter_point = circle_inter_data.intersection_points[0]
	ellipse_inter_point = ellipse_inter_data.intersection_points[0]

	distance_to_circle_inter_point = (circle_inter_point - first_shape.center).get_magnitude()
	distance_to_ellipse_inter_point = (ellipse_inter_point - second_shape.center).get_magnitude()

	# If an ellipse and a circle intersect with each other than segment-ellipse intersection point should lay
	# closer or at the same place as segment-circle intersection point
	if distance_to_ellipse_inter_point > distance_to_circle_inter_point:
		return None

	penetration_depth = (ellipse_inter_point - circle_inter_point).get_magnitude()

	return circle_inter_point, ellipse_inter_point, penetration_depth

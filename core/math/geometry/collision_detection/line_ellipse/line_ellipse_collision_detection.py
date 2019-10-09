from typing import Union, Optional

from core.math.geometry.collision_detection.collision_data import CollisionData
from .line_ellipse_inter_points import (get_circle_line_intersection_points,
                                        get_ellipse_line_intersection_points)
from .line_ellipse_penetration import (get_penttr_depth_one_point_line_ellipse,
                                       get_penttr_depth_two_points_line_ellipse)


#########################
# "Circle"
#########################

def get_inter_data_line_shape_circle(segment: Union["Segment", "Line", "Ray"], circle: "Circle") -> Optional[
	CollisionData]:
	distance_to_center = segment.get_distance_to_point(circle.center)

	if distance_to_center > circle.radius:
		return None

	penetration_depth = circle.radius - distance_to_center

	points = get_circle_line_intersection_points(segment, circle)

	return CollisionData(points, penetration_depth)


def get_inter_data_segment_circle(circle: "Circle", segment: "Segment") -> Optional[CollisionData]:
	return get_inter_data_line_shape_circle(segment, circle)


def get_inter_data_circle_segment(circle: "Circle", segment: "Segment") -> Optional[CollisionData]:
	return get_inter_data_segment_circle(segment, circle)


def get_inter_data_line_circle(line: "Line", circle: "Circle") -> Optional[CollisionData]:
	return get_inter_data_line_shape_circle(line, circle)


def get_inter_data_circle_line(circle: "Circle", line: "Line") -> Optional[CollisionData]:
	return get_inter_data_line_circle(line, circle)


def get_inter_data_ray_circle(ray: "Ray", circle: "Circle") -> Optional[CollisionData]:
	return get_inter_data_line_shape_circle(ray, circle)


def get_inter_data_circle_ray(circle: "Circle", ray: "Ray") -> Optional[CollisionData]:
	return get_inter_data_ray_circle(ray, circle)


#########################
# Ellipse
#########################

def get_inter_data_line_shape_ellipse(segment: Union["Segment", "Line", "Ray"], ellipse: "Ellipse") -> \
		Optional[CollisionData]:
	points = get_ellipse_line_intersection_points(segment, ellipse)

	if not points:
		return None
	elif len(points) == 2:
		penetration_depth = get_penttr_depth_two_points_line_ellipse(points, ellipse)
	else:
		penetration_depth = get_penttr_depth_one_point_line_ellipse(points[0], segment,
		                                                            ellipse.center)
	return CollisionData(points, penetration_depth)


def get_inter_data_segment_ellipse(segment: "Segment", ellipse: "Ellipse") -> Optional[CollisionData]:
	return get_inter_data_line_shape_ellipse(segment, ellipse)


def get_inter_data_ellipse_segment(ellipse: "Ellipse", segment: "Segment") -> Optional[CollisionData]:
	return get_inter_data_segment_ellipse(segment, ellipse)


def get_inter_data_line_ellipse(line: "Line", ellipse: "Ellipse") -> Optional[CollisionData]:
	return get_inter_data_line_shape_ellipse(line, ellipse)


def get_inter_data_ellipse_line(ellipse: "Ellipse", line: "Line") -> Optional[CollisionData]:
	return get_inter_data_line_ellipse(line, ellipse)


def get_inter_data_ray_ellipse(ray: "Ray", ellipse: "Ellipse") -> Optional[CollisionData]:
	return get_inter_data_line_shape_ellipse(ray, ellipse)


def get_inter_data_ellipse_ray(ellipse: "Ellipse", ray: "Ray") -> Optional[CollisionData]:
	return get_inter_data_ray_ellipse(ray, ellipse)

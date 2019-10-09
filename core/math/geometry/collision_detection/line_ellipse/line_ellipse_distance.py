from typing import Union

from .line_ellipse_inter_points import get_ellipse_line_intersection_points


def get_distance_line_circle(line: "Line", circle: "Circle") -> float:
	return get_distance_to_circle(line, circle)


def get_distance_circle_line(circle: "Circle", line: "Line") -> float:
	return get_distance_line_circle(line, circle)


def get_distance_line_ellipse(line: "Line", ellipse: "Ellipse") -> float:
	return get_distance_ray_ellipse(line, ellipse)


def get_distance_to_ellipse_line(ellipse: "Ellipse", line: "Line") -> float:
	return get_distance_line_circle(line, ellipse)


def get_distance_ray_circle(ray: "Ray", circle: "Circle") -> float:
	return get_distance_to_circle(ray, circle)


def get_distance_circle_ray(circle: "Circle", ray: "Ray") -> float:
	return get_distance_ray_circle(ray, circle)


def get_distance_ray_ellipse(ray: "Ray", ellipse: "Ellipse") -> float:
	get_distance_to_ellipse(ray, ellipse)


def get_distance_to_ellipse_ray(ellipse: "Ellipse", ray: "Ray") -> float:
	return get_distance_ray_ellipse(ray, ellipse)


def get_distance_segment_circle(ray: "Ray", circle: "Circle") -> float:
	return get_distance_to_circle(ray, circle)


def get_distance_circle_segment(circle: "Circle", ray: "Ray") -> float:
	return get_distance_ray_circle(ray, circle)


def get_distance_segment_ellipse(segment: "Segment", ellipse: "Ellipse") -> float:
	return get_distance_to_ellipse(segment, ellipse)


def get_distance_to_ellipse_segment(ellipse: "Ellipse", segment: "Segment") -> float:
	return get_distance_ray_ellipse(segment, ellipse)


def get_distance_to_ellipse(line: Union["Line", "Ray", "Segment"], ellipse: "Ellipse") -> float:
	closest_point = line.get_closest_point(ellipse.center)
	line_to_center = ellipse.center - closest_point
	points = get_ellipse_line_intersection_points(ellipse, line_to_center)

	if not points:
		return 0

	distance = (points[0] - closest_point).get_magnitude()

	return distance


def get_distance_to_circle(line: Union["Line", "Ray", "Segment"], circle: "Circle") -> float:
	distance = line.get_distance_to_point(circle) - circle.radius

	if distance < 0:
		distance = 0

	return distance

from typing import Optional

from core.math.geometry.collision_detection.collision_data import CollisionData
from .lines_inter_points import get_segments_intersection_points
from .lines_penetr_coeff import (get_penetr_line_line_coeff, get_penetr_line_ray_coeff,
                                 get_penetr_ray_ray_coeff, get_penetr_segment_ray_coeff,
                                 get_penetr_segment_line_coeff,
                                 get_penetr_segment_segment_coeff)


def get_inter_data_line_line(first_line: "Line", second_line: "Line") -> Optional[CollisionData]:
	coefficients = get_penetr_line_line_coeff(first_line, second_line)
	if not coefficients:
		return None

	intersection_point = get_segments_intersection_points(first_line, coefficients)

	return CollisionData(intersection_point)


def get_inter_data_line_ray(line: "Line", ray: "Ray") -> Optional[CollisionData]:
	coefficients = get_penetr_line_ray_coeff(line, ray)
	if not coefficients:
		return None

	intersection_point = get_segments_intersection_points(line, coefficients)

	return CollisionData(intersection_point)


def get_inter_data_ray_line(line: "Line", ray: "Ray") -> Optional[CollisionData]:
	return get_inter_data_line_ray(line, ray)


def get_inter_data_segment_line(segment: "Segment", line: "Line") -> Optional[CollisionData]:
	coefficients = get_penetr_segment_line_coeff(segment, line)
	if not coefficients:
		return None

	intersection_point = get_segments_intersection_points(segment, coefficients)

	length = segment.get_length()
	penetration_length = length - length * coefficients[0]
	penetration_length = min(penetration_length, length - penetration_length)

	return CollisionData(intersection_point, penetration_length)


def get_inter_data_line_segment(line: "Line", segment: "Segment") -> Optional[CollisionData]:
	data = get_inter_data_segment_line(segment, line)

	return data


def get_inter_data_ray_segment(ray: "Ray", segment: "Segment") -> Optional[CollisionData]:
	data = get_inter_data_segment_ray(segment, ray)

	return data


def get_inter_data_ray_ray(first_ray: "ray", second_ray: "Ray") -> Optional[CollisionData]:
	coefficients = get_penetr_ray_ray_coeff(first_ray, second_ray)
	if not coefficients:
		return None

	intersection_point = get_segments_intersection_points(first_ray, coefficients)

	return CollisionData(intersection_point)


def get_inter_data_segment_segment(first_segment: "Segment", second_segment: "Segment") -> Optional[
	CollisionData]:
	coefficients = get_penetr_segment_segment_coeff(first_segment, second_segment)
	if not coefficients:
		return None

	intersection_point = get_segments_intersection_points(first_segment, coefficients)

	length = first_segment.get_length()
	penetration_length = length - length * coefficients[0]
	penetration_length = min(penetration_length, length - penetration_length)

	return CollisionData(intersection_point, penetration_length)


def get_inter_data_segment_ray(segment: "Segment", ray: "Ray") -> Optional[CollisionData]:
	coefficients = get_penetr_segment_ray_coeff(segment, ray)
	if not coefficients:
		return None

	intersection_point = get_segments_intersection_points(segment, coefficients)

	length = segment.get_length()
	penetration_length = length - length * coefficients[0]
	penetration_length = min(penetration_length, length - penetration_length)

	return CollisionData(intersection_point, penetration_length)

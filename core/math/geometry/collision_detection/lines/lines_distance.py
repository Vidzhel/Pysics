from core.math.geometry.collision_detection.lines.is_lines_intersect import (is_intersect_line_line,
                                                                             is_intersect_line_ray,
                                                                             is_intersect_line_segment,
                                                                             is_intersect_ray_ray,
                                                                             is_intersect_ray_segment,
                                                                             is_intersect_segment_segment)


def get_distance_line_line(first_line: "Line", second_line: "Line") -> float:
	closest_point = first_line.get_closest_point(second_line.first_point)
	distance = (closest_point - second_line.first_point).get_magnitude()

	if is_intersect_line_line(first_line, second_line):
		return -distance

	return distance


def get_distance_line_ray(line: "Line", ray: "Ray") -> float:
	closest_point = line.get_closest_point(ray.first_point)
	distance = (closest_point - ray.first_point).get_magnitude()

	if is_intersect_line_ray(line, ray):
		return -distance

	return distance


def get_distance_ray_line(ray: "Ray", line: "Line") -> float:
	return get_distance_line_ray(line, ray)


def get_distance_line_segment(line: "Line", segment: "Segment") -> float:
	first_closest_point = line.get_closest_point(segment.first_point)
	second_closest_point = line.get_closest_point(segment.second_point)

	first_dist = (first_closest_point - segment.first_point).get_magnitude()
	second_dist = (second_closest_point - segment.second_point).get_magnitude()

	distance = min(first_dist, second_dist)

	if is_intersect_line_segment(line, segment):
		return -distance

	return distance


def get_distance_segment_line(segment: "Segmnet", line: "Line") -> float:
	return get_distance_line_segment(line, segment)


def get_distance_ray_ray(first_ray: "Ray", second_ray: "Ray") -> float:
	dist = (second_ray.first_point - first_ray.first_point).get_magnitude()

	if is_intersect_ray_ray(first_ray, second_ray):
		return -dist

	return dist


def get_distance_ray_segment(ray: "Ray", segment: "Segment") -> float:
	first_closest_point = ray.get_closest_point(segment.first_point)
	second_closest_point = ray.get_closest_point(segment.second_point)
	third_closest_point = segment.get_closest_point(ray.first_point)

	first_dist = (first_closest_point - segment.first_point).get_magnitude()
	second_dist = (second_closest_point - segment.second_point).get_magnitude()
	third_dist = (third_closest_point - ray.first_point).get_magnitude()

	distance = min(first_dist, second_dist, third_dist)

	if is_intersect_ray_segment(ray, segment):
		return -distance

	return distance


def get_distance_segment_ray(segment: "Segmnet", ray: "Ray") -> float:
	return get_distance_ray_segment(ray, segment)


def get_distance_segment_segment(first_segment: "Segment", second_segment: "Segment") -> float:
	first_closest_point = first_segment.get_closest_point(second_segment.first_point)
	second_closest_point = first_segment.get_closest_point(second_segment.second_point)
	third_closest_point = second_segment.get_closest_point(first_segment.first_point)
	fourth_closest_point = second_segment.get_closest_point(first_segment.second_point)

	first_dist = (first_closest_point - second_segment.first_point).get_magnitude()
	second_dist = (second_closest_point - second_segment.second_point).get_magnitude()
	third_dist = (third_closest_point - first_segment.first_point).get_magnitude()
	fourth_dist = (fourth_closest_point - first_segment.second_point).get_magnitude()

	distance = min(first_dist, second_dist, third_dist, fourth_dist)

	if is_intersect_segment_segment(first_segment, second_segment):
		return -distance

	return distance

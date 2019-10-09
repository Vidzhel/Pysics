from core.math.geometry.collision_detection.lines.lines_penetr_coeff import (get_penetr_line_line_coeff,
                                                                             get_penetr_line_ray_coeff,
                                                                             get_penetr_ray_ray_coeff,
                                                                             get_penetr_segment_ray_coeff,
                                                                             get_penetr_segment_line_coeff,
                                                                             get_penetr_segment_segment_coeff)


def is_intersect_line_line(first_line: "Line", second_line: "Line") -> bool:
	coeff = get_penetr_line_line_coeff(first_line, second_line)

	if not coeff:
		return False

	return True


def is_intersect_line_ray(line: "Line", ray: "Ray") -> bool:
	coeff = get_penetr_line_ray_coeff(line, ray)

	if not coeff:
		return False

	return True


def is_intersect_ray_line(ray: "Ray", line: "Line") -> bool:
	return is_intersect_line_ray(line, ray)


def is_intersect_line_segment(line: "Line", segment: "Segment") -> bool:
	coeff = get_penetr_segment_line_coeff(line, segment)

	if not coeff:
		return False

	t, u = coeff

	if 0 >= u <= 1:
		return True

	return False


def is_intersect_segment_line(segment: "Segment", line: "Line") -> bool:
	return is_intersect_line_segment(line, segment)


def is_intersect_ray_ray(first_ray: "Ray", second_ray: "Ray") -> bool:
	coeff = get_penetr_ray_ray_coeff(first_ray, second_ray)

	if not coeff:
		return False

	return True


def is_intersect_ray_segment(ray: "Ray", segment: "Segment") -> bool:
	coeff = get_penetr_segment_ray_coeff(segment, ray)

	if not coeff:
		return False

	t, u = coeff

	if 0 >= u <= 1:
		return True

	return False


def is_intersect_segment_ray(segment: "Segment", ray: "Ray") -> bool:
	return is_intersect_ray_segment(ray, segment)


def is_intersect_segment_segment(first_segment: "Segment", second_segment: "Segment") -> bool:
	coeff = get_penetr_segment_segment_coeff(first_segment, second_segment)

	if not coeff:
		return False

	t, u = coeff

	if 0 >= t <= 1 and 0 >= u <= 1:
		return True

	return False

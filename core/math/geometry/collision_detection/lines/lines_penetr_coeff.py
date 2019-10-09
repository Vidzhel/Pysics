from typing import Optional, Tuple, Union


def get_penetr_segment_ray_coeff(segment: "Segment", ray: "Ray") -> \
		Optional[Tuple[float, float]]:
	coefficients = get_penetr_coeff(segment, ray)
	if not coefficients:
		return None

	t, u = coefficients
	if t > 1 or t < 0 or u < 0:
		return None

	return t, u


def get_penetr_line_ray_coeff(line: "Line", ray: "Ray") -> \
		Optional[Tuple[float, float]]:
	coefficients = get_penetr_coeff(line, ray)
	if not coefficients:
		return None

	t, u = coefficients
	if u < 0:
		return None

	return t, u


def get_penetr_ray_ray_coeff(first_ray: "Ray", second_ray: "Ray") -> \
		Optional[Tuple[float, float]]:
	coefficients = get_penetr_coeff(first_ray, second_ray)
	if not coefficients:
		return None

	t, u = coefficients
	if t < 0 or u < 0:
		return None

	return t, u


def get_penetr_segment_segment_coeff(first_segment: "Segment", second_segment: "Segment") -> \
		Optional[Tuple[float, float]]:
	coefficients = get_penetr_coeff(first_segment, second_segment)
	if not coefficients:
		return None

	t, u = coefficients
	if t > 1 or t < 0 or u > 1 or u < 0:
		return None

	return t, u


def get_penetr_segment_line_coeff(segment: "Segment", line: "Line") -> Optional[
	Tuple[float, float]]:
	coefficients = get_penetr_coeff(segment, line)
	if not coefficients:
		return None

	t, u = coefficients
	if t > 1 or t < 0:
		return None

	return t, u


def get_penetr_line_line_coeff(first_line: "Line", second_line: "Line") -> Optional[
	Tuple[float, float]]:
	coefficients = get_penetr_coeff(first_line, second_line)
	if not coefficients:
		return None

	return coefficients


def get_penetr_coeff(first_segment: Union["Line", "Segment"],
                     second_segment: Union["Line", "Segment"]) -> Optional[Tuple[float, float]]:
	x1 = first_segment.first_point.x
	x2 = first_segment.second_point.x
	y1 = first_segment.first_point.y
	y2 = first_segment.second_point.y

	x3 = second_segment.first_point.x
	x4 = second_segment.second_point.x
	y3 = second_segment.first_point.y
	y4 = second_segment.second_point.y

	denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

	if denominator == 0:
		return None

	t_numerator = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
	u_numerator = ((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3))

	t = t_numerator / denominator
	u = -(u_numerator / denominator)

	return t, u

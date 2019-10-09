from typing import Optional


def get_penetr_length_line_line(cls, first_line: "Segment", second_line: "Segment") \
		-> Optional[float]:
	coefficients = cls.get_penetr_line_line_coeff(first_line, second_line)
	if not coefficients:
		return None

	length = first_line.get_length()
	penetration_length = length - length * coefficients[0]

	return penetration_length


def get_penetr_length_line_ray(cls, line: "Segment", ray: "Line") -> Optional[float]:
	coefficients = cls.get_penetr_line_ray_coeff(line, ray)
	if not coefficients:
		return None

	length = line.get_length()
	penetration_length = length - length * coefficients[0]

	return penetration_length


def get_penetr_length_ray_line(cls, ray: "Line", line: "Segment") -> Optional[float]:
	return cls.get_penetr_length_line_ray(line, ray)

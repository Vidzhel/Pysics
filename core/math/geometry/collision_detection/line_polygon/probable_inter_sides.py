from typing import List, Union


def get_probable_intersect_sides_line(poly: Union["BasePolygon"], line: "Line") -> List["Segment"]:
	lines = []

	if line.is_horizontal():
		upper_border = max(line.first_point.y, line.second_point.y)
		lower_border = min(line.first_point.y, line.second_point.y)

		for side in poly.sides:
			if lower_border <= side.first_point.y <= upper_border or lower_border <= side.second_point.y <= \
					upper_border:
				lines.append(side)


	elif line.is_vertical():
		left_border = min(line.first_point.x, line.second_point.x)
		right_border = max(line.first_point.x, line.second_point.x)

		for side in poly.sides:
			if left_border <= side.first_point.x <= right_border or left_border <= side.second_point.x <= \
					right_border:
				lines.append(side)

	return lines


def get_probable_intersect_sides_ray(poly: Union["BasePolygon"], ray: "Ray") -> List["Segment"]:
	lines = []
	ray_start = ray.first_point
	ray_direction = ray.get_direction()
	ray_direction = ray_direction.scale()

	left_border = min(ray_start.x, ray_direction.x)
	right_border = max(ray_start.x, ray_direction.x)

	upper_border = max(ray_start.y, ray_direction.y)
	lower_border = min(ray_start.y, ray_direction.y)

	for side in poly.sides:
		if left_border <= side.first_point.x <= right_border or left_border <= side.second_point.x <= \
				right_border:
			if lower_border <= side.first_point.y <= upper_border or lower_border <= side.second_point.y <= \
					upper_border:
				lines.append(side)

	return lines


def get_probable_intersect_sides_segment(poly: Union["BasePolygon"], segment: "Segment") -> List["Segment"]:
	lines = []
	left_border = min(segment.first_point.x, segment.second_point.x)
	right_border = max(segment.first_point.x, segment.second_point.x)

	upper_border = max(segment.first_point.y, segment.second_point.y)
	lower_border = min(segment.first_point.y, segment.second_point.y)

	for side in poly.sides:
		if left_border <= side.first_point.x <= right_border or left_border <= side.second_point.x <= \
				right_border:
			if lower_border <= side.first_point.y <= upper_border or lower_border <= side.second_point.y <= \
					upper_border:
				lines.append(side)

	return lines

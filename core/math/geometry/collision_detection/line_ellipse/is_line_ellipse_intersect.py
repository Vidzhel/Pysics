from .line_ellipse_inter_points import get_ellipse_line_intersection_points


def is_intersect_line_circle(line: "Line", circle: "Circle"):
	distance_to_center = line.get_distance_to_point(circle.center)

	if distance_to_center > circle.radius:
		return False

	return True


def is_intersect_circle_line(circle: "Circle", line: "Line"):
	return is_intersect_line_circle(line, circle)


def is_intersect_line_ellipse(line: "Line", ellipse: "Ellipse"):
	line_to_center = ellipse.center - line.get_closest_point(ellipse.center)

	if line_to_center.get_magnitude() < ellipse.get_min_radius():
		return True

	if not get_ellipse_line_intersection_points(line_to_center, ellipse):
		return False

	return True


def is_intersect_ellipse_line(ellipse: "Ellipse", line: "Line"):
	return is_intersect_line_ellipse(line, ellipse)


def is_intersect_ray_circle(ray: "Ray", circle: "Circle"):
	distance_to_center = ray.get_distance_to_point(circle.center)

	if distance_to_center > circle.radius:
		return False

	return True


def is_intersect_circle_ray(circle: "Circle", ray: "Ray"):
	return is_intersect_ray_circle(ray, circle)


def is_intersect_ray_ellipse(ray: "Ray", ellipse: "Ellipse"):
	line_to_center = ellipse.center - ray.get_closest_point(ellipse.center)

	if line_to_center.get_magnitude() < ellipse.get_min_radius():
		return True

	if not get_ellipse_line_intersection_points(line_to_center, ellipse):
		return False

	return True


def is_intersect_ellipse_ray(ellipse: "Ellipse", ray: "Ray"):
	return is_intersect_ray_ellipse(ray, ellipse)


def is_intersect_segment_circle(segment: "Segment", circle: "Circle"):
	distance_to_center = segment.get_distance_to_point(circle.center)

	if distance_to_center > circle.radius:
		return False

	return True


def is_intersect_circle_segment(circle: "Circle", segment: "Segment"):
	return is_intersect_segment_circle(segment, circle)


def is_intersect_segment_ellipse(segment: "Segment", ellipse: "Ellipse"):
	line_to_center = ellipse.center - segment.get_closest_point(ellipse.center)

	if line_to_center.get_magnitude() < ellipse.get_min_radius():
		return True

	if not get_ellipse_line_intersection_points(line_to_center, ellipse):
		return False

	return True


def is_intersect_ellipse_segment(ellipse: "Ellipse", segment: "Segment"):
	return is_intersect_segment_ellipse(segment, ellipse)

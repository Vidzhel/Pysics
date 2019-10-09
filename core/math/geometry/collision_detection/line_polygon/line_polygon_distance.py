from typing import Union

from .line_polygon_collision_detection import (get_inter_data_convexpolygon_line,
                                               get_inter_data_concavepolygon_line,
                                               get_inter_data_rectangle_line, get_inter_data_triangle_line,
                                               get_inter_data_concavepolygon_ray,
                                               get_inter_data_rectangle_ray, get_inter_data_triangle_ray,
                                               get_inter_data_concavepolygon_segment,
                                               get_inter_data_rectangle_segment,
                                               get_inter_data_triangle_segment)


def get_distance_line_convexpolygon(line: "Line", poly: "ConvexPolygon") -> float:
	return get_distance_line_poly(line, poly, get_inter_data_convexpolygon_line)


def get_distance_convexpolygon_line(poly: "ConvexPolygon", line: "Line") -> float:
	return get_distance_line_convexpolygon(line, poly)


def get_distance_line_concavepolygon(line: "Line", poly: "ConcavePolygon") -> float:
	return get_distance_line_poly(line, poly, get_inter_data_concavepolygon_line)


def get_distance_concavepolygon_line(poly: "ConcavePolygon", line: "Line") -> float:
	return get_distance_line_concavepolygon(line, poly)


def get_distance_line_rectangle(line: "Line", rect: "Rectangle") -> float:
	return get_distance_line_poly(line, rect, get_inter_data_rectangle_line)


def get_distance_rectangle_line(rect: "Rectangle", line: "Line") -> float:
	return get_distance_line_rectangle(line, rect)


def get_distance_line_triangle(line: "Line", triangle: "Triangle") -> float:
	return get_distance_line_poly(line, triangle, get_inter_data_triangle_line)


def get_distance_triangle_line(triangle: "Triangle", line: "Line") -> float:
	return get_distance_line_triangle(line, triangle)


def get_distance_segment_convexpolygon(segment: "Segment", poly: "ConvexPolygon") -> float:
	return get_distance_line_poly(segment, poly, get_inter_data_convexpolygon_line)


def get_distance_convexpolygon_segment(poly: "ConvexPolygon", segment: "Segment") -> float:
	return get_distance_segment_convexpolygon(segment, poly)


def get_distance_segment_concavepolygon(segment: "Segment", poly: "ConcavePolygon") -> float:
	return get_distance_line_poly(segment, poly, get_inter_data_concavepolygon_segment)


def get_distance_concavepolygon_segment(poly: "ConcavePolygon", segment: "Segment") -> float:
	return get_distance_segment_concavepolygon(segment, poly)


def get_distance_segment_rectangle(segment: "Segment", rect: "Rectangle") -> float:
	return get_distance_line_poly(segment, rect, get_inter_data_rectangle_segment)


def get_distance_rectangle_segment(rect: "Rectangle", segment: "Segment") -> float:
	return get_distance_segment_rectangle(segment, rect)


def get_distance_segment_triangle(segment: "Segment", triangle: "Triangle") -> float:
	return get_distance_line_poly(segment, triangle, get_inter_data_triangle_segment)


def get_distance_triangle_segment(triangle: "Triangle", segment: "Segment") -> float:
	return get_distance_segment_triangle(segment, triangle)


def get_distance_ray_convexpolygon(ray: "Ray", poly: "ConvexPolygon") -> float:
	return get_distance_line_poly(ray, poly, get_inter_data_convexpolygon_line)


def get_distance_convexpolygon_ray(poly: "ConvexPolygon", ray: "Ray") -> float:
	return get_distance_ray_convexpolygon(ray, poly)


def get_distance_ray_concavepolygon(ray: "Ray", poly: "ConcavePolygon") -> float:
	return get_distance_line_poly(ray, poly, get_inter_data_concavepolygon_ray)


def get_distance_concavepolygon_ray(poly: "ConcavePolygon", ray: "Ray") -> float:
	return get_distance_ray_concavepolygon(ray, poly)


def get_distance_ray_rectangle(ray: "Ray", rect: "Rectangle") -> float:
	return get_distance_line_poly(ray, rect, get_inter_data_rectangle_ray)


def get_distance_rectangle_ray(rect: "Rectangle", ray: "Ray") -> float:
	return get_distance_ray_rectangle(ray, rect)


def get_distance_ray_triangle(ray: "Ray", triangle: "Triangle") -> float:
	return get_distance_line_poly(ray, triangle, get_inter_data_triangle_ray)


def get_distance_triangle_ray(triangle: "Triangle", ray: "Ray") -> float:
	return get_distance_ray_triangle(ray, triangle)


def get_distance_line_poly(line: Union["Line", "Ray", "Segment"], poly: "BasePolygon",
                           get_inter_data_func) -> float:
	closest_point = line.get_closest_point(poly.centroid)
	line_to_center = poly.centroid - closest_point

	inter_data = get_inter_data_func(poly, line_to_center)

	if not inter_data:
		return 0.0

	result_distance = 0

	for point in inter_data.intersection_points:
		distance = (point - closest_point).get_magnitude()
		result_distance = min(distance, result_distance)

	return result_distance

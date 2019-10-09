from typing import Union

from core.math.geometry.collision_detection.lines.lines_collision_detection import (
	get_inter_data_segment_line,
	get_inter_data_segment_ray,
	get_inter_data_segment_segment)
from .probable_inter_sides import (get_probable_intersect_sides_line, get_probable_intersect_sides_ray,
                                   get_probable_intersect_sides_segment)


def is_intersect_line_convexpolygon(line: "Line", poly: "ConvexPolygon") -> bool:
	return is_inter_line_poly(line, poly, get_probable_intersect_sides_line, get_inter_data_segment_line)


def is_intersect_convexpolygon_line(poly: "ConvexPolygon", line: "Line") -> bool:
	return is_intersect_line_convexpolygon(line, poly)


def is_intersect_line_concavepolygon(line: "Line", poly: "ConcavePolygon") -> bool:
	return is_intersect_line_convexpolygon(line, poly)


def is_intersect_concavepolygon_line(poly: "ConvexPolygon", line: "Line") -> bool:
	return is_intersect_line_concavepolygon(line, poly)


def is_intersect_line_rectangle(line: "Line", rect: "Rectangle") -> bool:
	return is_intersect_line_convexpolygon(line, rect)


def is_intersect_rectangle_line(rect: "Rectangle", line: "Line") -> bool:
	return is_intersect_line_rectangle(line, rect)


def is_intersect_line_triangle(line: "Line", triangle: "Triangle") -> bool:
	return is_intersect_line_convexpolygon(line, triangle)


def is_intersect_triangle_line(triangle: "Triangle", line: "Line") -> bool:
	return is_intersect_line_triangle(line, triangle)


def is_intersect_ray_convexpolygon(ray: "Ray", poly: "ConvexPolygon") -> bool:
	return is_inter_line_poly(ray, poly, get_probable_intersect_sides_ray, get_inter_data_segment_ray)


def is_intersect_convexpolygon_ray(poly: "ConvexPolygon", ray: "Ray") -> bool:
	return is_intersect_ray_convexpolygon(ray, poly)


def is_intersect_ray_concavepolygon(ray: "Line", poly: "ConcavePolygon") -> bool:
	return is_intersect_ray_convexpolygon(ray, poly)


def is_intersect_concavepolygon_ray(poly: "ConvexPolygon", ray: "Ray") -> bool:
	return is_intersect_ray_concavepolygon(ray, poly)


def is_intersect_ray_rectangle(ray: "Ray", rect: "Rectangle") -> bool:
	return is_intersect_ray_convexpolygon(ray, rect)


def is_intersect_rectangle_ray(rect: "Rectangle", ray: "Ray") -> bool:
	return is_intersect_ray_rectangle(ray, rect)


def is_intersect_ray_triangle(ray: "Ray", triangle: "Triangle") -> bool:
	return is_intersect_ray_convexpolygon(ray, triangle)


def is_intersect_triangle_ray(triangle: "Triangle", ray: "Ray") -> bool:
	return is_intersect_ray_triangle(ray, triangle)


def is_intersect_segment_convexpolygon(segment: "Segment", poly: "ConvexPolygon") -> bool:
	return is_inter_line_poly(segment, poly, get_probable_intersect_sides_segment,
	                          get_inter_data_segment_segment)


def is_intersect_convexpolygon_segment(poly: "ConvexPolygon", segment: "Segment") -> bool:
	return is_intersect_segment_convexpolygon(segment, poly)


def is_intersect_segment_concavepolygon(segment: "Segment", poly: "ConcavePolygon") -> bool:
	return is_intersect_segment_convexpolygon(segment, poly)


def is_intersect_concavepolygon_segment(poly: "ConvexPolygon", segment: "Segment") -> bool:
	return is_intersect_segment_concavepolygon(segment, poly)


def is_intersect_segment_rectangle(segment: "Segment", rect: "Rectangle") -> bool:
	return is_intersect_segment_convexpolygon(segment, rect)


def is_intersect_rectangle_segment(segment: "Segment", ray: "Ray") -> bool:
	return is_intersect_segment_rectangle(ray, segment)


def is_intersect_segment_triangle(segment: "Segment", triangle: "Triangle") -> bool:
	return is_intersect_segment_convexpolygon(segment, triangle)


def is_intersect_triangle_segment(triangle: "Triangle", segment: "Segment") -> bool:
	return is_intersect_segment_triangle(segment, triangle)


def is_inter_line_poly(line: Union["Line", "Ray", "Segment"], poly: "BasePolygon", get_prob_sides_func,
                       get_inter_data_func) -> bool:
	prob_sides = get_prob_sides_func(poly, line)

	for side in prob_sides:
		inter_data = get_inter_data_func(side, line)

		if inter_data:
			return True

	return False

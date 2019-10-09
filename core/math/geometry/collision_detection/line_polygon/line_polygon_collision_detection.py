from typing import Optional, Union

from core.math.geometry.collision_detection.collision_data import CollisionData
from core.math.geometry.collision_detection.lines.lines_collision_detection import (
	get_inter_data_segment_line,
	get_inter_data_segment_ray,
	get_inter_data_segment_segment)
from .probable_inter_sides import (get_probable_intersect_sides_line, get_probable_intersect_sides_ray,
                                   get_probable_intersect_sides_segment)


def get_inter_data_poly(line: Union["Segment", "Ray", "LIne"], poly: "BasePolygon", get_sides_func,
                        get_inter_data_func) -> Optional[CollisionData]:
	probable_inter_sides = get_sides_func(poly, line)
	result_inter_data = CollisionData([], None)

	for side in probable_inter_sides:
		inter_data = get_inter_data_func(side, line)

		if inter_data:
			result_inter_data.add_points_of_intersection(inter_data.intersection_points)
			result_inter_data.set_max_penetration_depth(inter_data.penetration_depth)

	if len(result_inter_data.intersection_points):
		return result_inter_data

	return None


def get_inter_data_line_convexpolygon(line: "Segment", poly: "ConvexPolygon") -> Optional[CollisionData]:
	return get_inter_data_poly(line, poly, get_probable_intersect_sides_line, get_inter_data_segment_line)


def get_inter_data_convexpolygon_line(poly: "ConvexPolygon", line: "Segment") -> Optional[CollisionData]:
	return get_inter_data_line_convexpolygon(line, poly)


def get_inter_data_line_concavepolygon(line: "Segment", poly: "ConcavePolygon") -> Optional[CollisionData]:
	return get_inter_data_line_convexpolygon(line, poly)


def get_inter_data_concavepolygon_line(poly: "ConcavePolygon", line: "Segment") -> Optional[CollisionData]:
	return get_inter_data_line_concavepolygon(line, poly)


def get_inter_data_line_rectangle(line: "Segment", rect: "Rectangle") -> Optional[CollisionData]:
	return get_inter_data_line_convexpolygon(line, rect)


def get_inter_data_rectangle_line(rect: "Rectangle", line: "Segment") -> Optional[CollisionData]:
	return get_inter_data_line_rectangle(line, rect)


def get_inter_data_line_triangle(line: "Segment", triangle: "Triangle") -> Optional[CollisionData]:
	return get_inter_data_line_convexpolygon(line, triangle)


def get_inter_data_triangle_line(triangle: "Triangle", line: "Segment") -> Optional[CollisionData]:
	return get_inter_data_line_triangle(line, triangle)


def get_inter_data_ray_convexpolygon(ray: "Line", poly: "ConvexPolygon") -> Optional[CollisionData]:
	return get_inter_data_poly(ray, poly, get_probable_intersect_sides_ray, get_inter_data_segment_ray)


def get_inter_data_convexpolygon_ray(poly: "ConvexPolygon", ray: "Line") -> Optional[CollisionData]:
	return get_inter_data_ray_convexpolygon(ray, poly)


def get_inter_data_ray_concavepolygon(ray: "Line", poly: "ConcavePolygon") -> Optional[CollisionData]:
	return get_inter_data_ray_convexpolygon(ray, poly)


def get_inter_data_concavepolygon_ray(poly: "ConcavePolygon", ray: "Line") -> Optional[CollisionData]:
	return get_inter_data_ray_concavepolygon(ray, poly)


def get_inter_data_ray_rect(ray: "Line", rect: "Rectangle") -> Optional[CollisionData]:
	return get_inter_data_ray_convexpolygon(ray, rect)


def get_inter_data_rectangle_ray(rect: "Rectangle", ray: "Line") -> Optional[CollisionData]:
	return get_inter_data_ray_rect(ray, rect)


def get_inter_data_ray_triangle(ray: "Line", triangle: "Triangle") -> Optional[CollisionData]:
	return get_inter_data_ray_convexpolygon(ray, triangle)


def get_inter_data_triangle_ray(triangle: "Triangle", ray: "Line") -> Optional[CollisionData]:
	return get_inter_data_ray_triangle(ray, triangle)


def get_inter_data_segment_convexpolygon(segment: "Segment", poly: "ConvexPolygon") -> Optional[
	CollisionData]:
	return get_inter_data_poly(segment, poly, get_probable_intersect_sides_segment,
	                           get_inter_data_segment_segment)


def get_inter_data_convexpolygon_segment(poly: "ConvexPolygon", segment: "Segment") -> Optional[
	CollisionData]:
	return get_inter_data_segment_convexpolygon(segment, poly)


def get_inter_data_segment_concavepolygon(segment: "Segment", poly: "ConcavePolygon") -> Optional[
	CollisionData]:
	return get_inter_data_segment_convexpolygon(segment, poly)


def get_inter_data_concavepolygon_segment(poly: "ConcavePolygon", segment: "Segment") -> Optional[
	CollisionData]:
	return get_inter_data_segment_concavepolygon(segment, poly)


def get_inter_data_segment_rect(segment: "Segment", rect: "Rectangle") -> Optional[CollisionData]:
	return get_inter_data_segment_convexpolygon(segment, rect)


def get_inter_data_rectangle_segment(rect: "Rectangle", segment: "Segment") -> Optional[CollisionData]:
	return get_inter_data_segment_rect(segment, rect)


def get_inter_data_segment_triangle(segment: "Segment", triangle: "Triangle") -> Optional[CollisionData]:
	return get_inter_data_segment_convexpolygon(segment, triangle)


def get_inter_data_triangle_segment(triangle: "Triangle", segment: "Segment") -> Optional[CollisionData]:
	return get_inter_data_segment_triangle(segment, triangle)

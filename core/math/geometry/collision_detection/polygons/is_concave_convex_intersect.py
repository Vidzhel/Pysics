from core.math.geometry.collision_detection.separated_axis import is_intersect_convex_concave
from .is_convex_polygons_intersect import is_intersect_rect_poly


def is_intersect_concavepolygon_convexpolygon(concave: "ConcavePolygon", convex: "ConvexPolygon") -> bool:
	return is_intersect_convex_concave(convex, concave)


def is_intersect_convexpolygon_concavepolygon(convex: "ConvexPolygon", concave: "ConcavePolygon") -> bool:
	return is_intersect_convex_concave(convex, concave)


def is_intersect_concavepolygon_rectangle(concave: "ConcavePolygon", rect: "Rectangle") -> bool:
	return is_intersect_rect_poly(rect, concave)


def is_intersect_rectangle_concavepolygon(rect: "Rectangle", concave: "ConcavePolygon") -> bool:
	return is_intersect_rect_poly(rect, concave)


def is_intersect_concavepolygon_triangle(concave: "ConcavePolygon", triangle: "Triangle") -> bool:
	return is_intersect_convex_concave(triangle, concave)


def is_intersect_triangle_concavepolygon(triangle: "Triangle", concave: "ConcavePolygon") -> bool:
	return is_intersect_convex_concave(triangle, concave)

from .concave_polygons_distance import get_distance_concavepolygon_concavepolygon


def get_distance_concavepolygon_convexpolygon(concave: "ConcavePolygon", convex: "ConvexPolygon") -> float:
	return get_distance_concavepolygon_concavepolygon(concave, convex)


def get_distance_convexpolygon_concavepolygon(convex: "ConvexPolygon", concave: "ConcavePolygon") -> float:
	return get_distance_concavepolygon_concavepolygon(concave, convex)


def get_distance_concavepolygon_rectangle(concave: "ConcavePolygon", rectangle: "Rectangle") -> float:
	return get_distance_concavepolygon_concavepolygon(concave, rectangle)


def get_distance_rectangle_concavepolygon(rectangle: "Rectangle", concave: "ConcavePolygon") -> float:
	return get_distance_concavepolygon_concavepolygon(concave, rectangle)


def get_distance_concavepolygon_triangle(concave: "ConcavePolygon", triangle: "Triangle") -> float:
	return get_distance_concavepolygon_concavepolygon(concave, triangle)


def get_distance_triangle_concavepolygon(triangle: "Triangle", concave: "ConcavePolygon") -> float:
	return get_distance_concavepolygon_concavepolygon(concave, triangle)

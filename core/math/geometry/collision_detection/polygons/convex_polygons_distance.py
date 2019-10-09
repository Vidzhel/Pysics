from core.math.geometry.collision_detection.polygons.get_closest_polygons_point import \
	get_closest_support_point
from core.math.geometry.collision_detection.polygons.minkowski_difference_of_polygons import \
	polygons_difference
from core.math.geometry.convex_hull import create_convex_hull
from core.math.vector2d import Vector2d


def get_distance_convexpolygon_convexpolygon(first_polygon: "ConvexPolygon",
                                             second_polygon: "ConvexPolygon") -> float:
	return get_dist_convex_polygons(first_polygon, second_polygon)


def get_distance_convexpolygon_rectangle(poly: "ConvexPolygon", rectangle: "Rectangle") -> float:
	return get_dist_convex_polygons(poly, rectangle)


def get_distance_rectangle_convexpolygon(rectangle: "Rectangle", poly: "ConvexPolygon") -> float:
	return get_dist_convex_polygons(poly, rectangle)


def get_distance_convexpolygon_triangle(poly: "ConvexPolygon", triangle: "Triangle") -> float:
	return get_dist_convex_polygons(poly, triangle)


def get_distance_triangle_convexpolygon(triangle: "Triangle", poly: "ConvexPolygon") -> float:
	return get_dist_convex_polygons(poly, triangle)


def get_distance_rectangle_rectangle(first_rect: "Rectangle", second_rect: "Rectangle") -> float:
	return get_dist_convex_polygons(first_rect, second_rect)


def get_distance_rectangle_triangle(rectangle: "Rectangle", triangle: "Triangle") -> float:
	return get_dist_convex_polygons(rectangle, triangle)


def get_distance_triangle_rectangle(triangle: "Triangle", rectangle: "Rectangle") -> float:
	return get_dist_convex_polygons(rectangle, triangle)


def get_dist_convex_polygons(first_polygon: "ConvexPolygon", second_polygon: "ConvexPolygon") -> float:
	"""Uses the Gilbert-Johnson-Keerthi Algorithm to get penetration depth and intersection points"""

	new_polygon_points = polygons_difference(first_polygon, second_polygon)
	convex_hull = create_convex_hull(new_polygon_points)

	closest_point = get_closest_support_point(convex_hull, Vector2d(0, 0))
	penetration = (closest_point - Vector2d(0, 0)).get_magnitude()

	if convex_hull.is_point_belongs(Vector2d(0, 0)):
		return -penetration

	return penetration

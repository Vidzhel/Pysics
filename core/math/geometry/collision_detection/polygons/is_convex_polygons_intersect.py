from core.math.geometry.convex_hull import create_convex_hull
from core.math.vector2d import Vector2d
from .minkowski_difference_of_polygons import polygons_difference


def is_intersect_convexpolygon_convexpolygon(first_poly: "ConvexPolygon",
                                             second_poly: "ConvexPolygon") -> bool:
	return is_intersect_convexpolygons(first_poly, second_poly)


def is_intersect_convexpolygon_rectangle(first_poly: "ConvexPolygon", rectangle: "Rectangle") -> bool:
	return is_intersect_rect_poly(first_poly, rectangle)


def is_intersect_rectangle_convexpolygon(rectangle: "Rectangle", first_poly: "ConvexPolygon") -> bool:
	return is_intersect_rect_poly(first_poly, rectangle)


def is_intersect_convexpolygon_triangle(first_poly: "ConvexPolygon", triangle: "Triangle") -> bool:
	return is_intersect_convexpolygons(first_poly, triangle)


def is_intersect_triangle_convexpolygon(triangle: "Triangle", first_poly: "ConvexPolygon") -> bool:
	return is_intersect_convexpolygons(first_poly, triangle)


def is_intersect_rectangle_rectangle(first_rectangle: "Rectangle", second_rectangle: "Rectangle") -> bool:
	return is_intersect_rect_poly(first_rectangle, second_rectangle)


def is_intersect_rectangle_triangle(rectangle: "Rectangle", triangle: "Triangle") -> bool:
	return is_intersect_rect_poly(triangle, rectangle)


def is_intersect_triangle_rectangle(triangle: "Triangle", rectangle: "Rectangle") -> bool:
	return is_intersect_rect_poly(triangle, rectangle)


def is_intersect_triangle_triangle(first_triangle: "Triangle", second_triangle: "Triangle") -> bool:
	return is_intersect_rect_poly(first_triangle, second_triangle)


def is_intersect_convexpolygons(first_poly: "ConvexPolygon", second_poly: "ConvexPolygon") -> bool:
	new_polygon_points = polygons_difference(first_poly, second_poly)
	convex_hull = create_convex_hull(new_polygon_points)

	if not convex_hull.is_point_belongs(Vector2d(0, 0)):
		return False

	return True


def is_intersect_rect_poly(poly: "ConvexPolygon", rect: "Rectangle") -> bool:
	left_upper_corner, right_upper_corner, right_lower_corner, left_lower_corner = rect.get_corners
	max_x_point, max_y_point, min_x_point, min_y_point = poly.the_most_distant_points

	if left_upper_corner.x <= min_x_point.x <= right_upper_corner.x or left_upper_corner.x <= max_x_point.x \
			<= right_upper_corner.x:
		if left_lower_corner.y <= min_y_point.y <= left_upper_corner.y or left_lower_corner.y <= \
				min_y_point.y <= left_upper_corner.y:
			return True

	return False

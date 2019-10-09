from core.math.vector2d import Vector2d


def get_closest_support_point(polygon: "BasePolygon", point: Vector2d) -> Vector2d:
	"""Gets the point from the polygon border that has the smallest distance to the given point

	Uses support function (gets point with the biggest dot product on the given vector) to build simplexes in
	our case 2-simplex - that represents triangle"""
	poly_points = polygon.points

	min_distance = 100000
	min_distance_point = None

	for poly_point in poly_points:
		distance = (poly_point - point).get_magnitude()

		if distance < min_distance:
			min_distance = distance
			min_distance_point = poly_point

	closest_lines = polygon.get_side_with_point(min_distance_point)

	min_distance = 100000
	min_distance_point = None

	for line in closest_lines:
		closest_point = line.get_closest_point(point)
		distance = (closest_point - point).get_magnitude()

		if distance < min_distance:
			min_distance = distance
			min_distance_point = closest_point

	return min_distance_point

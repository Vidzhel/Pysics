from .is_concave_polygons_intersect import is_intersect_concavepolygon_concavepolygon


def get_distance_concavepolygon_concavepolygon(first_polygon: "ConcavePolygon",
                                               second_polygon: "ConcavePolygon") -> float:
	center_vector = second_polygon.centroid - first_polygon.centroid
	first_closest_point = first_polygon.get_support_point(center_vector)
	second_closest_point = second_polygon.get_support_point(center_vector.inverse())

	distance = (second_closest_point - first_closest_point).get_magnitude()

	if is_intersect_concavepolygon_concavepolygon(first_polygon, second_polygon):
		return -distance

	return distance

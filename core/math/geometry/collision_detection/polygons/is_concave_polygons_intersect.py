from core.math.geometry.collision_detection.separated_axis import is_intersect_concave_concave


def is_intersect_concavepolygon_concavepolygon(first_polygon: "ConcavePolygon",
                                               second_polygon: "ConcavePolygon") -> bool:
	return is_intersect_concave_concave(first_polygon, second_polygon)

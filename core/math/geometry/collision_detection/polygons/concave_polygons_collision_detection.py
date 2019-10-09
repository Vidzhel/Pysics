from typing import Optional

from core.math.average import average
from core.math.geometry.collision_detection.collision_data import CollisionData
from core.math.geometry.collision_detection.line_polygon.line_polygon_collision_detection import \
	get_inter_data_segment_concavepolygon


def get_inter_data_concavepolygon_concavepolygon(first_poly: "ConcavePolygon",
                                                 second_poly: "ConcavePolygon") -> Optional[CollisionData]:
	penetration_length: float = 0.0
	points = []

	for side in first_poly.sides:
		side_inter_data = get_inter_data_segment_concavepolygon(side, second_poly)
		if side_inter_data:
			points.extend(side_inter_data.intersection_points)
			penetration_length = average(penetration_length, side_inter_data.penetration_depth)

	if len(points) == 0:
		return None

	return CollisionData(points, penetration_length)

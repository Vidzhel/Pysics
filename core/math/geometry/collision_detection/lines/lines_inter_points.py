from typing import Union, Tuple, List

from core.math.vector2d import Vector2d


def get_segments_intersection_points(segment: Union["Line", "Segment", "Ray"],
                                     penetration_coefficients: Tuple[float, float]) -> List[
	Vector2d]:
	t, u = penetration_coefficients

	intersection_point_x = segment.first_point.x + t * (
			segment.second_point.x - segment.first_point.x)
	intersection_point_y = segment.first_point.y + t * (
			segment.second_point.y - segment.first_point.y)
	intersection_point = Vector2d(intersection_point_x, intersection_point_y)

	return [intersection_point]

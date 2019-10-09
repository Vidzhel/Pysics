from typing import Optional, List

from core.math.vector2d import Vector2d


class CollisionData:
	"""Stores intersection points and penetration depth

	penetration depth can be set None when we can't get it
	e.g ray doesn't have length, so we can't resolve the collision
	"""

	def __init__(self, intersection_points: List[Vector2d],
	             penetration_depth: Optional[float] = None):
		self.intersection_points = intersection_points
		self.penetration_depth = penetration_depth

	def set_max_penetration_depth(self, penetration: float) -> None:
		self.penetration_depth = max(self.penetration_depth, penetration)

	def add_points_of_intersection(self, points: List[Vector2d]) -> None:
		self.intersection_points.extend(points)

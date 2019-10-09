from typing import Optional

from core.math.geometry.collision_detection.collision_data import CollisionData
from .concave_polygons_collision_detection import get_inter_data_concavepolygon_concavepolygon


def get_inter_data_concavepolygon_convexpolygon(concave: "ConcavePolygon", convex: "ConvexPolygon") -> \
Optional[CollisionData]:
	return get_inter_data_concavepolygon_concavepolygon(concave, convex)


def get_inter_data_convexpolygon_concavepolygon(convex: "ConvexPolygon", concave: "ConcavePolygon") -> \
Optional[CollisionData]:
	return get_inter_data_concavepolygon_concavepolygon(concave, convex)


def get_inter_data_concavepolygon_rectangle(concave: "ConcavePolygon", rect: "Rectancle") -> Optional[
	CollisionData]:
	return get_inter_data_concavepolygon_concavepolygon(concave, rect)


def get_inter_data_rectangle_concavepolygon(rect: "Rectancle", concave: "ConcavePolygon") -> Optional[
	CollisionData]:
	return get_inter_data_concavepolygon_concavepolygon(concave, rect)


def get_inter_data_concavepolygon_triangle(concave: "ConcavePolygon", triangle: "Triangle") -> Optional[
	CollisionData]:
	return get_inter_data_concavepolygon_concavepolygon(concave, triangle)


def get_inter_data_triangle_concavepolygon(triangle: "Triangle", concave: "ConcavePolygon") -> Optional[
	CollisionData]:
	return get_inter_data_concavepolygon_concavepolygon(concave, triangle)

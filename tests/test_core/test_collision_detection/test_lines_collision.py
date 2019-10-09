import unittest

from core.math.geometry.collision_detection.objects_collision_detection import CollisionDetection
from core.math.geometry.geometry_objects import Segment, Line, Ray
from core.math.vector2d import Vector2d


class TestSegments(unittest.TestCase):
	# Do not intersect
	first_segment = Segment(Vector2d(-2, 0), Vector2d(0, 2))
	second_segment = Segment(Vector2d(-6, 0), Vector2d(0, 4))

	# Intersect
	# y=0.5x+3
	third_segment = Segment(Vector2d(-6, 0), Vector2d(6, 6))
	# y=x + 2
	fourth_segment = Segment(Vector2d(-2, 0), Vector2d(4, 6))

	def test_segments_intersection(self):
		data = CollisionDetection.get_intersection_data(self.first_segment, self.second_segment)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_segment))

		data = CollisionDetection.get_intersection_data(self.second_segment, self.first_segment)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_segment))

		data1 = CollisionDetection.get_intersection_data(self.third_segment, self.fourth_segment)
		self.assertIsNotNone(data1, 'data1 shouldn\'t be null')
		point = data1.intersection_points
		self.assertEqual(point, [Vector2d(2, 4)], 'Intersection point for data1 does not equal to ' \
		                                          'the expected')

		data2 = CollisionDetection.get_intersection_data(self.fourth_segment, self.third_segment)
		self.assertIsNotNone(data2, 'data2 shouldn\'t be null')
		point = data2.intersection_points
		self.assertEqual(point, [Vector2d(2, 4)], 'Intersection point for data2 does not equal to '
		                                          'the expected')

		self.assertEqual(data1.intersection_points, data2.intersection_points,
		                 'data1[0] and data2[0] does not equal')

	# Do not intersect
	# y = x
	first_line = Line(Vector2d(-1, -1), Vector2d(1, 1))
	# y = x + 2
	second_line = Line(Vector2d(-2, 0), Vector2d(0, 2))

	# Intersect far away
	# y= 0.9x
	third_line = Line(Vector2d(-1, -0.9), Vector2d(1, 0.9))
	# y=x + 2
	fourth_line = Line(Vector2d(-2, 0), Vector2d(0, 2))

	# Intersect
	fifth_line = Line(Vector2d(-1, 1), Vector2d(0, 2))
	sixth_line = Line(Vector2d(0, 0), Vector2d(1, 2))

	def test_line_interaction(self):
		data = CollisionDetection.get_intersection_data(self.first_line, self.second_line)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_line))

		data = CollisionDetection.get_intersection_data(self.second_line, self.first_line)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_line))

		data1 = CollisionDetection.get_intersection_data(self.sixth_line, self.fifth_line)
		self.assertIsNotNone(data1, 'data1 shouldn\'t be null')
		point = data1.intersection_points
		self.assertEqual(point, [Vector2d(2, 4)], 'Intersection point for data1 does not equal to ' \
		                                          'the expected')

		data2 = CollisionDetection.get_intersection_data(self.fifth_line, self.sixth_line)
		self.assertIsNotNone(data2, 'data2 shouldn\'t be null')
		point = data2.intersection_points
		self.assertEqual(point, [Vector2d(2, 4)], 'Intersection point for data2 does not equal to '
		                                          'the expected')

		data3 = CollisionDetection.get_intersection_data(self.third_line, self.fourth_line)
		self.assertIsNotNone(data3, 'Data3 should not be null')

		data4 = CollisionDetection.get_intersection_data(self.fourth_line, self.third_line)
		self.assertIsNotNone(data4, 'Data4 should not be null')

	# Do not intersect
	first_ray = Ray(Vector2d(-2, -2), Vector2d(1, 1))
	second_ray = Ray(Vector2d(-2.3, -3), Vector2d(0, -8))

	# Do not intersect
	seventh_ray = Ray(Vector2d(-0.88, 2.55), Vector2d(0.22, 2.26))
	eighth_ray = Ray(Vector2d(-2.3, -3), Vector2d(0, -8))

	# Intersect far away
	third_ray = Ray(Vector2d(0.86, -6), Vector2d(2, -2))
	fourth_ray = Ray(Vector2d(0, -4), Vector2d(1.5, -0.2))

	# Intersect
	fifth_ray = Ray(Vector2d(-6.3, -0.58), Vector2d(-3.92, -0.47))
	sixth_ray = Ray(Vector2d(-5.3, 2.49), Vector2d(-3.35, 0.45))

	def test_ray_intersection(self):
		data = CollisionDetection.get_intersection_data(self.first_line, self.second_line)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_line))

		data = CollisionDetection.get_intersection_data(self.second_line, self.first_line)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_line))

		data = CollisionDetection.get_intersection_data(self.seventh_ray, self.eighth_ray)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_line))

		data = CollisionDetection.get_intersection_data(self.eighth_ray, self.seventh_ray)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_line))

		data1 = CollisionDetection.get_intersection_data(self.sixth_ray, self.fifth_ray)
		self.assertIsNotNone(data1, 'data1 shouldn\'t be null')
		point = data1.intersection_points
		self.assertEqual(point, [Vector2d(-2.53, -0.4)],
		                 'Intersection point for data1 does not equal to the expected')

		data2 = CollisionDetection.get_intersection_data(self.fifth_ray, self.sixth_ray)
		self.assertIsNotNone(data2, 'data2 shouldn\'t be null')
		point = data2.intersection_points
		self.assertEqual(point, [Vector2d(-2.53, -0.4)], 'Intersection point for data2 does not equal to '
		                                                 'the expected')

		data3 = CollisionDetection.get_intersection_data(self.third_ray, self.fourth_ray)
		self.assertIsNotNone(data3, 'Data3 should not be null')

		data4 = CollisionDetection.get_intersection_data(self.fourth_ray, self.third_ray)
		self.assertIsNotNone(data4, 'Data4 should not be null')


if __name__ == '__main__':
	unittest.main()

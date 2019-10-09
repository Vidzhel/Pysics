import unittest

from core.math.geometry.geometry_objects import Segment, Line, Circle
from core.math.vector2d import Vector2d


class TestSegments(unittest.TestCase):
	# Do not intersect
	# y = x+2.85
	first_line = Segment(Vector2d(-2, 0.85), Vector2d(-0.65, 2.2))
	# y= -x+2.85
	second_line = Segment(Vector2d(2.85, 0), Vector2d(0, 2.85))
	circle = Circle(Vector2d(0, 0), 2)

	# Intersect
	# y=0.5x+3
	third_line = Segment(Vector2d(-6, 0), Vector2d(6, 6))
	# y=x + 2
	fourth_line = Segment(Vector2d(-2, 0), Vector2d(4, 6))

	def test_line_ellipse_inter(self):
		data = self.circle.get_intersection_data(self.first_line)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_ray))

		data = self.first_line.get_intersection_data(self.circle)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_ray))

		data = self.circle.get_intersection_data(self.second_line)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_ray))

		data = self.second_line.get_intersection_data(self.circle)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_ray))

	# Do not intersect
	# y = x
	first_ray = Line(Vector2d(-1, -1), Vector2d(1, 1))
	# y = x + 2
	second_ray = Line(Vector2d(-2, 0), Vector2d(0, 2))

	# Intersect far away
	# y= 0.9x
	third_ray = Line(Vector2d(-1, -0.9), Vector2d(1, 0.9))
	# y=x + 2
	fourth_ray = Line(Vector2d(-2, 0), Vector2d(0, 2))

	# Intersect
	fifth_ray = Line(Vector2d(-1, 1), Vector2d(0, 2))
	sixth_ray = Line(Vector2d(0, 0), Vector2d(1, 2))

	def test_ray_interaction(self):
		data = self.first_ray.get_intersection_data(self.second_ray)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_ray))

		data = self.second_ray.get_intersection_data(self.first_ray)
		self.assertIsNone(data, 'Data should be null' + str(data) + ' ' + str(self.second_ray))

		data1 = self.sixth_ray.get_intersection_data(self.fifth_ray)
		self.assertIsNotNone(data1, 'data1 shouldn\'t be null')
		point = data1[0]
		self.assertEqual(point, [Vector2d(2, 4)], 'Intersection point for data1 does not equal to ' \
		                                          'the expected')

		data2 = self.fifth_ray.get_intersection_data(self.sixth_ray)
		self.assertIsNotNone(data2, 'data2 shouldn\'t be null')
		point = data2[0]
		self.assertEqual(point, [Vector2d(2, 4)], 'Intersection point for data2 does not equal to '
		                                          'the expected')

		data3 = self.third_ray.get_intersection_data(self.fourth_ray)
		self.assertIsNotNone(data3, 'Data3 should not be null')

		data4 = self.fourth_ray.get_intersection_data(self.third_ray)
		self.assertIsNotNone(data4, 'Data4 should not be null')


if __name__ == '__main__':
	unittest.main()

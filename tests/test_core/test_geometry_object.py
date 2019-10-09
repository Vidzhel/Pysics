import unittest

from core.math.geometry.geometry_objects import *


class TestGeometryObjects(unittest.TestCase):
	segment = Segment(Vector2d(-4, 1), Vector2d(1, -6))
	parallel_y_segment = Segment(Vector2d(-1, -1), Vector2d(-1, 1))

	horizontal_segment = Segment(Vector2d(-4, 2), Vector2d(5, 2))
	vertical_segment = Segment(Vector2d(-5, -4), Vector2d(-5, 2))

	def test_segment(self):
		self.assertEqual(self.segment.first_point, Vector2d(-4, 1), "Init points don't match")
		self.assertEqual(self.segment.second_point, Vector2d(1, -6), "Init points don't match")

		self.assertTrue(self.horizontal_segment.is_horizontal())
		self.assertTrue(self.vertical_segment.is_vertical())

		self.assertFalse(self.horizontal_segment.is_vertical())
		self.assertFalse(self.vertical_segment.is_horizontal())

		self.assertFalse(self.segment.is_horizontal())
		self.assertFalse(self.segment.is_vertical())

		is_belongs = self.segment.is_point_belongs(Vector2d(-2, -1.8))
		self.assertTrue(is_belongs, "The point should belongs to the segment")

		is_belongs = self.segment.is_point_belongs(Vector2d(2, -7.4))
		self.assertFalse(is_belongs, "The point should not belongs to the segment (it's on the ray "
		                             "with the same coordinates of first and second point)")

		is_belongs = self.segment.is_point_belongs(Vector2d(1, -6.1))
		self.assertFalse(is_belongs, "Does not belongs to the ray")

		self.assertAlmostEqual(self.segment.get_length(), 8.6, delta=0.01)

		self.assertEqual(self.segment.get_closest_point(Vector2d(-1.78, -1.64)),
		                 Vector2d(-2, -1.8))

		self.assertEqual(Vector2d(-4, 1), self.segment.get_closest_point(Vector2d(-4, 2)),
		                 "Should be first point")
		self.assertEqual(Vector2d(1, -6), self.segment.get_closest_point(Vector2d(1, -6.5)),
		                 "Should be second point")

		self.assertEqual(Vector2d(-1, -1),
		                 self.parallel_y_segment.get_closest_point(Vector2d(-1, -1.5)),
		                 "Should be first point")

		self.assertEqual(Vector2d(-1, 1), self.parallel_y_segment.get_closest_point(Vector2d(-1, 1.5)),
		                 "Should be second point")

		self.assertAlmostEqual(0.4, self.segment.get_distance_to_point(Vector2d(1.2, -5.6)),
		                       delta=0.01, msg="Distance to the second point doesn't equal expect.")

		self.assertAlmostEqual(0.2, self.segment.get_distance_to_point(Vector2d(-4, 1.2)),
		                       delta=0.01, msg="Distance to the first point doesn't match expect.")

		self.assertEqual(Vector2d(-1, 0), self.parallel_y_segment.get_middle_point())
		self.assertEqual(Vector2d(-1.5, -2.5), self.segment.get_middle_point())

		perpendicular = self.segment.get_perpendicular()
		self.assertEqual(90, self.segment.get_angle(perpendicular))

	ray = Ray(Vector2d(-4, 1), Vector2d(1, -6))

	def test_ray(self):
		is_belongs = self.ray.is_point_belongs(Vector2d(-2, -1.8))
		self.assertTrue(is_belongs, "The point should belongs to the segment")

		is_belongs = self.ray.is_point_belongs(Vector2d(2, -7.4))
		self.assertTrue(is_belongs, "The point should belongs to the segment")

		is_belongs = self.ray.is_point_belongs(Vector2d(1, -6.1))
		self.assertFalse(is_belongs, "Does not belongs to the ray")

		is_belongs = self.ray.is_point_belongs(Vector2d(-4.75, 2.05))
		self.assertFalse(is_belongs, "The point should not belongs to the ray (it's on the segment "
		                             "with the same coordinates of first and second point)")

		self.assertEqual(Vector2d(-2, -1.8), self.ray.get_closest_point(Vector2d(-1.78, -1.64)))

		self.assertEqual(Vector2d(-4, 1), self.ray.get_closest_point(Vector2d(-4, 2)),
		                 "Should be first point")

		self.assertNotEqual(Vector2d(1, -6), self.ray.get_closest_point(Vector2d(1, -6.5)),
		                    "Should not be second point")

	line = Line(Vector2d(-4, 1), Vector2d(1, -6))

	def test_line(self):
		is_belongs = self.line.is_point_belongs(Vector2d(-2, -1.8))
		self.assertTrue(is_belongs, "The point should belongs to the segment")

		is_belongs = self.line.is_point_belongs(Vector2d(2, -7.4))
		self.assertTrue(is_belongs, "The point should belongs to the segment")

		is_belongs = self.line.is_point_belongs(Vector2d(1, -6.1))
		self.assertFalse(is_belongs, "Does not belongs to the ray")

		is_belongs = self.line.is_point_belongs(Vector2d(-4.75, 2.05))
		self.assertTrue(is_belongs, "The point should belongs to the segment")

		is_belongs = self.line.is_point_belongs(Vector2d(-4.75, 2.1))
		self.assertFalse(is_belongs, "The point should belongs to the segment")

		self.assertEqual(Vector2d(-2, -1.8), self.line.get_closest_point(Vector2d(-1.78, -1.64)))

		self.assertNotEqual(Vector2d(-4, 1), self.line.get_closest_point(Vector2d(-4, 2)),
		                    "Should be first point")

		self.assertNotEqual(Vector2d(1, -6), self.line.get_closest_point(Vector2d(1, -6.5)),
		                    "Should not be second point")

	circle = Circle(Vector2d(-10, -2), 6)

	def test_circle(self):
		self.assertEqual(12, self.circle.get_diameter())

		self.assertAlmostEqual(113.097, self.circle.get_area(), delta=0.01, msg="Wrong area")

		self.assertTrue(self.circle.is_point_belongs(Vector2d(-6.79, -7.07)), "Should belongs")
		self.assertTrue(self.circle.is_point_belongs(Vector2d(-7.5, -5.5)), "Should belongs")
		self.assertFalse(self.circle.is_point_belongs(Vector2d(-5, 1.5)), "Should not belongs")

	ellipse = Ellipse(Vector2d(-6, 2), 5.66, 4)

	def test_ellipse(self):
		self.assertAlmostEqual(71.12, self.ellipse.get_area(), delta=0.01, msg="Wrong area")

		self.assertTrue(self.ellipse.is_point_belongs(Vector2d(-3.17, 2)), "Should belongs")
		self.assertTrue(self.ellipse.is_point_belongs(Vector2d(-7.7, 3.6)), "Should belongs")
		self.assertTrue(self.ellipse.is_point_belongs(Vector2d(-6.87, 3.34)), "Should belongs")
		self.assertFalse(self.ellipse.is_point_belongs(Vector2d(-4.47, 0.23)), "Should not belongs")

	points_convex_poly = [
		Vector2d(-7.29, 2),
		Vector2d(-5.72, 0.74),
		Vector2d(-3.44, 1.98),
		Vector2d(-3.96, 3.62),
		Vector2d(-6.33, 3.86),
		Vector2d(-7.29, 3.41)
	]

	points_concave_poly = [
		Vector2d(-9, -2),
		Vector2d(-7.84, -2.54),
		Vector2d(-6.41, -1.14),
		Vector2d(-5.47, -2.89),
		Vector2d(-5.91, -4.48),
		Vector2d(-8.43, -5.05)
	]

	points_self_inter_poly = [
		Vector2d(1.74, -1.41),
		Vector2d(2.29, -2.09),
		Vector2d(1.42, -2.35),
		Vector2d(2.11, -2),
		Vector2d(1.5, -1.5),
		Vector2d(2, -1.5)
	]

	convex_poly = ConvexPolygon(points_convex_poly)

	# concave_poly = ConcavePolygon(points_concave_poly)

	def test_convex_poly(self):
		with self.assertRaises(AttributeError):
			self_inter_poly = ConcavePolygon(self.points_self_inter_poly)
			convex_poly_wrong_angles = ConvexPolygon(self.points_concave_poly)


if __name__ == '__main__':
	unittest.main()

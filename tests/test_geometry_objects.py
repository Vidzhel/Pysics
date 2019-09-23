import unittest
from pysics.core.vector2d import Vector2d
from pysics.core.Objects.geometry_objects import Line, Ray


class TestShapes(unittest.TestCase):

    # Do not intersect
    first_line = Line(Vector2d(-2, 0), Vector2d(0, 2))
    second_line = Line(Vector2d(-6, 0), Vector2d(0, 4))

    # Intersect
    third_line = Line(Vector2d(-6, 0), Vector2d(4, 5))
    fourth_line = Line(Vector2d(-6, 0), Vector2d(3, 5))

    def test_lines_intersection(self):
        data = self.first_line.get_intersection_data(self.second_line)
        self.assertIsNone(data)

        data = self.second_line.get_intersection_data(self.first_line)
        self.assertIsNone(data)

        data1 = self.third_line.get_intersection_data(self.fourth_line)
        self.assertIsNotNone(data1)
        point = data1[0]
        self.assertEqual(point, Vector2d(2, 4))

        data2 = self.fourth_line.get_intersection_data(self.third_line)
        self.assertIsNotNone(data2)
        point = data2[0]
        self.assertEqual(point, Vector2d(2, 4))

        self.assertEqual(data1[0], data2[0])
        self.assertEqual(data1[1], data2[1])
        self.assertEqual(data1[2], data2[2])

    def test_circle(self):
        pass


if __name__ == '__main__':
    unittest.main()

import unittest, math
from core.vector2d import Vector2d


class TestVector2d(unittest.TestCase):

    integer_case = Vector2d(1, 1)
    float_case = Vector2d(2.5, 3.5)
    integer_negative_case = Vector2d(-4, 6)
    float_negative_case = Vector2d(-3.6, 6.4)
    negative_case = Vector2d(-3, -3.5)
    zero_case = Vector2d(0, 0)

    def test_scale_integer(self):

        self.assertEqual(self.integer_case.scale_vector(
            3), Vector2d(self.integer_case.x * 3, self.integer_case.y * 3), "Integer scale fails")

        self.assertEqual(self.float_case.scale_vector(
            3), Vector2d(self.float_case.x * 3, self.float_case.y * 3), "Integer scale fails")

        self.assertEqual(self.integer_negative_case.scale_vector(
            3), Vector2d(self.integer_negative_case.x * 3, self.integer_negative_case.y * 3), "Integer scale fails")

        self.assertEqual(self.float_negative_case.scale_vector(
            3), Vector2d(self.float_negative_case.x * 3, self.float_negative_case.y * 3), "Integer scale fails")

        self.assertEqual(self.negative_case.scale_vector(
            3), Vector2d(self.negative_case.x * 3, self.negative_case.y * 3), "Integer scale fails")

        self.assertEqual(self.zero_case.scale_vector(
            3), Vector2d(self.zero_case.x * 3, self.zero_case.y * 3), "Integer scale fails")

    def test_scale_negative_float(self):

        self.assertEqual(self.integer_case.scale_vector(-3.5),
                         Vector2d(self.integer_case.x * -3.5, self.integer_case.y * -3.5), "Integer scale fails")

        self.assertEqual(self.float_case.scale_vector(-3.5),
                         Vector2d(self.float_case.x * -3.5, self.float_case.y * -3.5), "Integer scale fails")

        self.assertEqual(self.integer_negative_case.scale_vector(-3.5),
                         Vector2d(self.integer_negative_case.x * -3.5, self.integer_negative_case.y * -3.5), "Integer scale fails")

        self.assertEqual(self.float_negative_case.scale_vector(-3.5),
                         Vector2d(self.float_negative_case.x * -3.5, self.float_negative_case.y * -3.5), "Integer scale fails")

        self.assertEqual(self.negative_case.scale_vector(-3.5),
                         Vector2d(self.negative_case.x * -3.5, self.negative_case.y * -3.5), "Integer scale fails")

        self.assertEqual(self.zero_case.scale_vector(-3.5),
                         Vector2d(self.zero_case.x * -3.5, self.zero_case.y * -3.5), "Integer scale fails")

    def test_add_vector(self):

        self.assertEqual(self.integer_case.add_vector(self.float_case),
                         Vector2d(self.integer_case.x + self.float_case.x, self.integer_case.y + self.float_case.y), "Integer addition fails")

        self.assertEqual(self.integer_negative_case.add_vector(self.float_negative_case),
                         Vector2d(self.integer_negative_case.x + self.float_negative_case.x, self.integer_negative_case.y + self.float_negative_case.y), "Integer addition fails")

        self.assertEqual(self.negative_case.add_vector(self.zero_case),
                         Vector2d(self.negative_case.x + self.zero_case.x, self.negative_case.y + self.zero_case.y), "Integer addition fails")

    def test_add_scaled_vector(self):

        self.assertEqual(self.integer_case.add_scaled_vector(self.float_case, -3.25),
                         Vector2d(self.integer_case.x + self.float_case.x * -3.25, self.integer_case.y + self.float_case.y * -3.25), "Integer scaled addition fails")

        self.assertEqual(self.integer_negative_case.add_scaled_vector(self.float_negative_case, -3.25),
                         Vector2d(self.integer_negative_case.x + self.float_negative_case.x * -3.25, self.integer_negative_case.y + self.float_negative_case.y * -3.25), "Integer scaled addition fails")

        self.assertEqual(self.negative_case.add_scaled_vector(self.zero_case, -3.25),
                         Vector2d(self.negative_case.x + self.zero_case.x * -3.25, self.negative_case.y + self.zero_case.y * -3.25), "Integer scaled addition fails")

    def test_substract_vector(self):

        self.assertEqual(self.integer_case.substract_vector(self.float_case),
                         Vector2d(self.integer_case.x - self.float_case.x, self.integer_case.y - self.float_case.y), "Integer substraction fails")

        self.assertEqual(self.integer_negative_case.substract_vector(self.float_negative_case),
                         Vector2d(self.integer_negative_case.x - self.float_negative_case.x, self.integer_negative_case.y - self.float_negative_case.y), "Integer substraction fails")

        self.assertEqual(self.negative_case.substract_vector(self.zero_case),
                         Vector2d(self.negative_case.x - self.zero_case.x, self.negative_case.y - self.zero_case.y), "Integer substraction fails")


    def test_get_magnitude(self):

        self.assertEqual(self.integer_case.get_magnitude(), math.sqrt(self.integer_case.x ** 2 + self.integer_case.y ** 2), "Integer substraction fails")

        self.assertEqual(self.float_case.get_magnitude(), math.sqrt(self.float_case.x ** 2 + self.float_case.y ** 2), "Integer substraction fails")

        self.assertEqual(self.integer_negative_case.get_magnitude(), math.sqrt(self.integer_negative_case.x ** 2 + self.integer_negative_case.y ** 2), "Integer substraction fails")

        self.assertEqual(self.float_negative_case.get_magnitude(), math.sqrt(self.float_negative_case.x ** 2 + self.float_negative_case.y ** 2), "Integer substraction fails")

        self.assertEqual(self.negative_case.get_magnitude(), math.sqrt(self.negative_case.x ** 2 + self.negative_case.y ** 2), "Integer substraction fails")

        self.assertEqual(self.zero_case.get_magnitude(), math.sqrt(self.zero_case.x ** 2 + self.zero_case.y ** 2), "Integer substraction fails")

    def test_normalize(self):

        self.assertEqual(self.integer_case.normalize(), Vector2d(self.integer_case.x / self.integer_case.get_magnitude(), self.integer_case.y / self.integer_case.get_magnitude()), "Integer substraction fails")

        self.assertEqual(self.float_case.normalize(), Vector2d(self.float_case.x / self.float_case.get_magnitude(), self.float_case.y / self.float_case.get_magnitude()), "Integer substraction fails")

        self.assertEqual(self.integer_negative_case.normalize(), Vector2d(self.integer_negative_case.x / self.integer_negative_case.get_magnitude(), self.integer_negative_case.y / self.integer_negative_case.get_magnitude()), "Integer substraction fails")

        self.assertEqual(self.float_negative_case.normalize(), Vector2d(self.float_negative_case.x / self.float_negative_case.get_magnitude(), self.float_negative_case.y / self.float_negative_case.get_magnitude()), "Integer substraction fails")

        self.assertEqual(self.negative_case.normalize(), Vector2d(self.negative_case.x / self.negative_case.get_magnitude(), self.negative_case.y / self.negative_case.get_magnitude()), "Integer substraction fails")

        self.assertEqual(self.zero_case.normalize(), Vector2d(0, 0), "Integer substraction fails")


if __name__ == '__main__':
    unittest.main()

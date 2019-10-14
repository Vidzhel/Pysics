import unittest

from core.math.geometry.geometry_objects import Circle, ConvexPolygon
from core.math.vector2d import Vector2d
from core.objects.object import Object


class TestObjectComponents(unittest.TestCase):
    
    circle_shape = Circle(Vector2d(0, 0), 1.0)
    polygon_shape = ConvexPolygon([Vector2d(0, 1), Vector2d(1, 1), Vector2d(1, 0), Vector2d(0, 0)])

    _object = Object(circle_shape)

    def test_force_adding(self):
        self._object.add_force(Vector2d(10, 10))

        self.assertEqual(self._object.result_force, Vector2d(10, 10))

        self._object.clear_force()

    def test_force_subtraction(self):
	    self._object.subtract_force(Vector2d(10, 10))

        self.assertEqual(self._object.result_force, Vector2d(-10, -10))

        self._object.clear_force()


        
if __name__ == '__main__':
    unittest.main()
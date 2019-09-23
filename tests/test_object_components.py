import unittest
from core.vector2d import Vector2d
from core.Objects.objects import Object
from core.Objects.shapes import Circle, Polygon

class TestObjectComponents(unittest.TestCase):
    
    circle_shape = Circle(Vector2d(0, 0), 1.0)
    polygon_shape = Polygon([Vector2d(0, 1), Vector2d(1, 1), Vector2d(1, 0), Vector2d(0, 0)])

    _object = Object(circle_shape)

    def test_force_adding(self):
        self._object.add_force(Vector2d(10, 10))

        self.assertEqual(self._object.result_force, Vector2d(10, 10))

        self._object.clear_force()

    def test_force_substraction(self):
        self._object.substract_force(Vector2d(10, 10))

        self.assertEqual(self._object.result_force, Vector2d(-10, -10))

        self._object.clear_force()


        
if __name__ == '__main__':
    unittest.main()
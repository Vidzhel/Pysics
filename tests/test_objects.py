import unittest
from core.vector2d import Vector2d
from core.Objects.objects import Object, NonInteractiveObject, StaticNonInteractiveObject, StaticObject
from core.Objects.shapes import Circle, Polygon

class Test_Objects(unittest.TestCase):
    
    circle_shape = Circle(1.0)
    polygon_shape = Polygon()

    _object = Object(circle_shape)
    static_object = StaticObject(circle_shape)
    static_non_interactive_object = StaticNonInteractiveObject(circle_shape)
    non_interactive_object = NonInteractiveObject(circle_shape)

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
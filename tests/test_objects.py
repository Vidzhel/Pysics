import unittest
from core.vector2d import Vector2d
from core.Objects.objects import Object
from core.Objects.shapes import Circle, Polygon

class TestObjects(unittest.TestCase):
    
    _object = Object("Object1")

    def test_maintaining_component(self):
        transform = _object.get_component(components.TRANSFORM_COMPONENT)
        self.assertIsInstance(transform, components.TransformComponent)

        _object.del_component(components.TRANSFORM_COMPONENT)
        transform = _object.get_component(components.TRANSFORM_COMPONENT)
        self.assertIsNone(transform)
        
        _object.add_component(components.TRANSFORM_COMPONENT)
        transform = _object.get_component(components.TRANSFORM_COMPONENT)
        self.assertIsInstance(transform, components.TransformComponent)


        
if __name__ == '__main__':
    unittest.main()
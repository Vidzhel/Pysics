import unittest

from core.force_generators.force_generators import (StaticForceGenerator, CalculatedForceGenerator,
                                                    TemporaryForceGenerator, ConditionalForceGenerator)
from core.math.geometry.geometry_objects import Circle
from core.math.vector2d import Vector2d
from core.objects.objects import Object, BaseNonStaticObject


def calculator(obj: BaseNonStaticObject, time: float):
    mass = obj.mass

    return Vector2d(1, 1).scale(mass)


def condition(obj):
    if obj.mass == 10:
        return True

    return False


class TestBaseForceGenerators(unittest.TestCase):

    shape = Circle(Vector2d(0, 0),1)

    _object = Object(shape)

    static_force_generator = StaticForceGenerator(
        "Test Static Force", Vector2d(0, -10), [_object])
    calculated_force_generator = CalculatedForceGenerator(
        "Test Calculated Force", [_object], calculator)
    temporary_force_generator = TemporaryForceGenerator(
        "Test Temporary Force", Vector2d(10, 0), [_object], 2000)
    conditional_force_generator = ConditionalForceGenerator(
        "Test Conditional Force", Vector2d(-10, 0), [_object], condition)

    def test_static_force(self):

        self.static_force_generator.apply_force(1)

        self.assertEqual(self._object.result_force,
                         Vector2d(0, -10), "Static force error")

        self._object.clear_force()

    def test_calculated_force(self):

        self.calculated_force_generator.apply_force(1)

        self.assertEqual(self._object.result_force,
                         Vector2d(1, 1).scale(self._object.mass), "Calculated force error")

        self._object.clear_force()

    def test_conditional_force(self):

        self.conditional_force_generator.apply_force(1)

        self.assertEqual(self._object.result_force,
                         Vector2d(0, 0), "Conditional force (condition == False) error")

        self._object.mass = 10

        self.conditional_force_generator.apply_force(1)

        self.assertEqual(self._object.result_force,
                         Vector2d(-10, 0), "Conditional force (condition == True) error")

        self._object.mass = 1

        self._object.clear_force()

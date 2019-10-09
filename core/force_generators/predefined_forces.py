from typing import List

from core.force_generators import force_generators
from core.math.vector2d import Vector2d
from core.objects.objects import BaseNonStaticObject


class DrugForce(force_generators.StaticForceGenerator):
    """Apply drug force on all non static objects"""

    def __init__(self, name: str, targeted_objects: List[BaseNonStaticObject],
                 coefficient_low_velocity: float, coefficient_high_velocity: float) -> None:
        """
        Parameters:
        name (str): name of the force
        targeted_objects (List[BaseNonStaticObject]): objects on which the force will be applied
        all static objects will be omitted
        """

        super().__init__(name, targeted_objects)

        self.coefficient_low_velocity = coefficient_low_velocity
        self.coefficient_high_velocity = coefficient_high_velocity

    def calculate_force(self, _object: BaseNonStaticObject) -> Vector2d:
        """Calculates drug force for an object"""
        velocity = _object.velocity.get_magnitude()
        velocity_direction = _object.velocity.normalize()

        force_magnitude = self.coefficient_low_velocity * velocity
        force_magnitude += self.coefficient_high_velocity * velocity * velocity

        force = velocity_direction.scale(force_magnitude)

        # Force has opposite the velocity direction
        force.inverse()

        return force


class GravityForce(force_generators.ConditionalForceGenerator):
    """Apply gravity force on all non static objects"""

    def __init__(self, name: str, targeted_objects: List[BaseNonStaticObject],
                 free_fall_coefficient: float) -> None:
        """
        Parameters:
        name (str): name of the force
        targeted_objects (List[BaseNonStaticObject]): objects on which the force will be applied
        all static objects will be omitted
        """

        super().__init__(name, targeted_objects,)

        self.free_fall_coefficient = free_fall_coefficient

    def calculate_force(self, _object: BaseNonStaticObject) -> Vector2d:
        """Calculates gravity force for an object"""
        force_magnitude = self.free_fall_coefficient * _object.mass

        force = Vector2d(0, force_magnitude)

        return force

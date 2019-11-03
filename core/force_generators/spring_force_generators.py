from typing import List

from core.force_generators.force_generators import StaticForceGenerator
from core.math.vector2d import Vector2d
from core.objects.object import BaseNonStaticObject


class SpringForceGenerator(StaticForceGenerator):
    """Uses Hook's Law to calculate spring force between objects

    If you need objects attract to each other than add this force generetor to both objects"""

    def __init__(self, name: str, force: Vector2d, rest_length: float, spring_coefficient: float,
                 attracting_object: BaseNonStaticObject, targeted_objects:
                 List[BaseNonStaticObject]) -> None:
        """
        Parameters:
        name (str): name of the force
        force (Vector2d): force that will applied to the objects
        rest_length (float): length of a spring in rest state
        attracting_object (BaseNonStaticObject): object that will attract other
        targeted_objects (List[BaseNonStaticObject]): objects on which the force will be applied
        all static objects will be omitted
        duration (float): the time that a force will be active
        """

        super().__init__(name, force, targeted_objects)

        self.rest_length = rest_length
        self.attracting_object = attracting_object
        self.spring_coefficient = spring_coefficient

    def apply_force(self, time_since_last_apply: float) -> None:

        attracting_object_pos = self.attracting_object.position

        for obj in self.targeted_objects:
            force = self.calculate_force(attracting_object_pos, obj)
            obj.add_force(force)

    def calculate_force(
            self, attracting_object_pos: Vector2d, obj: BaseNonStaticObject) -> Vector2d:
        current_spring_length = obj.position - attracting_object_pos
        force_direction = current_spring_length.normalize()

        force_magnitude = current_spring_length.get_magnitude()
        force_magnitude = abs(force_magnitude - self.rest_length)
        force_magnitude *= self.spring_coefficient

        force = force_direction.scale(force_magnitude)
        return force

class AnchoredSpringForceGenerator(StaticForceGenerator):
    """Uses Hook's Law to calculate spring force between objects and anchor"""

    def __init__(self, name: str, force: Vector2d, rest_length: float, spring_coefficient: float,
                 anchor_point: Vector2d, targeted_objects:
                 List[BaseNonStaticObject]) -> None:
        """
        Parameters:
        name (str): name of the force
        force (Vector2d): force that will applied to the objects
        rest_length (float): length of a spring in rest state
        anchor_point (Vector2d): point that will attract objects
        targeted_objects (List[BaseNonStaticObject]): objects on which the force will be applied
        all static objects will be omitted
        duration (float): the time that a force will be active
        """

        super().__init__(name, force, targeted_objects)

        self.rest_length = rest_length
        self.anchor_point = anchor_point
        self.spring_coefficient = spring_coefficient

    def apply_force(self, time_since_last_apply: float) -> None:

        for obj in self.targeted_objects:
            force = self.calculate_force(self.anchor_point, obj)
            obj.add_force(force)

    def calculate_force(
            self, attracting_object_pos: Vector2d, obj: BaseNonStaticObject) -> Vector2d:
        current_spring_length = obj.position - attracting_object_pos
        force_direction = current_spring_length.normalize()

        force_magnitude = current_spring_length.get_magnitude()
        force_magnitude = abs(force_magnitude - self.rest_length)
        force_magnitude *= self.spring_coefficient

        force = force_direction.scale(force_magnitude)
        return force


class BungeeForceGenerator(StaticForceGenerator):
    """Uses Hook's Law to calculate spring force between objects but only if
    the distance between objects bigger than rest length, it creates behavior
    of elastic rope

    If you need objects attract to each other than add this force generetor to both objects"""

    def __init__(self, name: str, force: Vector2d, rest_length: float, spring_coefficient: float,
                 attracting_object: BaseNonStaticObject, targeted_objects:
                 List[BaseNonStaticObject]) -> None:
        """
        Parameters:
        name (str): name of the force
        force (Vector2d): force that will applied to the objects
        rest_length (float): length of a spring in rest state
        attracting_object (BaseNonStaticObject): object that will attract other
        targeted_objects (List[BaseNonStaticObject]): objects on which the force will be applied
        all static objects will be omitted
        duration (float): the time that a force will be active
        """

        super().__init__(name, force, targeted_objects)

        self.rest_length = rest_length
        self.attracting_object = attracting_object
        self.spring_coefficient = spring_coefficient

    def apply_force(self, time_since_last_apply: float) -> None:

        attracting_object_pos = self.attracting_object.position

        for obj in self.targeted_objects:
            force = self.calculate_force(attracting_object_pos, obj)
            obj.add_force(force)

    def calculate_force(
            self, attracting_object_pos: Vector2d, obj: BaseNonStaticObject) -> Vector2d:
        current_spring_length = obj.position - attracting_object_pos

        if current_spring_length.get_magnitude() <= self.rest_length:
            return Vector2d(0, 0)

        force_direction = current_spring_length.normalize()

        force_magnitude = current_spring_length.get_magnitude()
        force_magnitude = abs(force_magnitude - self.rest_length)
        force_magnitude *= self.spring_coefficient

        force = force_direction.scale(force_magnitude)
        return force


class BuoyancyForceGenerator(StaticForceGenerator):
    """Uses Hook's Law to calculate spring force between objects

    If you need objects attract to each other than add this force generetor to both objects"""

    def __init__(self, name: str, force: Vector2d, trigger_object_density: float,
                 trigger_object: BaseNonStaticObject, force_direction: Vector2d, targeted_objects:
                 List[BaseNonStaticObject]) -> None:
        """
        Parameters:
        name (str): name of the force
        force (Vector2d): force that will applied to the objects
        rest_length (float): length of a spring in rest state
        trigger_object (BaseNonStaticObject): object that will trigger force generator if targets
                                              collide with the object
        trigger_object_density (float): density of a pure water is 1000 kg per cubic meter
        targeted_objects (List[BaseNonStaticObject]): objects on which the force will be applied
        all static objects will be omitted
        duration (float): the time that a force will be active
        """

        super().__init__(name, force, targeted_objects)

        self.trigger_object = trigger_object
        self.trigger_object_density = trigger_object_density
        self.force_direction = force_direction.normalize()

    def apply_force(self, time_since_last_apply: float) -> None:

        for obj in self.targeted_objects:
            if obj.is_colliding_with(self.trigger_object):
                force = self.calculate_force(obj)
                obj.add_force(force)

    def calculate_force(self, obj: BaseNonStaticObject) -> Vector2d:
        
        collision_info = obj.get_collision_info(self.trigger_object)
        penetration_depth = collision_info.penetration_depth
        object_height = obj.shape.get_height()

        if penetration_depth >= object_height:
            area = obj.shape.get_area()
            force_magnitude = self.completely_submerged(penetration_depth, area)

        else:
            penetration_part_area = collision_info.get_penetration_part_area()
            force_magnitude = self.completely_submerged(penetration_part_area, area)

        force = self.force_direction.scale(force_magnitude)
        return force


    def completely_submerged(self, penetration_part_area: float, area: float) -> float:
        force_magnitude = penetration_part_area * area

        return force_magnitude

class StiffSpringForceGenerator(StaticForceGenerator):
	raise NotImplemented()

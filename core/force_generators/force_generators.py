from typing import List, Callable

from core.math.vector2d import Vector2d
from core.objects.objects import BaseNonStaticObject


class BaseForceGenerator:

    def __init__(self, name: str, targeted_objects: List[BaseNonStaticObject]) -> None:
        """
        Parameters:
        name (str): name of the force
        force (Vector2d): force that will applied to the objects
        targeted_objects (List[BaseNonStaticObject]): objects on which the force will be applied
        all static objects will be omitted
        """
        self.name = name
        self.targeted_objects = targeted_objects
        self.active = True

    def apply_force(self, time_since_last_apply: float) -> None:
        pass

    def is_active(self) -> bool:
        return self.active

    def deactivate_force(self) -> None:
        """Deactivate force, afterwards it will be deleted"""
        self.active = False

    def __str__(self):
        return f"{self.name}({self.active}): \n\n {self.targeted_objects}"


class StaticForceGenerator(BaseForceGenerator):
    """A class for static force (will apply a force all the time)

    Inherit from the class to create you own force
    that ypu can add to a scene forces registry, afterwards
    the force will be applied on specified objects using apply_force
    method

    """

    def __init__(self, name: str, force: Vector2d, targeted_objects: List[BaseNonStaticObject]) -> None:
        """
        Parameters:
        name (str): name of the force
        force (Vector2d): force that will applied to the objects
        targeted_objects (List[BaseNonStaticObject]): objects on which the force will be applied
        all static objects will be omitted
        duration (float): the time that a force will be active
        """

        super().__init__(name, targeted_objects)

        self.force = force

    def apply_force(self, time_since_last_apply: float) -> None:
        """The method will be called by update_scene method of Scene object

        all static objects will be omitted
        """

        if not self.is_active():
            return None

        for obj in self.targeted_objects:
            obj.add_force(self.force)

    def __str__(self):
        return f"{self.name} (Force: {self.force}) (Active: {self.active}): \n\n {self.targeted_objects}"


class CalculatedForceGenerator(BaseForceGenerator):
    """
    A class for temporary force (will apply a force
    while duration > 0)

    Inherit from the class to create you own force
    that ypu can add to a scene forces registry, afterwards
    the force will be applied on specified objects using apply_force
    method
    """

    def __init__(self, name: str, targeted_objects: List[BaseNonStaticObject],
                 calculator: Callable[[BaseNonStaticObject, float], Vector2d]) -> None:
        """
        Parameters:
        name (str): name of the force
        targeted_objects (List[BaseNonStaticObject]): objects on which the force will be applied
        all static objects will be omitted
        calculator: a function which will be given target object and time_since_last_apply
        parameters
        """

        super().__init__(name, targeted_objects)

        self.calculate_force = calculator

    def apply_force(self, time_since_last_apply: float):
        """The method will be called by update_scene method of a Scene object
        which in the turn will call calculate_force function

        all static objects will be omitted
        """

        if not self.is_active():
            return None

        for obj in self.targeted_objects:
            force = self.calculate_force(obj, time_since_last_apply)
            obj.add_force(force)


class TemporaryForceGenerator(BaseForceGenerator):
    """A class for temporary force (will apply a force
    while duration > 0)

    Inherit from the class to create you own force
    that ypu can add to a scene forces registry, afterwards
    the force will be applied on specified objects using apply_force
    method
    """

    def __init__(self, name: str, force: Vector2d, targeted_objects: List[BaseNonStaticObject],
                 duration: float) -> None:
        """
        Parameters:
        name (str): name of the force
        force (Vector2d): force that will applied to the objects
        targeted_objects (List[BaseNonStaticObject]): objects on which the force will be applied
        all static objects will be omitted
        duration (float): the time that a force will be active
        """

        super().__init__(name, targeted_objects)

        self.force = force
        self.duration = duration

    def apply_force(self, time_since_last_apply: float) -> None:
        """The method will be called by update_scene method of Scene object
        Disables force when duration <= 0

        all static objects will be omitted
        """

        if not self.is_active():
            return None

        if self.duration <= 0:
            self.deactivate_force()
            return None

        for obj in self.targeted_objects:
            obj.add_force(self.force)

        self.duration -= time_since_last_apply

    def __str__(self):
        return f"{self.name} (Duration: {self.duration}s)(Active: {self.active}): \n\n {self.targeted_objects}"


class ConditionalForceGenerator(BaseForceGenerator):
    """Class for a conditional force (will apply force if
    a conditional function return true)

    Inherit from the class to create you own force
    that ypu can add to a scene forces registry, afterwards
    the force will be applied on specified objects using apply_force
    method

    """

    def __init__(self, name: str, force: Vector2d, targeted_objects: List[BaseNonStaticObject],
                 condition: Callable[[BaseNonStaticObject], bool]) -> None:
        """
        Parameters:
        name (str): name of the force
        force (Vector2d): force that will applied to the objects
        targeted_objects (List[BaseNonStaticObject]): objects on which the force will be applied
        all static objects will be omitted
        condition (Callable[[BaseNonStaticObject], bool])): a function that decide apply a force or not
        """

        super().__init__(name, targeted_objects)

        self.force = force
        self.condition = condition

    def apply_force(self, time_since_last_apply: float) -> None:
        """The method will be called by update_scene method of Scene object

        all static objects will be omitted
        """

        if not self.is_active():
            return None

        for obj in self.targeted_objects:
            if self.condition(obj):
                obj.add_force(self.force)

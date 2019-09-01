from typing import List, Callable
from core.vector2d import Vector2d
from core.Objects.objects import BaseObject

class BaseForceGenerator:

    def __init__(self, name: str, force: Vector2d, targeted_objects: List[BaseObject]) -> None:
        """
        Parameters:
        name (str): name of the force
        force (Vector2d): force that will applied to the objects
        targeted_objects (List[BaseObject]): objects on which the force will be applied
        all static objects will be omitted
        """
        self.name = name
        self.force = force
        self.targeted_objects = targeted_objects
        self.active = True

    def apply_force(self, time_since_last_apply) -> None:
        pass

    def is_active(self) -> bool:
        return self.active

    def deactivate_force(self) -> None:
        """Deactivate force, afterwards it will be deleted"""
        self.active = False

class StaticForceGenerator(BaseForceGenerator):
    """A class for static force (will apply a force all the time)
    
    Inherit from the class to create you own force
    that ypu can add to a scene forces registry, afterwards
    the force will be applied on specified objects using apply_force
    method

    """

    def apply_force(self, time_since_last_apply) -> None:
        """The method will be called by update_scene method of Scene object
        
        all static objects will be omitted
        """

        if not self.is_active():
            return None

        for obj in self.targeted_objects:
            if not obj.is_static():
                obj.add_force(self.force)

class TemporaryForceGenerator(BaseForceGenerator):
    """A class for temporary force (will apply a force
    while duration > 0)
    
    Inherit from the class to create you own force
    that ypu can add to a scene forces registry, afterwards
    the force will be applied on specified objects using apply_force
    method

    """

    def __init__(self, name: str, force: Vector2d, targeted_objects: List[BaseObject],
                 duration: float) -> None:
        """
        Parameters:
        name (str): name of the force
        force (Vector2d): force that will applied to the objects
        targeted_objects (List[BaseObject]): objects on which the force will be applied
        all static objects will be omitted
        duration (float): the time that a force will be active
        """

        super().__init__(name, force, targeted_objects)

        self.duration = duration

    def apply_force(self, time_since_last_apply) -> None:
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
            if not obj.is_static():
                obj.add_force(self.force)

        self.duration -= time_since_last_apply


class ConditionalForceGenerator(BaseForceGenerator):
    """Class for a conditional force (will apply force if
    a conditional function return true)
    
    Inherit from the class to create you own force
    that ypu can add to a scene forces registry, afterwards
    the force will be applied on specified objects using apply_force
    method

    """

    def __init__(self, name: str, force: Vector2d, targeted_objects: List[BaseObject],
                 condition: Callable[[BaseObject], bool]) -> None:
        """
        Parameters:
        name (str): name of the force
        force (Vector2d): force that will applied to the objects
        targeted_objects (List[BaseObject]): objects on which the force will be applied
        all static objects will be omitted
        condition (Callable[[BaseObject], bool])): a function that decide apply a force or not
        """

        super().__init__(name, force, targeted_objects)

        self.condition = condition

    def apply_force(self, time_since_last_apply) -> None:
        """The method will be called by update_scene method of Scene object
        
        all static objects will be omitted
        """

        if not self.is_active():
            return None

        for obj in self.targeted_objects:
            if not obj.is_static() and self.condition:
                obj.add_force(self.force)

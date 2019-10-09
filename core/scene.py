from typing import List, Optional

from core.environments import Environment
from core.math.vector2d import Vector2d
from .force_generators.force_generators import BaseForceGenerator


class Scene:

    def __init__(self, width: float, height: float, origin: Vector2d,
                 environments: Optional[List[Environment]] = None,
                 time_flow_coefficient: float = 1.0,
                 force_generators: Optional[List[BaseForceGenerator]] = None) -> None:
        """Creates scene which is used to set environments and objects.

        origin (float): define origin coordinates
            can be setted in percentages using set_origin_percentages function
            starting from the left upper corner by default (0, 0)
        time_flow_coefficient (float): set the time flow speed multiplier 
        force_generators (Optional[List[BaseForceGenerator]]): list of force generators
            that apply forces on objects
        environments (Optional[List[Environment]]): list of environments in a scene
        """

        self.origin = origin
        self.environments: List[Environment] = []
        self.forces_registry: List[BaseForceGenerator] = []
        self.width = width
        self.height = height

        self.time_flow_coefficient = time_flow_coefficient

        if force_generators is not None:
            self.forces_registry.extend(force_generators)

        if environments is not None:
            self.environments.extend(environments)

    def add_force_generator(self, force_generator: BaseForceGenerator) -> None:
        """Adds force generator to the force registry"""
        self.forces_registry.append(force_generator)

    def add_environment(self, environment: Environment) -> None:
        """Adds mew environment to a scene"""
        self.environments.append(environment)

    def set_origin_percentages(self):
        pass

    def update_scene(self, time_since_last_update):
        """Updates every environment and
        apply forces in a scene
        """

        multiplied_time = self.time_flow_coefficient * time_since_last_update

        self.apply_forces(multiplied_time)
        self.update_environments(multiplied_time)

    def update_environments(self, time_since_last_update):
        for env in self.environments:
            env.update_environment(time_since_last_update)

    def apply_forces(self, time_since_last_update):
        """Apply force from each force generator and delete disabled"""

        for force_generator in self.forces_registry:

            if force_generator.is_active():
                force_generator.apply_force(time_since_last_update)

            else:
                del force_generator

    def __str__(self) -> str:
        return f"Scene consist of: \n  {self.environments} \n\n Forces: \n{self.forces_registry}"

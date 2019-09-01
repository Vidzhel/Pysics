from typing import List, Optional
from core.environments import Environment
from core.vector2d import Vector2d


class Scene:

    def __init__(self, width: float, height: float, origin: Vector2d,
                 environments: Optional[List[Environment]] = None) -> None:
        """Creates scene which uses to set environments and objects.

        origin - define origin coordinates can be setted in
                 persentages using set_origin_persentages function
        starting from the left upper corner by default (0, 0)

        environments - list of environments in a scene
        """

        self.origin = origin
        self.environments: List[Environment] = []
        self.width = width
        self.height = height

        if environments is not None:
            self.environments.extend(environments)

    def add_environment(self, environment: Environment) -> None:
        """Adds mew environment to a scene"""
        self.environments.append(environment)

    def set_origin_persentages(self):
        pass

    def update_scene(self, timestamp):
        """Updates every environment in a scene"""

        for env in self.environments:
            env.update_environment(timestamp)

    def __str__(self) -> str:
        return f"Scene consist of: \n  {self.environments}"

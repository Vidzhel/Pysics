from typing import List, Optional


class BaseObject:

    def __init__(self, density: float, pos_x: float = 0.0, pos_y: float = 0.0, origin_x: float = 0.0, origin_y: float = 0.0, rotation: float = 0.0) -> None:
        # TODO check the position regarding to the possible resolution
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.rotation = rotation
        self.density = density


class Object(BaseObject):
    """Represent an object of arbitrary size that you can put in a scene and simulate"""

    def __init__(self, density: float, pos_x: float = 0.0, pos_y: float = 0.0, origin_x: float = 0.0, origin_y: float = 0.0,
                 weight: float = 0.0, rotation: float = 0.0, allow_collisions: bool = True) -> None:
        """Create an object that you can put in scene and simulate

        Weight specified in kilograms
        Position will be calculated regarding to a scene origin coordinates
        It is possible to specify in persentage

        Rotation specified in degrees or persentages
        """

        super().__init__(density, pos_x, pos_y, origin_x, origin_y, rotation)

        self.weight = weight
        self.allow_collisions = allow_collisions


class Environment(BaseObject):
    """Represent an object that you can add to a scene and cause the object collisions"""

    def __init__(self, density, pos_x: float = 0.0, pos_y: float = 0.0, origin_x: float = 0.0, origin_y: float = 0.0,
                 weight: float = 0.0, rotation: float = 0.0, powers=None) -> None:
        """Creates an environment that you can add to a scene and cause the object collisions

        Position will be calculated regarding to a scene origin coordinates
        It is possible to specify in persentage

        Rotation specified in degrees or persentages
        """


class Scene:

    def __init__(self, origin_x: float = 0.0, origin_y: float = 0.0,
                 objects: List[Object] = None, environments: List[Environment] = None) -> None:
        """Creates scene which uses to set environments and objects.

        origin_x, origin_y - define origin coordinates (in percentages)
        starting from the left upper corner by default (0, 0)

        objects - list of objects in a scene
        environments - list of environments in a scene
        """

        self.origin_x = origin_x
        self.origin_y = origin_y
        self.objects: List[Object] = []
        self.environments: List[Environment] = []

        if(objects is not None):
            self.objects.extend(objects)

        if(environments is not None):
            self.environments.extend(environments)

    def add_object(self, _object: Object) -> None:
        """Adds new object to a scene"""
        self.objects.append(_object)

    def add_enviroment(self, environment: Environment) -> None:
        """Adds mew environment to a scene"""
        self.environments.append(environment)

    def __str__(self) -> str:
        return f"Scene consist of:\n {self.objects} \n  {self.environments}"

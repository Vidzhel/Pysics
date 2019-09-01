from core.Objects.objects import BaseObject
from core.vector2d import Vector2d
from core.Objects import shapes


class Environment(BaseObject):
    """Represent an object that you can add to a scene and cause the object collisions"""

    def __init__(self, density: float, shape: shapes.shape_type, objects: Optional[List[BaseObject]] = None, position: Vector2d = Vector2d(0, 0), origin: Vector2d = Vector2d(0, 0),
                 rotation: float = 0.0, forces=None, allow_object_collisions=True, static_objects_positioning=False) -> None:
        """Creates an environment that you can add to a scene and cause the object collisions

        Position will be calculated regarding to a scene origin coordinates
        It is possible to specify position in persentages using set_position_persentages() and set_origin_persentages() functions

        Rotation specified in degrees, you can use set_rotation_presentages to set rotation in persentages

        allow_object_collisions: defines whether the objects of an environment will interact or not
        static_objects_positioning: defines whether the objects of an environment will move due to collisions
        """

        super().__init__(shape, density, position, origin, rotation)

        self.objects = []
        if objects is not None:
            self.objects = objects

        self.forces = forces
        self.allow_object_collisions = allow_object_collisions
        self.static_objects_positioning = static_objects_positioning

    def add_force(self, force):
        if(self.forces is not None):
            self.forces.append(force)

    def set_position_persentages(self):
        pass

    def set_origin_persentages(self):
        pass

    def set_rotation_presentages(self):
        pass

    def update_environment(self, timestamp):
        """Updates every object in an environment"""

        for obj in self.objects:
            obj.update_object(timestamp)

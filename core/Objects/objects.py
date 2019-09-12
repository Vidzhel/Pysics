from core.vector2d import Vector2d
from . import shapes


class BaseObject:

    def __init__(self, shape: shapes.BaseShape,
                 position: Vector2d = Vector2d(0, 0), origin: Vector2d = Vector2d(0, 0), rotation: float = 0.0) -> None:

        # TODO check the position regarding to the scene size
        self.position = position
        self.origin = origin

        self.rotation = rotation

        self.shape = shape

    def is_static(self):
        pass

    def set_position_persentages(self):
        pass

    def set_origin_persentages(self):
        pass

    def set_rotation_presentages(self):
        pass


class BaseNonStaticObject(BaseObject):
    """Represent an object of arbitrary size that you can put in a scene and simulate"""

    def __init__(self, shape: shapes.BaseShape,
                 velocity: Vector2d = Vector2d(0, 0),
                 position: Vector2d = Vector2d(0, 0),
                 origin: Vector2d = Vector2d(0, 0), mass: float = 1.0,
                 force: Vector2d = Vector2d(0, 0),
                 rotation: float = 0.0) -> None:
        """Create an object that you can interact with other objects

        Position will be calculated regarding to a scene origin coordinates
        It is possible to specify position in persentage
         using set_position_persentages() and set_origin_persentages() functions

        Rotation specified in degrees, you can
         use set_rotation_presentages to set rotation in persentages

        """

        super().__init__(shape, position, origin, rotation)

        self.mass = mass
        self.inverted_mass = 1/mass

        self.result_force = force

        self.velocity = velocity

    def is_static(self):
        return False

    def add_force(self, force: Vector2d) -> None:
        self.result_force = self.result_force + force

    def substract_force(self, force: Vector2d) -> None:
        self.result_force = self.result_force - force

    def clear_force(self) -> None:
        self.result_force = Vector2d(0, 0)

    def update_object(self, time_since_last_update: float) -> None:
        pass


class BaseStaticObject(BaseObject):
    """Represent an object that you can use as static object or decoration """

    def is_static(self):
        return True


class Object(BaseNonStaticObject):

    def update_object(self, time_since_last_update: float) -> None:
        """Updated object's data (position, velocity ...)"""

        self.position.add_scaled_vector(self.velocity, time_since_last_update)

        acceleration = self.result_force.scale_vector(self.inverted_mass)
        self.velocity.add_scaled_vector(acceleration, time_since_last_update)

        self.clear_force()

    def is_static(self):
        return False


class NonInteractiveObject(BaseNonStaticObject):
    """Represent an object of arbitrary size that you can put in a scene and simulate
    but it won't be colliding with other objects

    """

    def update_object(self, time_since_last_update: float) -> None:
        """Updated object's data (position, velocity ...)"""

        self.position.add_scaled_vector(self.velocity, time_since_last_update)

        acceleration = self.result_force.scale_vector(self.inverted_mass)
        self.velocity.add_scaled_vector(acceleration, time_since_last_update)

        self.clear_force()

    def is_static(self):
        return False


class StaticObject(BaseStaticObject):

    def __init__(self, shape: shapes.BaseShape,
                 position: Vector2d = Vector2d(0, 0),
                 origin: Vector2d = Vector2d(0, 0),
                 rotation: float = 0.0) -> None:
        """Create an object that can't move but can interact with other objects

        Position will be calculated regarding to a scene origin coordinates
        It is possible to specify position in persentage
         using set_position_persentages() and set_origin_persentages() functions

        Rotation specified in degrees, you can
         use set_rotation_presentages to set rotation in persentages

        """

        super().__init__(shape, position, origin, rotation)


class StaticNonInteractiveObject(BaseStaticObject):
    pass

from core.vector2d import Vector2d
from . import shapes


class BaseObject:

    def __init__(self, shape: shapes.shape_type,
                 position: Vector2d, origin: Vector2d, rotation: float = 0.0) -> None:

        # TODO check the position regarding to the scene size
        self.position = position
        self.origin = origin

        self.rotation = rotation

        self.shape = shapes.shape_type(shape)

    def is_static(self):
        pass

    def add_force(self, force: Vector2d) -> None:
        pass

    def substract_force(self, force: Vector2d) -> None:
        pass

    def set_position_persentages(self):
        pass

    def set_origin_persentages(self):
        pass

    def set_rotation_presentages(self):
        pass


class Object(BaseObject):
    """Represent an object of arbitrary size that you can put in a scene and simulate"""

    def __init__(self, shape: shapes.shape_type,
                 velocity: Vector2d = Vector2d(0, 0),
                 position: Vector2d = Vector2d(0, 0),
                 origin: Vector2d = Vector2d(0, 0), mass: float = 0.0,
                 force: Vector2d = Vector2d(0, 0),
                 rotation: float = 0.0) -> None:
        """Create an object that you can interact with other objects

        mass specified in kilograms

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

    def add_force(self, force: Vector2d) -> None:
        self.result_force += force

    def substract_force(self, force: Vector2d) -> None:
        self.result_force -= force

    def update_object(self, time_since_last_update):
        """Updated object's data (position, velocity ...)"""

        self.position.add_scaled_vector(self.velocity, time_since_last_update)

        acceleration = self.result_force * self.inverted_mass
        self.velocity.add_scaled_vector(acceleration, time_since_last_update)

    def is_static(self):
        return False

class NonInteractiveObject(BaseObject):
    """Represent an object of arbitrary size that you can put in a scene and simulate"""

    def __init__(self, shape: shapes.shape_type,
                 velocity: Vector2d = Vector2d(0, 0),
                 position: Vector2d = Vector2d(0, 0),
                 force: Vector2d = Vector2d(0, 0),
                 origin: Vector2d = Vector2d(0, 0), mass: float = 0.0,
                 rotation: float = 0.0) -> None:
        """Create an object that you can behaves like a ghost

        mass specified in kilograms
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

    def add_force(self, force: Vector2d) -> None:
        self.result_force += force

    def substract_force(self, force: Vector2d) -> None:
        self.result_force -= force

    def update_object(self, time_since_last_update):
        """Updated object's data (position, velocity ...)"""

        self.position.add_scaled_vector(self.velocity, time_since_last_update)

        acceleration = self.result_force * self.inverted_mass
        self.velocity.add_scaled_vector(acceleration, time_since_last_update)

    def is_static(self):
        return False

class StaticObject(BaseObject):
    """Represent an object of arbitrary size that you can put in a scene and simulate"""

    def __init__(self, shape: shapes.shape_type,
                 position: Vector2d = Vector2d(0, 0),
                 origin: Vector2d = Vector2d(0, 0),
                 rotation: float = 0.0) -> None:
        """Create an object that can't move but can interact with other objects

        mass specified in kilograms
        Position will be calculated regarding to a scene origin coordinates
        It is possible to specify position in persentage
         using set_position_persentages() and set_origin_persentages() functions

        Rotation specified in degrees, you can
         use set_rotation_presentages to set rotation in persentages

        """

        super().__init__(shape, position, origin, rotation)

    def is_static(self):
        return True

class StaticNonInteractiveObject(BaseObject):
    """Represent an object of arbitrary size that you can put in a scene and simulate"""

    def __init__(self, shape: shapes.shape_type,
                 position: Vector2d = Vector2d(0, 0),
                 origin: Vector2d = Vector2d(0, 0),
                 rotation: float = 0.0) -> None:
        """Create an object that can't move but can interact with other objects

        mass specified in kilograms
        Position will be calculated regarding to a scene origin coordinates
        It is possible to specify position in persentage
         using set_position_persentages() and set_origin_persentages() functions

        Rotation specified in degrees, you can
         use set_rotation_presentages to set rotation in persentages

        """

        super().__init__(shape, position, origin, rotation)

    def is_static(self):
        return True
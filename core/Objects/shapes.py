import typing


class Circle:
    """Represent circle shape that you can use to create object"""

    def __init__(self, radius: float) -> None:
        self.radius = radius


class Particle:
    pass


class Polygon:
    pass


shape_type = typing.TypeVar("shape_type", Circle, Particle, Polygon)

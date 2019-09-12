
class BaseShape():
    pass


class Circle(BaseShape):
    """Represent circle shape that you can use to create object"""

    def __init__(self, radius: float) -> None:
        self.radius = radius


class Particle(BaseShape):
    pass


class Polygon(BaseShape):
    pass

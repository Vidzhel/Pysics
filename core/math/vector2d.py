import math


class Vector2d:
    """Represent vector in 2D space

    Provide all essential methods, in order to work with 2D vectors
    """

    def __init__(self, x: float, y: float):
	    self.x = round(float(x), 4)
	    self.y = round(float(y), 4)

    def scale(self, scalar: float) -> "Vector2d":
	    return Vector2d(self.x * scalar, self.y * scalar)

    def copy(self):
	    return Vector2d(self.x, self.y)

    def add_vector(self, another_vector: "Vector2d") -> "Vector2d":
        return Vector2d(self.x + another_vector.x, self.y + another_vector.y)

    def __add__(self, another_vector: "Vector2d") -> "Vector2d":
        return self.add_vector(another_vector)

    def __iadd__(self, another_vector: "Vector2d") -> "Vector2d":
        self.x += another_vector.x
        self.y += another_vector.y

        return self

    def project_on(self, another_vector: "Vector2d"):
	    projection_len = self.dot_product(another_vector)
	    another_vector_squared_len = another_vector.get_squared_magnitude()
	    scalar = projection_len / another_vector_squared_len

	    return another_vector.scale(scalar)

    def get_cos_of_angle(self, other: "Vector2d") -> float:
	    numerator = self.dot_product(other)
	    denominator = self.get_magnitude() * other.get_magnitude()

	    return numerator / denominator

    def get_angle(self, other: "Vector2d") -> float:
	    cos = self.get_cos_of_angle(other)
	    angle_radians = math.acos(cos)

	    return math.degrees(angle_radians)

    def get_perpendicular_vector(self):
	    return Vector2d(self.y, -self.x)

    def add_scaled_vector(self, another_vector: "Vector2d", scalar: float) -> "Vector2d":
	    return Vector2d(self.x + (another_vector.x * scalar), self.y + (another_vector.y * scalar))

    def subtract_vector(self, another_vector: "Vector2d") -> "Vector2d":
        return Vector2d(self.x - another_vector.x, self.y - another_vector.y)

    def __sub__(self, another_vector: "Vector2d") -> "Vector2d":
	    return self.subtract_vector(another_vector)

    def __isub__(self, another_vector: "Vector2d") -> "Vector2d":
        self.x -= another_vector.x
        self.y -= another_vector.y

        return self

    def cross(self, other: "Vector2d") -> float:
	    """Cross product (vector product) of vectors

		Returns the magnitude of the vector that perpendicular
		to the plain that contains these vectors
		"""

	    return (self.x * other.y) - (self.y * other.x)

    def dot_product(self, another_vector: "Vector2d") -> float:
        return self.x * another_vector.x + self.y * another_vector.y

    def get_magnitude(self) -> float:
        square_sum = self.x * self.x + self.y * self.y

        return math.sqrt(square_sum)

    def __len__(self) -> float:
        return self.get_magnitude()

    def get_squared_magnitude(self) -> float:
        return self.x * self.x + self.y * self.y

    def inverse(self) -> "Vector2d":
        return Vector2d(-self.x, -self.y)

    def __neg__(self) -> "Vector2d":
        return self.inverse()

    def normalize(self) -> "Vector2d":
        """Create unit vector from the vector"""

        magnitude = self.get_magnitude()
        normalized_x = 0.0
        normalized_y = 0.0

        if magnitude != 0:
            normalized_x = self.x / magnitude
            normalized_y = self.y / magnitude

        return Vector2d(normalized_x, normalized_y)

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Vector2d):
            return NotImplemented

        if math.isclose(self.x, other.x, abs_tol=0.01) and \
		        math.isclose(self.y, other.y, abs_tol=0.01):
            return True

        return False

    def __str__(self) -> str:
        return f"({self.x}; {self.y})"

    def __repr__(self) -> str:
        return f"Vector2d({self.x}, {self.y})"

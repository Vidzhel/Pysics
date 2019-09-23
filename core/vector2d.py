import math


class Vector2d:
    """Represent vector in 2D space

    Provide all essential methods, in order to work with 2D vectors
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def scale_vector(self, scaler: float) -> "Vector2d":
        return Vector2d(self.x * scaler, self.y * scaler)

    def add_vector(self, another_vector: "Vector2d") -> "Vector2d":
        return Vector2d(self.x + another_vector.x, self.y + another_vector.y)

    def __add__(self, another_vector: "Vector2d") -> "Vector2d":
        return self.add_vector(another_vector)

    def __iadd__(self, another_vector: "Vector2d") -> "Vector2d":
        self.x += another_vector.x
        self.y += another_vector.y

        return self

    def add_scaled_vector(self, another_vector: "Vector2d", scaler: float) -> "Vector2d":
        return Vector2d(self.x + (another_vector.x * scaler), self.y + (another_vector.y * scaler))

    def substract_vector(self, another_vector: "Vector2d") -> "Vector2d":
        return Vector2d(self.x - another_vector.x, self.y - another_vector.y)

    def __sub__(self, another_vector: "Vector2d") -> "Vector2d":
        return self.substract_vector(another_vector)

    def __isub__(self, another_vector: "Vector2d") -> "Vector2d":
        self.x -= another_vector.x
        self.y -= another_vector.y
        
        return self

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

        if(magnitude != 0):
            normalized_x = self.x / magnitude
            normalized_y = self.y / magnitude

        return Vector2d(normalized_x, normalized_y)

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Vector2d):
            return NotImplemented

        if(self.x == other.x and self.y == other.y):
            return True

        return False

    def __str__(self) -> str:
        return f"({self.x}; {self.y})"

    def __repr__(self) -> str:
        return f"Vector2d({self.x}, {self.y})"

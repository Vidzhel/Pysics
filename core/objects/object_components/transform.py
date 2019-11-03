from core.math.vector2d import Vector2d
from core.objects.properties.property import ConstrainedProperty
from .base_component import BaseComponent


class Transform(BaseComponent):
	"""Store position of an object"""

	rotation = ConstrainedProperty()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def move(self, direction: Vector2d) -> None:
		self.position.add_vector(direction)

	def rotate(self, angle: float) -> None:
		self.rotation += angle


from core.math.vector2d import Vector2d
from .base_component import BaseComponent, CT_TRANSFORM
from core.objects.game_object import GameObject


class Transform(BaseComponent):

	def __init__(self, name: str, attached_obj: GameObject, position: Vector2d = Vector2d(0, 0),
	             rotation: float = 0.0):
		super().__init__(name, CT_TRANSFORM, attached_obj)

		self.position = position
		self.rotation = rotation

	def move(self, direction: Vector2d) -> None:
		self.position.add_vector(direction)

	def rotate(self, angle: float) -> None:
		self.rotation += angle

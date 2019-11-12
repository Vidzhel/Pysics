from typing import TYPE_CHECKING

from core.objects.object_components.base_component import BaseComponent

if TYPE_CHECKING:
	from core.math.geometry.geometry_objects import BaseShape, Rectangle


class Shape(BaseComponent):
	center_mass_x = None
	center_mass_y = None

	def __init__(self, **kwargs):
		super(Shape, self).__init__(**kwargs)
		self._shapes = []

	def attach_shape(self, shape: "BaseShape"):
		self._shapes.append(shape)

	def detach_shape(self, shape: "BaseShape"):
		self._shapes.remove(shape)

	def get_border_box(self) -> "Rectangle":
		raise NotImplementedError()

	def get_positioned_border_box(self) -> "Rectangle":
		raise NotImplementedError()

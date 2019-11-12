from typing import TYPE_CHECKING

from core.math.vector2d import Vector2d
from .base_layout import Layout

if TYPE_CHECKING:
	pass


class Canvas(Layout):

	def __init__(self):
		super(Canvas, self).__init__()

	@property
	def origin(self) -> Vector2d:
		NotImplementedError()

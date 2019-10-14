from typing import Set

from core.objects.object import Object
from core.objects.object_components.sprite_renderer import SpriteRenderer
from logger.loggers import LoggingSystem as Logger


class Layer(Object):

	def __init__(self, name: str):
		super(Layer, self).__init__(name)

		self.components: Set[SpriteRenderer] = set()

	def update(self, delta_time: float) -> None:
		pass

	def attach_render_component(self, render_component: SpriteRenderer):
		if self.is_exist(render_component):
			Logger.log_error(
				"Component with the same component id{} and attached object{} already exists".format(
					render_component.id, render_component.attached_obj))
			raise AttributeError(
				"Component with the same component id{} and attached object{} already exists".format(
					render_component.id, render_component.attached_obj))

		self.components.add(render_component)

	def is_exist(self, render_component: SpriteRenderer) -> bool:
		for component in self.components:
			if component == render_component:
				return True

		return False

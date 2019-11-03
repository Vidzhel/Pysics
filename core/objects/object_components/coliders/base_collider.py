from abc import abstractmethod
from typing import TYPE_CHECKING

from core.math.geometry.geometry_objects import BaseShape
from core.objects.entity import Entity
from core.objects.object_components.base_component import BaseComponent

if TYPE_CHECKING:
	from core.objects.object_components.bodies.base_body import BaseBody


class BaseCollider(BaseComponent):

	def __init__(self, name: str, component_type: str, body: BaseBody, attached_obj: Entity,
	             shape: BaseShape,
	             is_approximated_shape: bool = False):
		super(BaseCollider, self).__init__(name, component_type, attached_obj)

		self.shape = shape
		self.body = body
		self.is_approximated_shape = is_approximated_shape

	def update_component(self):
		if self.body:
			return

	# TODO Events

	@abstractmethod
	def on_collision_enter(self):
		raise NotImplemented()

	@abstractmethod
	def on_collision_stay(self):
		raise NotImplemented()

	@abstractmethod
	def on_collision_exit(self):
		raise NotImplemented()

	@abstractmethod
	def on_trigger_enter(self):
		raise NotImplemented()

	@abstractmethod
	def on_trigger_stay(self):
		raise NotImplemented()

	@abstractmethod
	def on_trigger_exit(self):
		raise NotImplemented()

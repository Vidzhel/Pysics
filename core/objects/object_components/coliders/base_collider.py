from core.objects.object_components.base_component import BaseComponent
from core.math.geometry.geometry_objects import BaseShape
from core.objects.game_object import GameObject


class BaseCollider(BaseComponent):

	def __init__(self, name: str, component_type: str, attached_obj: GameObject, shape: BaseShape,
	             is_approximated_shape: bool = false):
		super(BaseCollider, self).__init__(name, component_type, attached_obj)

		self.shape = shape
		self.is_approximated_shape = is_approximated_shape

	def update_component(self):
		pass

	# TODO Events

	def on_collision_enter(self):
		pass

	def on_collision_stay(self):
		pass

	def on_collision_exit(self):
		pass

	def on_trigger_enter(self):
		pass

	def on_trigger_stay(self):
		pass

	def on_trigger_exit(self):
		pass

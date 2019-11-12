from typing import Optional

from core.math.vector2d import Vector2d
from core.objects.entity import Entity
from core.objects.object_components.layouts.base_layout import Layout
from core.objects.object_components.shape import Shape
from events.event_arguments import PropertyChangedEventArgs
from .base_systems import System


class LayoutSystem(System):
	__required_components = [Layout, Shape]

	def add_entity_to_queue(self, entity: "Entity"):
		entity.bind_event_callback(depth=self._on_entity_depth_changed_handler)
		depth = entity.depth
		level = self._process_queue_storage.get(depth, None)

		if level is None:
			level = self._process_queue_storage[depth] = []

		entity.bind_event_callback(on_component_changed=self._relative_value_handler)
		level.append(entity)

	def remove_entity_from_queue(self, entity):
		self._process_queue_storage[entity.depth].remove(entity)
		entity.unbind_event_callback(depth=self._on_entity_depth_changed_handler)
		entity.unbind_event_callback(on_component_changed=self._relative_value_handler)

	def run(self):
		for level in self._process_queue_storage.values():
			for obj in level:
				self.position(obj)

	def position(self, entity: "Entity"):
		component = entity.get_component_by_type(Layout)
		handler = component.__class__.__name__.lower() + "_position"
		# TODO handle exception if unsupported layout type
		self.__dict__[handler](entity)

	def canvas_position(self, entity):
		CanvasPositioning.canvas_position(entity)
		layout: Layout = entity.get_component_by_type(Layout)

		for child in layout.children:
			CanvasPositioning.canvas_position(child)

	def grid_position(self, entity: "Entity"):
		pass

	def stack_position(self, entity: "Entity"):
		pass

	def _relative_value_handler(self, sender: "Entity", event_args: "PropertyChangedEventArgs"):
		self.position(sender)


# TODO implement async position on children

# Get object from queue
# Do layout
#   Calculate position, rotation
#   Calculate Shape, adjust size (clip overflow), set center mass
#   Calculate position origin
#   Translate shape to position origin and rotate
#   If there is the layout system layout =>
#       Calculate parent origin
# Do layout for children


class CanvasPositioning:

	@classmethod
	def position(cls, entity: "Entity"):
		cls.position_layout(entity)
		cls.position_children(entity)

	@classmethod
	def position_children(cls, entity: "Entity"):
		cls.calculate_position(entity)

	@classmethod
	def position_layout(cls, entity: "Entity"):
		"""Sets initial position to an entity with no parent"""
		transform = entity.transform

		# Relative values are disallowed if there is no parent
		if transform.is_relative_value(transform.pos_x) or transform.is_relative_value(
				transform.pos_y) or transform.is_relative_value(transform.rotation):
			raise Exception(
				"Can't calculate relative position value for entity with no parent, entity {}".format(
					entity))

		transform.actual_pos_x = 0
		transform.actual_pos_y = 0
		transform.actual_rotation = 0

	@classmethod
	def calculate_position(cls, entity: "Entity"):
		transform = entity.transform

		if entity.parent is None:
			cls.calculate_abs_position(entity)

		parent_shape: Optional[Shape] = entity.parent.get_component_by_type(Shape)
		parent_layout: Optional[Layout] = entity.parent.get_component_by_type(Layout)
		parent_transform = entity.parent.transform

		# If value relative than calculate and set relative value in pixels, and then it'll be called and
		# used to set actual position
		if transform.is_relative_value(transform.pos_x):
			transform.pos_x = parent_shape.get_border_box().width * transform.pos_x.value
		else:
			transform.actual_pos_x = parent_layout.parent_origin_x + transform.pos_x

		if transform.is_relative_value(transform.pos_y):
			transform.pos_x = parent_shape.get_border_box().width * transform.pos_x
		else:
			transform.actual_pos_y = parent_layout.parent_origin_y + transform.pos_y

		if transform.is_relative_value(transform.rotation):
			transform.rotation = parent_transform.rotation * transform.rotation
		else:
			transform.actual_rotation = parent_transform.rotation + transform.rotation

		border_box = parent_shape.get_positioned_border_box()
		border_box.is_point_belongs(Vector2d(transform.ac))

	@classmethod
	def calculate_abs_position(cls, entity: "Entity"):
		pass

	@classmethod
	def calculate_shape(cls, entity: Entity):
		pass

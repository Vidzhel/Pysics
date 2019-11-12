from typing import Optional, Union

from core.math.vector2d import Vector2d
from core.objects.constraints.position_constraint import (PositionConstraint,
                                                          RelativeRotation)
from core.objects.object_components.base_component import BaseComponent
from core.objects.properties.property import ConstrainedProperty
from events.event_arguments import PropertyChangedEventArgs


class Transform(BaseComponent):
	"""Store position of an object

	:Events:
		on_component_changed: is called every time when one of the component's
		properties has just been changed
		on_relative_value: is called when relative value set to the component's properties
	"""

	rotation = ConstrainedProperty(RelativeRotation)

	pos_x = ConstrainedProperty(PositionConstraint)
	pos_y = ConstrainedProperty(PositionConstraint)

	# origin_x and origin_y set position of origin that object's Shape will be translated to
	# default value for both is 0 that means upper left corner of the border box of the Shape component,
	# 1 1 means lower right corner
	origin_x = ConstrainedProperty(PositionConstraint)
	origin_y = ConstrainedProperty(PositionConstraint)

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.register_event("on_relative_value")

		self.actual_rotation = None
		self.actual_pos_x = None
		self.actual_pos_y = None

		self.actual_origin_x = None
		self.actual_origin_y = None

	def move(self, x: Optional[Union[int, float]], y: Optional[Union[int, float]]) -> None:
		is_x_rel = self.is_relative_value(self.pos_x)
		is_y_rel = self.is_relative_value(self.pos_y)

		if x is not None and not is_x_rel:
			self.pos_x = self.pos_x + x
		elif x is not None and is_x_rel:
			raise ValueError("Can't move relative value x, in {}".format(self))

		if y is not None and not is_y_rel:
			self.pos_y = self.pos_y + y
		elif y is not None and is_y_rel:
			raise ValueError("Can't move relative value y, in {}".format(self))

	def rotate(self, angle: float) -> None:
		if self.is_relative_value(self.rotation):
			raise ValueError("Can't rotate relative value, in {}".format(self))
		self.rotation += angle

	@property
	def position(self) -> Optional[Vector2d]:
		"""Check whether the actual position components values are calculated
		and return an position vector. If at least one of components
		isn't calculated than None value will be returned"""

		if self.actual_pos_x is None or self.actual_pos_y is None:
			return None

		return Vector2d(self.pos_x, self.pos_y)

	def is_relative_value(self, value) -> bool:
		"""Determines whether a value of int, float or constraint type

		:return bool: true if a value of constraint type, not absolute"""
		return type(value) not in (float, int)

	# Handlers

	def _property_changed_handler(self, sender, event_args: PropertyChangedEventArgs):
		self.dispatch_event("on_component_changed", event_args)

		if self.is_relative_value(event_args.new_value):
			self.dispatch_event("on_relative_value", event_args)

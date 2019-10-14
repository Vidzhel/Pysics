from abc import ABC, abstractmethod
from typing import Union

from core.objects.game_object import GameObject
from core.objects.objects import Object

CT_TRANSFORM = "Transform"
CT_RIGID_BODY = "RigidBody"
CT_CIRCLE_COLLIDER = "CircleCollider"

COMPONENT_TYPES = Union[CT_TRANSFORM, CT_RIGID_BODY]


class BaseComponent(ABC, Object):
	"""Base component for everything that could be attached to attached_obj"""

	def __init__(self, name: str, component_type: str, attached_obj: GameObject):
		super(BaseComponent, self).__init__(name)

		self.component_type = component_type
		self.attached_obj = attached_obj
		self.enabled = True

	def enable_component(self) -> None:
		self.enabled = True

	def disable_component(self) -> None:
		self.enabled = False

	def switch_component(self) -> None:
		if self.enabled:
			self.enabled = False
		else:
			self.enabled = True

	@abstractmethod
	def update_component(self, delta_time):
		pass

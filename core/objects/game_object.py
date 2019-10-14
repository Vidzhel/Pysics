from typing import Set, List

from .object import Object
from logger.loggers import LoggingSystem as Logger
from .object_components.base_component import COMPONENT_TYPES
from .object_components.transform import Transform

class GameObject(Object):
	"""Represent en object to which we can attach components to extend
	 functionality"""

	childes = set()
	transform: Transform = None

	def __init__(self, name: str, tag: str):

		super().__init__(name)

		self.component_id = 0
		self.transform = Transform("Transform", self)
		self.components: Set[COMPONENT_TYPES] = set()

	def add_component(self, component: COMPONENT_TYPES) -> None:
		component.id = self.component_id
		self.components.add(component)
		self.component_id += 1

	@Logger.decorator_info()
	def get_component(self, component_name: str) -> COMPONENT_TYPES:
		for component in self.components:
			if component.name == component_name:
				return component

		raise Exception("The component with the name {} doesn't exist".format(component_name))

	@Logger.decorator_info()
	def try_get_component(self, component_name: str) -> COMPONENT_TYPES:
		for component in self.components:
			if component.name == component_name:
				return component

	def update(self, delta_time: float) -> None:
		pass

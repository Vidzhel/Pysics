from inspect import getmro
from typing import Set, List, Optional, Dict

from events.event_arguments import ComponentsChanged
from logger.loggers import LoggingSystem as Logger
from .object import Object
from .object_components.base_component import BaseComponent
from .object_components.transform import Transform


class Entity(Object):
	"""Represent en object to which we can attach components to extend
	 functionality

	 :Events:
	    on_component_added: occurs when new component added
	    on_component_removed: occurs when a component removed
	 """

	__entities_storage: Dict[str, List["Entity"]] = dict()
	__events__ = ["on_component_added", "on_component_removed"]

	def __init__(self, name: str, tag: str):
		"""
		:param tag: the same tag can be set to multiple objects and then easily get the group of objects
		"""
		super().__init__()

		self.tag = tag

		self.components: Set[BaseComponent] = set()
		self.parent: Optional["Entity"] = None

		self.add_component(Transform())
		self._register_entity()

	def add_component(self, component: BaseComponent) -> None:
		if self.is_component(component):
			error = "Component of the same type already exists"
			Logger.log_error(error)
			raise AttributeError(error)

		component.attached_obj = self
		self.components.add(component)
		self.dispatch_event("on_component_added", ComponentsChanged(component))

	def remove_component(self, component: BaseComponent) -> None:
		if component.attached_obj is not self:
			error = "The component {} is not a component of the {}".format(component, self)
			Logger.log_error(error)
			raise AttributeError(error)

		self.components.remove(component)
		component.attached_obj = None
		self.dispatch_event("on_component_removed", ComponentsChanged(component))

	def is_component(self, component: BaseComponent) -> bool:
		classes_to_check: tuple = getmro(component.__class__)

		for comp in self.components:
			for base in classes_to_check:
				if base in (type(object), type(BaseComponent)):
					continue
				if base in getmro(comp):
					return True

		return False

	def _register_entity(self) -> None:
		entities = self.__entities_storage.get(self.tag, None)

		if entities is None:
			self.__entities_storage[self.tag] = entities = list()

		entities.append(self)

	def __delete__(self, instance) -> None:
		entities = self.__entities_storage[self.tag]
		entities.remove(self)

	def get_objects_by_tag(self, tag: str) -> List["Entity"]:
		return self.__entities_storage.get(tag, [])

	def get_component_by_type(self, component_type: type) -> BaseComponent:
		for component in self.components:
			if type(component) is component_type:
				return component

	@Logger.decorator_info()
	def get_component(self, component_name: str) -> BaseComponent:
		for component in self.components:
			if component.__class__.__name__ == component_name:
				return component

		raise Exception("The component with the name {} doesn't exist".format(component_name))

	def try_get_component(self, component_name: str) -> Optional[BaseComponent]:
		for component in self.components:
			if component.__class__.__name__ == component_name:
				return component

	def __str__(self):
		res = "{}:{}\n(".format(type(self).__name__, self.name)

		return res

	def __repr__(self):
		res = "{space}{}:{}\n(".format(type(self), self.name, space="{space}")

		for component in self.components:
			res += "{}\n".format(component)
		res += ")"

		return res

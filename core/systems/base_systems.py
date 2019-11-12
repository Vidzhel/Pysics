from typing import TYPE_CHECKING, List, Dict, Any

from core.objects.entity import Entity

if TYPE_CHECKING:
	from core.objects.object_components.base_component import BaseComponent
	from events.event_arguments import ComponentsChanged, PropertyChangedEventArgs


class SystemMeta(type):

	def __new__(mcs, classname: str, superclasses: tuple, attributedict: dict, *args, **kwargs):
		if classname not in ("BaseSystem", "GlobalSystem", "System"):
			singleton = attributedict.get("_singleton", None)
			if singleton is None:
				singleton = super(SystemMeta, mcs).__new__(mcs, classname, superclasses, attributedict)
				singleton._singleton = singleton
		else:
			singleton = super(SystemMeta, mcs).__new__(mcs, classname, superclasses, attributedict)

		return singleton


class BaseSystem(metaclass=SystemMeta):
	__required_components = []

	def __new__(cls):
		if hasattr(cls, '_singleton'):
			return cls._singleton

		return super().__new__(cls)

	def check_required_components(self, entity: "Entity") -> bool:
		"""
		:param entity: object to check
		:return bool: true if the object has got all required components
		"""

		for req_component in self.__required_components:
			if not entity.has_component(req_component):
				return False

		return True

	def is_required_component(self, component: "BaseComponent"):
		""":return bool: true if the a component is the one of required components of the system"""
		return component in self.__required_components

	def run(self):
		raise NotImplementedError("Should be implemented in derivative classes")


class GlobalSystem(BaseSystem):
	"""Base class for systems that update whole objects tree"""

	def __init__(self, root: "Entity"):
		"""
		:param root: root object
		"""
		self.root = root


class System(BaseSystem):
	"""Base class for systems that update objects only if they have required components

	Every time when an entity adds new component the system will be check
	the objects components and if required components  than adds to objects list
	"""

	def __init__(self):
		Entity.pre_bound_callback(on_component_added=self._on_component_added_handler)
		Entity.pre_bound_callback(on_component_removed=self._on_component_removed_handler)
		self._process_queue_storage: Dict[Any, List["Entity"]] = {}

	def has_object(self, entity: "Entity") -> bool:
		""":return bool: true if the object has already been in the component objects list"""
		return entity in self._process_queue_storage

	def _on_component_added_handler(self, sender: "Entity", event_args: "ComponentsChanged"):
		if self.has_object(sender) or not self.is_required_component(event_args.changed_component):
			return

		if self.check_required_components(sender):
			self.add_entity_to_queue(sender)

	def add_entity_to_queue(self, entity: "Entity"):
		entity.bind_event_callback(depth=self._on_entity_depth_changed_handler)
		depth = entity.depth
		level = self._process_queue_storage.get(depth, None)

		if level is None:
			level = self._process_queue_storage[depth] = []

		level.append(entity)

	def _on_entity_depth_changed_handler(self, sender: "Entity", event_args: "PropertyChangedEventArgs"):
		"""Moves the entity to an other level in process queue storage"""
		self._process_queue_storage[event_args.old_value].remove(sender)
		self._process_queue_storage[event_args.new_value].append(sender)

	def _on_component_removed_handler(self, sender: "Entity", event_args: "ComponentsChanged"):
		if not self.has_object(sender) or not self.is_required_component(event_args.changed_component):
			return

		self.remove_entity_from_queue(sender)

	def remove_entity_from_queue(self, entity):
		self._process_queue_storage[entity.depth].remove(entity)
		entity.unbind_event_callback(depth=self._on_entity_depth_changed_handler)


class SystemBehaviour:
	"""Adds update method that will be called every frame"""

	def update(self, delta_time):
		NotImplementedError("Should be implemented in derivative class")

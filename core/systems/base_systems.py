from abc import ABC

from core.objects.entity import Entity


class BaseGlobalSystem(ABC):
	"""Base class for systems that update whole objects tree"""

	def __init__(self):
		pass

	def update(self):
		pass


class BaseSystem(ABC):
	"""Base class for systems that update objects only if they have required components

	Every time when an entity adds new component the system will be check
	the objects components and if required components  than adds to objects list
	"""
	__required_components = set()

	def __init__(self):
		Entity.pre_bound_callback(on_component_added=self.on_component_added_handler)
		self._objects = set()

	def check_required_components(self, entity: Entity):
		pass

	def on_component_added_handler(self, sender, event_args):
		pass

	def update(self):
		pass

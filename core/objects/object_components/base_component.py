from typing import Optional, TYPE_CHECKING

from core.objects.object import Object
from core.objects.properties.property import Property

if TYPE_CHECKING:
	from core.objects.entity import Entity


class BaseComponent(Object):
	"""Base component for everything that could be attached to attached_obj

	:Events:
		on_component_changed: is called every time when one of the component's
		properties has just been changed
	"""

	__events__ = ["on_component_changed"]

	def __init__(self, **kwargs) -> None:
		super(BaseComponent, self).__init__(**kwargs)

		# add property changed handler to all properties
		properties = [attr for attr in dir(self) if isinstance(attr, Property)]
		for prop in properties:
			prop.bind_callback(self._property_changed_handler)

		self.attached_obj: Optional["Entity"] = None

	def _property_changed_handler(self, sender, event_args):
		pass

	def __str__(self):
		return "{}: attached object: {}".format(self.__class__.__name__, self.attached_obj)

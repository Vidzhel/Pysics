from core.objects.properties.property import BoolProperty
from events.events_dispatcher import EventDispatcher


class Object(EventDispatcher):
	enabled = BoolProperty()

	def __init__(self, **kwargs) -> None:
		super(Object, self).__init__(**kwargs)

	def switch(self):
		self.enabled = not self.enabled

	def __eq__(self, other: "Object") -> bool:
		if other is self:
			return True

		return False

	def __str__(self):
		return "{}".format(type(self))

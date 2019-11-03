from enum import Enum, auto


class EventType(Enum):
	PropertyEvent = auto()
	CustomEvent = auto()
	EntityEvent = auto()
	ComponentEvent = auto()


class EventArguments:
	"""Base class for event arguments

	Event dispatcher passes the class as argument
	to a callback function when a particular event occurs"""

	def __init__(self):
		self.event_type = None
		self.event_name = None

	def __str__(self):
		return "{}: type= {}, name= {}".format(self.__class__.__name__, self.event_type,
		                                       self.event_name)


class PropertyChangedEventArgs(EventArguments):

	def __init__(self, new_value):
		super(PropertyChangedEventArgs, self).__init__()
		self.event_type = EventType.PropertyEvent
		self.new_value = new_value

	def __str__(self):
		return "{}, new_value= {}".format(super(PropertyChangedEventArgs, self).__str__(), self.new_value)


class ComponentsChanged(EventArguments):

	def __init__(self, changed_component):
		super(ComponentsChanged, self).__init__()
		self.event_type = EventType.EntityEvent
		self.changed_component = changed_component

	def __str__(self):
		return "{}, changed_component= {}".format(super(ComponentsChanged, self).__str__(),
		                                          self.changed_component)

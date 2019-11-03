from inspect import getmro, getfullargspec
from typing import Dict, TYPE_CHECKING, Callable, Optional, Set

from core.objects.properties.property import Property
from events.event_arguments import EventType
from events.event_storage import EventStorage

if TYPE_CHECKING:
	from events.event_arguments import EventArguments
	from core.objects.properties.property_storage import PropertyStorage


class EventDispatcher:
	"""Class that manages events

	Store all necessary data for properties as well as custom events
	that can be crated in derivative classes

	In order to register new event in derivative class you need to
	create "__events__" tuple in the class space and specify all
	available event names. Event name should starts with "on_"

	To bind callback function to an event or property you need to use bind_callback
	like that:

		class MyClass(EventDispatcher):
			__events__ = ("on_action", "on_another_action")

			def action(self)
				self.dispatch_event("on_action", EventArguments())

		def callback(sender, event_args):
			print("On action event raised, sender {}, event_args {}"
				   .format(sender, event_args))

		a = MyClass()

		a.bind_event_callback(on_action=callback, [other events callbacks])

	Use pre_bound_callback function to specify callbacks that will be set to each
	instance of a class. NOTICE it works only with class events aka __events__

		class MyClass(EventDispatcher):
				__events__ = ("on_action", "on_another_action")

				def action(self)
					self.dispatch_event("on_action", EventArguments())

		def callback(sender, event_args):
				print("On action event raised, sender {}, event_args {}"
					   .format(sender, event_args))

		MyClass.pre_bound_callback(on_action=callback)

		a = MyClass()
		a.action()

		'>>> On action event raised, sender {}, event_args {}'

	"""
	__events__ = []
	__cached_properties = {}
	__cached_events = {}
	__pre_bound_callbacks = {}

	def __init__(self, **kwargs) -> None:
		self._props_storage: Dict[str, "PropertyStorage"] = dict()
		self._events_storage: Dict[str, EventStorage] = dict()
		__cls__ = self.__class__

		# Get all properties in the class
		properties = self.get_properties()

		# Link all properties
		for prop_name in properties:
			prop = properties[prop_name]
			prop.link_dispatcher(self, prop_name)

		# Find and set values to properties
		prop_values = {prop_name: kwargs.pop(prop_name) for prop_name in list(kwargs)
		               if prop_name in properties}
		for prop_name, values in prop_values.items():
			# Check if it's a tuple to set multiple attributes to a property
			try:
				_ = iter(values)
			except TypeError:
				values = (values,)

			for val in values:
				if callable(val):
					properties[prop_name].bind_callback(val)
				else:
					setattr(self, prop_name, val)

		events = self.__events__

		# Find and set callbacks for events, properties
		event_callbacks = {event_name: kwargs.pop(event_name) for event_name in list(kwargs)
		                   if event_name in events}

		self.bind_event_callback(**event_callbacks)

		# Find and set pre-bound events
		event_callbacks = {event_name: self.__pre_bound_callbacks[event_name] for event_name in
		                   list(self.__pre_bound_callbacks) if event_name in events}

		self.bind_event_callback(**event_callbacks)

	@classmethod
	def pre_bound_callback(cls, **kwargs):
		"""Adds callbacks that will be bound to each instance of the class. Notice it works only with class
		events"""

		for key, value in kwargs.items():
			cls.__pre_bound_callbacks[key] = value

	def bind_event_callback(self, **kwargs):
		"""Bind new callback to an property or custom event

		Callable should take two arg: sender object and event args
		You can't bound one callable multiple times"""

		for name, callback in kwargs.items():
			if not callable(callback):
				raise Exception("Expected callable, but got {} in {}, target {}"
				                .format(type(callback), self, name))

			if len(getfullargspec(callback).args) < 2 and not getfullargspec(callback).varargs:
				raise Exception("Given callback doesn't match required signature,"
				                "expected (sender, event_args), got {}, in {}, target {}"
				                .format(getfullargspec(callback), self, name))

			# Set callback for event
			if name[:3] == "on_" and name in self.__events__:
				event_storage = self._events_storage.get(name, None)

				if not event_storage:
					self._events_storage[name] = event_storage = EventStorage()
				event_storage.add_callback(callback)
			else:
				prop = self.get_properties()
				if name in prop:
					prop[name].bind_callback(callback)
				else:
					raise Exception("Didn't find any property or event with the given name {}, in {}"
					                .format(name, self))

	def unbind_event_callback(self, **kwargs):
		for name, callback in kwargs.items():

			if name[:3] == "on_" and name in self.__events__:
				event_storage = self._events_storage.get(name, None)

				if not event_storage:
					continue
				event_storage.remove_callback(callback)
			else:
				prop = self.get_properties()
				if name in prop:
					prop[name].unbind_callback(callback)
				else:
					raise Exception("Didn't find any property or event with the given name {}, in {}"
					                .format(name, self))

	@classmethod
	def register_event(cls, event_name: str):
		"""Register new event with given name in the instance of a class"""

		if event_name[:3] != "on_":
			raise Exception("Event name should start with 'on_', get {}, in {}".format(event_name, cls))

		if event_name in cls.__events__:
			raise Exception("Event with the name {} in {}".format(event_name, cls))

		cls.__events__.append(event_name)

	def unregister_event(self, event_name):
		"""Unregister event with a given name in the instance of a class

		Deletes event and related callbacks"""

		if event_name not in self.__events__:
			raise Exception("Event with the name {} doesn't exist in {}".format(event_name, self))

		self.__events__.remove(event_name)

		try:
			del self._events_storage[event_name]
		except KeyError:
			pass

	def dispatch_event(self, event_name: str, event_args: "EventArguments"):
		event_args.event_name = event_name

		try:

			if event_name[:3] == "on_":
				event_args.event_type = EventType.CustomEvent
				self._events_storage[event_name].dispatch(self, event_args)
			else:
				event_args.event_type = EventType.PropertyEvent
				self._props_storage[event_name].dispatch(self, event_args)

		except KeyError:
			pass

	def get_properties(self) -> Dict[str, Property]:
		"""Gets dictionary with all properties in the class

		Returns the dictionary with property name as key
		and property itself as value
		"""

		found_properties: Dict[str, Property] = dict()
		__cls__ = self.__class__
		if __cls__ not in self.__cached_properties:

			for attr_name in dir(__cls__):
				attr = getattr(__cls__, attr_name, None)

				if not isinstance(attr, Property):
					continue

				found_properties[attr_name] = attr

			self.__cached_properties[__cls__] = found_properties
		else:
			found_properties = self.__cached_properties[__cls__]

		return found_properties

	def get_observers(self, name: str) -> Optional[Set[Callable]]:
		if name[:3] == "on_":
			event_storage = self._events_storage.get(name, None)

			if event_storage:
				return event_storage.callbacks
			return None
		else:
			prop_storage = self._props_storage.get(name, None)

			if prop_storage:
				return

	def _cache_events(self) -> None:
		"""Gets event, checks its name, caches it"""

		__cls__ = self.__class__
		if __cls__ not in self.__cached_events:
			classes_to_discover = getmro(__cls__)
			events = []

			for cls in classes_to_discover:
				if not hasattr(cls, "__events__"):
					continue

				for event in cls.__events__:
					if event in events:
						continue

					if event[:3] != "on_":
						raise Exception("Wrong event name {} in {}, should starts with 'on_'".
						                format(event, __cls__.__name__))

					events.append(event)

			self.__cached_events[__cls__] = events

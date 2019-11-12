from typing import Optional, Callable, Any, Union, TYPE_CHECKING, List

from core.objects.constraints.constraint import BaseConstraint
from core.objects.properties.property_storage import PropertyStorage
from events.event_arguments import EventArguments, PropertyChangedEventArgs

if TYPE_CHECKING:
	from events.events_dispatcher import EventDispatcher


class Property:

	def __init__(self, default_value: Any, dispatch_on_duplication: bool = False,
	             comparator: Optional[Callable[[Optional[Any], Any, Any], bool]] = None,
	             allowed_types: Optional[List[type]] = None,
	             error_value: Any = None,
	             error_handler: Optional[Callable[[Optional[Any], Any], Any]] = None,
	             allow_none: bool = False):
		"""
		:param default_value: a value that will be set after __init__
		:param dispatch_on_duplication: if event will be dispatched when
		:param comparator: takes two values (old one and new one) and return true if they the same
		:param allowed_types: a list of allowed types for this property
		:param error_value: a value that will be set if the given value isn't proper
		:param error_handler: will be called when given value isn't proper and error_value isn't set
		:param allow_none: allows None value
		"""
		self.dispatcher: Optional["EventDispatcher"] = None
		self._name: Optional[str] = None

		self.allow_none = allow_none
		self.error_value = error_value
		self.default_value = default_value
		self.dispatch_on_duplication = dispatch_on_duplication

		# Set empty list if allowed types aren't specified
		self.allowed_types = [] if not allowed_types else allowed_types

		if comparator is not None and not callable(comparator):
			raise AttributeError("Comparator should be callable, {}".format(self))

		if error_handler is not None and not callable(error_handler):
			raise AttributeError("Error handler should be callable, {}".format(self))

		self.comparator = comparator
		self.error_handler = error_handler

	@property
	def name(self):
		return self._name

	def link_dispatcher(self, dispatcher: "EventDispatcher", property_name: str) -> None:
		self.dispatcher = dispatcher
		self._name = property_name
		self.init_storage(dispatcher, property_name)

	def init_storage(self, dispatcher: "EventDispatcher", property_name: str) -> None:
		prop_storage = PropertyStorage()
		prop_storage.value = self.default_value
		dispatcher._props_storage[property_name] = prop_storage

	def unlink_dispatcher(self):
		if not self.dispatcher:
			raise Exception("Can't unlink already unlinked property, {}"
			                .format(self))

		del self.dispatcher._props_storage[self.name]

	def bind_callback(self, callback):
		prop_storage = self._get_prop_storage()
		prop_storage.add_callback(callback)

	def unbind_callback(self, callback):
		prop_storage = self._get_prop_storage()
		prop_storage.remove_callback(callback)

	def _get_prop_storage(self) -> "PropertyStorage":
		if not self.dispatcher:
			raise Exception("Can't get property storage of unlinked property, {}"
			                .format(self))

		try:
			return self.dispatcher._props_storage[self.name]
		except KeyError:
			raise Exception("Can't get property storage, {}, dispatcher {}"
			                .format(self, self.dispatcher))

	def __get__(self, dispatcher_instance, owner) -> Any:
		if dispatcher_instance is None:
			return self

		prop_storage = self._get_prop_storage()
		return prop_storage.value

	def __set__(self, instance, value):
		prop_storage = self._get_prop_storage()
		old_value = self.convert(prop_storage.value)

		same_value = self.compare_values(old_value, value)
		if same_value and not self.dispatch_on_duplication:
			return

		try:
			self.check_value(value)
		except ValueError as e:
			if self.error_value is not None:
				self.check_value(self.error_value)
				value = self.error_value
			elif self.error_handler is not None:
				value = self.error_handler(value)
				self.check_value(value)
			else:
				raise e

		prop_storage.value = value
		self.dispatch(PropertyChangedEventArgs(old_value, value))

	def dispatch(self, event_args: EventArguments):
		event_args.event_name = self.name
		prop_storage = self._get_prop_storage()
		prop_storage.dispatch(self, event_args)

	def check_value(self, value) -> None:
		"""
		:raise ValueError: if encounter wrong value
		:param value: value to check
		"""

		if value is None and not self.allow_none:
			raise ValueError("None values disallowed in the property, {}, dispatcher {}"
			                 .format(self, self.dispatch_on_duplication))
		else:
			# Check if a value of allowed type
			if issubclass(value, type):
				if value not in self.allowed_types:
					raise ValueError("type {}, is not allowed in the property {}".format(value, self))

			else:
				if type(value) not in self.allowed_types:
					raise ValueError("type {}, is not allowed in the property {}".format(type(value), self))

	def compare_values(self, old: Any, new: Any) -> bool:
		""":return: return true if values match"""

		if self.comparator is not None:
			return self.comparator(old, new)
		else:
			return old == new

	def convert(self, value):
		return value

	def __str__(self):
		return "<{} name={}>".format(self.__class__.__name__, self.name)


Numbers = Union[int, float]


class NumericProperty(Property):

	def __init__(self, default_value: Numbers = 0, dispatch_on_duplication: bool = False,
	             comparator: Optional[Callable[[Optional[Any], Numbers, Numbers], bool]] = None,
	             error_value: Numbers = None,
	             error_handler: Optional[Callable[[Optional[Any], Numbers], Numbers]] = None,
	             allow_none: bool = False):
		super(NumericProperty, self).__init__(default_value, dispatch_on_duplication, comparator,
		                                      error_value, error_handler, allow_none)

	def check_value(self, value) -> None:
		super(NumericProperty, self).check_value(value)

		if type(value) not in (int, float, type(None)):
			raise ValueError("The property accept only (int, float) types, got {}, {}, dispatcher {}"
			                 .format(type(value), self, self.dispatcher))


class BoundedNumericProperty(Property):

	def __init__(self, min: Optional[Numbers], max: Optional[Numbers], default_value: Numbers = 0,
	             dispatch_on_duplication: bool = False,
	             comparator: Optional[Callable[[Optional[Any], Numbers, Numbers], bool]] = None,
	             error_value: Numbers = None,
	             error_handler: Optional[Callable[[Optional[Any], Numbers], Numbers]] = None,
	             allow_none: bool = False):
		super(BoundedNumericProperty, self).__init__(default_value, dispatch_on_duplication, comparator,
		                                             error_value, error_handler, allow_none)
		self.min = min
		self.max = max
		self.use_min = type(min) in (int, float)
		self.use_max = type(min) in (int, float)

	def set_bounds(self, min: Optional[Numbers], max: Optional[Numbers]):
		self.min = min
		self.max = max
		self.use_min = type(min) in (int, float)
		self.use_max = type(min) in (int, float)

	def check_value(self, value) -> None:
		super(BoundedNumericProperty, self).check_value(value)

		if type(value) not in (int, float, type(None)):
			raise ValueError("The property accept only (int, float) types, got {}, {}, dispatcher {}"
			                 .format(type(value), self, self.dispatcher))

		if self.min is not None and value < self.min:
			raise ValueError("Value below the minimum bound {}, got {}".format(self.min, value))
		elif self.max is not None and value > self.max:
			raise ValueError("Value above the maximum bound {}, got {}".format(self.max, value))


class BoolProperty(Property):

	def __init__(self, default_value: bool = False, dispatch_on_duplication: bool = False,
	             comparator: Optional[Callable[[Optional[Any], bool, bool], bool]] = None,
	             error_value: bool = None,
	             error_handler: Optional[Callable[[Optional[Any], bool], bool]] = None,
	             allow_none: bool = False):
		super(BoolProperty, self).__init__(default_value, dispatch_on_duplication, comparator,
		                                   error_value, error_handler, allow_none)

	def check_value(self, value) -> None:
		super(BoolProperty, self).check_value(value)

		if type(value) not in (bool, type(None)):
			raise ValueError("The property accept only (bool) types, got {}, {}, dispatcher {}"
			                 .format(type(value), self, self.dispatcher))


Constrained = Union[int, float, BaseConstraint]


class ConstrainedProperty(Property):

	def __init__(self, constraint_types: List[type], default_value: Any = 0,
	             dispatch_on_duplication: bool = False,
	             comparator: Optional[
		             Callable[[Optional[Any], Constrained, Constrained], Constrained]] = None,
	             error_value: bool = None,
	             error_handler: Optional[Callable[[Optional[Any], Constrained], Constrained]] = None,
	             allow_none: bool = True):
		"""

		:param constraint_types: the type of constraint that will be allowed, other types will be cause an
		exception
		:param default_value: value that will be set after __init__
		:param dispatch_on_duplication: if event will be dispatched when
		:param comparator: takes two values (old one and new one) and return true if they the same
		:param error_value: value that will be set if the given value isn't proper
		:param error_handler: will be called when given value isn't proper and error_value isn't set
		:param allow_none: allow None value
		"""
		constraint_types.append(float)
		constraint_types.append(int)
		constraint_types.append(BaseConstraint)
		super(ConstrainedProperty, self).__init__(default_value, dispatch_on_duplication, comparator,
		                                          constraint_types, error_value, error_handler, allow_none)

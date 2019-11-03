from typing import Callable, TYPE_CHECKING, Any, Set

if TYPE_CHECKING:
	from events.event_arguments import EventArguments


class EventStorage:

	def __init__(self):
		self.callbacks: Set[Callable] = set()

	def add_callback(self, callback: Callable):
		self.callbacks.add(callback)

	def remove_callback(self, callback: Callable):
		try:
			self.callbacks.remove(callback)
		except KeyError:
			return

	def dispatch(self, sender: Any, event_args: "EventArguments"):
		for callback in list(self.callbacks):
			callback(sender, event_args)

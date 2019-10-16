from abc import ABC, abstractmethod
from typing import Callable

from events.base_event import Event


class Window(ABC):

	def __init__(self, width: float, height: float, window_title: str):
		self.width = width
		self.height = height
		self.window_title = window_title
		self.events_callback = None

	def set_on_event_callback(self, callback_function: Callable[[Event], None]):
		self.events_callback = callback_function

	@abstractmethod
	def update(self):
		pass

	@abstractmethod
	def open(self):
		pass

	@abstractmethod
	def shutdown(self):
		pass

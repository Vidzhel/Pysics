from abc import ABC
from typing import Optional
from enum import Enum, auto


class EventType(Enum):
	WindowClosed = auto()
	WindowFolded = auto()
	WindowUnfolded = auto()
	WindowFocused = auto()
	WindowLostFocus = auto()
	WindowMoved = auto()
	WindowResized = auto()

	KeyPressed = auto()
	KeyReleased = auto()
	KeyTaped = auto()

	MouseButtonPressed = auto()
	MouseButtonReleased = auto()
	MouseMoved = auto()
	MouseScrolled = auto()


class EventCategory(Enum):
	ApplicationEvent = auto()
	WindowEvent = auto()
	KeyboardEvent = auto()
	MouseEvent = auto()


class Event(ABC):

	def __init__(self, event_type: EventType, event_category: EventCategory, name: Optional[str] = None):

		self.handled = False

		if not name:
			self.name = name
		else:
			self.name = event_type

		self.event_type = event_type
		self.event_category = event_category

	def handle(self) -> None:
		self.handled = True

	def is_in_category(self, category: EventCategory):
		if self.event_category == category:
			return True

		return False

	def __str__(self):
		return "[Event] {}:{}:{}".format(self.event_category, self.event_type, self.name)

from typing import Optional

from core.math.vector2d import Vector2d
from .base_event import Event, EventCategory, EventType


class MouseMovedEvent(Event):

	def __init__(self, position: Vector2d):
		super(MouseMovedEvent, self).__init__(EventType.MouseMoved, EventCategory.MouseEvent,
		                                      EventType.MouseMoved.name)

		self.position = position

	def __str__(self):
		return "[Event] {}:{} mouse moved to {}".format(self.event_category, self.event_type, self.position)


class MouseScrolledEvent(Event):

	def __init__(self, offset: Vector2d):
		super(MouseScrolledEvent, self).__init__(EventType.MouseScrolled, EventCategory.MouseEvent,
		                                         EventType.MouseScrolled.name)

		self.offset = offset

	def __str__(self):
		return "[Event] {}:{} mouse scrolled {}".format(self.event_category, self.event_type, self.offset)


class MouseKeyEvent(Event):

	def __init__(self, button: int, event_type: EventType):
		super(MouseKeyEvent, self).__init__(event_type, EventCategory.MouseEvent, event_type.name)

		self.button = button

	def __str__(self):
		return "[Event] {}:{} mouse button {}".format(self.event_category, self.event_type, self.button)


class MousePressedEvent(MouseKeyEvent):

	def __init__(self, button: int):
		super(MousePressedEvent, self).__init__(button, EventType.MouseButtonPressed)

	def __str__(self):
		return "[Event] {}:{} mouse button pressed {}".format(self.event_category, self.event_type,
		                                                      self.button)


class MouseReleasedEvent(MouseKeyEvent):

	def __init__(self, button: int):
		super(MouseReleasedEvent, self).__init__(button, EventType.MouseButtonReleased)

	def __str__(self):
		return "[Event] {}:{} mouse button released {}".format(self.event_category, self.event_type,
		                                                       self.button)

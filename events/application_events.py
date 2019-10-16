from core.math.vector2d import Vector2d
from .base_event import Event, EventCategory, EventType


class WindowResized(Event):

	def __init__(self, size: Vector2d):
		super(WindowResized, self).__init__(EventType.WindowResized, EventCategory.WindowEvent)

		self.size = size

	def __str__(self):
		return "[Event] {}:{} new window size {}".format(self.event_category, self.event_type, self.size)


class WindowFolded(Event):

	def __init__(self):
		super(WindowFolded, self).__init__(EventType.WindowFolded, EventCategory.WindowEvent)

	def __str__(self):
		return "[Event] {}:{} window folded".format(self.event_category, self.event_type)


class WindowUnfolded(Event):

	def __init__(self):
		super(WindowUnfolded, self).__init__(EventType.WindowUnfolded, EventCategory.WindowEvent)

	def __str__(self):
		return "[Event] {}:{} window unfolded".format(self.event_category, self.event_type)


class WindowFocused(Event):

	def __init__(self):
		super(WindowFocused, self).__init__(EventType.WindowFocused, EventCategory.WindowEvent)

	def __str__(self):
		return "[Event] {}:{} window focused".format(self.event_category, self.event_type)


class WindowLostFocus(Event):

	def __init__(self):
		super(WindowLostFocus, self).__init__(EventType.WindowLostFocus, EventCategory.WindowEvent)

	def __str__(self):
		return "[Event] {}:{} window lost focus".format(self.event_category, self.event_type)


class WindowMoved(Event):

	def __init__(self, position: Vector2d):
		super(WindowMoved, self).__init__(EventType.WindowMoved, EventCategory.WindowEvent)

		self.position = position

	def __str__(self):
		return "[Event] {}:{} window moved to".format(self.event_category, self.event_type, self.position)


class WindowClosed(Event):

	def __init__(self):
		super(WindowClosed, self).__init__(EventType.WindowClosed, EventCategory.WindowEvent)

	def __str__(self):
		return "[Event] {}:{} window closed".format(self.event_category, self.event_type)

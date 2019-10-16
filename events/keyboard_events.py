from typing import Optional

from .base_event import Event, EventCategory, EventType


class KeyEvent(Event):

	def __init__(self, key_code: int, event_type: EventType):
		super(KeyEvent, self).__init__(event_type, EventCategory.KeyboardEvent, event_type.name)

		self.key_code = key_code

	def __str__(self):
		return "[Event] {}:{} key code {}".format(self.event_category, self.event_type, self.key_code)


class KeyPressedEvent(KeyEvent):

	def __init__(self, key_code: int, repeated: bool):
		super(KeyPressedEvent, self).__init__(key_code, EventType.KeyPressed)

		self.repeated = repeated

	def __str__(self):
		return "[Event] {}:{} pressed key code {} repeated {}".format(self.event_category, self.event_type,
		                                                              self.key_code, self.repeated)


class KeyReleasedEvent(KeyEvent):

	def __init__(self, key_code: int):
		super(KeyReleasedEvent, self).__init__(key_code, EventType.KeyReleased)

	def __str__(self):
		return "[Event] {}:{} released key code {}".format(self.event_category, self.event_type,
		                                                   self.key_code)


class KeyTypedEvent(KeyEvent):

	def __init__(self, key_code: int):
		super(KeyTypedEvent, self).__init__(key_code, EventType.KeyTaped)

	def __str__(self):
		return "[Event] {}:{} taped key code {}".format(self.event_category, self.event_type,
		                                                self.key_code)

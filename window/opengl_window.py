import glfw

import events.application_events
import events.keyboard_events
import events.mouse_events
from core.math.vector2d import Vector2d
from core.window import Window
from logger.loggers import LoggingSystem as Logger


class OpenGLWindow(Window):

	def __init__(self, width: float, height: float, title: str):

		super(OpenGLWindow, self).__init__(width, height, title)

		self.window = None
		Logger.log_info("Create window width:{} height:{} title:{}".format(width, height, title))

	@Logger.decorator_info("Opening window", "Opened window")
	def open(self):
		if not glfw.init():
			raise Exception("Can't init glfw")

		self.window = glfw.create_window(self.width, self.height, self.window_title, None, None)

		if not self.window:
			glfw.terminate()
			raise Exception("Can't create window")

		glfw.make_context_current(self.window)

		self.set_callbacks()

	def update(self):
		glfw.swap_buffers(self.window)
		glfw.poll_events()

	def shutdown(self):
		glfw.terminate()
		Logger.log_info("Shutdown window")

	def set_callbacks(self):
		glfw.set_window_close_callback(self.window, self.window_close_callback)
		glfw.set_window_size_callback(self.window, self.window_resize_callback)
		glfw.set_key_callback(self.window, self.keyboard_callback)
		glfw.set_char_callback(self.window, self.key_typed_callback)
		glfw.set_mouse_button_callback(self.window, self.mouse_callback)
		glfw.set_scroll_callback(self.window, self.scroll_callback)
		glfw.set_cursor_pos_callback(self.window, self.cursor_pos_callback)

	def window_resize_callback(self, window, width, height):
		self.width = width
		self.height = height

		event = events.application_events.WindowResized(Vector2d(width, height))
		self.events_callback(event)

	def window_close_callback(self, window):
		event = events.application_events.WindowClosed()
		self.events_callback(event)
		self.shutdown()

	def keyboard_callback(self, window, key_code, scan_code, action, mods):

		if action == glfw.PRESS:
			event = events.keyboard_events.KeyPressedEvent(key_code, False)
			self.events_callback(event)

		elif action == glfw.RELEASE:
			event = events.keyboard_events.KeyReleasedEvent(key_code)
			self.events_callback(event)

		elif action == glfw.REPEAT:
			event = events.keyboard_events.KeyPressedEvent(key_code, True)
			self.events_callback(event)

	def key_typed_callback(self, window, key_code):
		event = events.keyboard_events.KeyTypedEvent(key_code)
		self.events_callback(event)

	def mouse_callback(self, window, button, action, mods):

		if action == glfw.PRESS:
			event = events.mouse_events.MousePressedEvent(button)
			self.events_callback(event)

		elif action == glfw.RELEASE:
			event = events.mouse_events.MouseReleasedEvent(button)
			self.events_callback(event)

	def scroll_callback(self, window, x_offset, y_offset):
		event = events.mouse_events.MouseScrolledEvent(Vector2d(x_offset, y_offset))
		self.events_callback(event)

	def cursor_pos_callback(self, window, x_pos, y_pos):
		event = events.mouse_events.MouseMovedEvent(Vector2d(x_pos, y_pos))
		self.events_callback(event)

	def error_callback(self, error_id, description):
		Logger.log_error("[GLFW] Error id:{}:{}", format(error_id, description))

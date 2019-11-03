from core.math.vector2d import Vector2d
from logger.loggers import LoggingSystem as Logger
from .base_layout import Layout


class Canvas(Layout):

	def __init__(self, width: float, height: float, name: str):
		super(Canvas, self).__init__(name, width, height)

		self.origin = Vector2d(0, 0)

	def set_origin_relative_x(self, x: float):
		if not 0 <= x <= 1:
			error = "Value should be between 0 and 1, got {}".format(x)
			Logger.log_error(error)
			raise AttributeError(error)

		self.origin.x = self.size.width * x

	def set_origin_relative_y(self, y: float):
		if not 0 <= y <= 1:
			error = "Value should be between 0 and 1, got {}".format(y)
			Logger.log_error(error)
			raise AttributeError(error)

		self.origin.y = self.size.height * y

	def set_origin_absolute_x(self, x: float):
		if not 0 <= x <= self.size.width:
			error = "Value should be between 0 and 1 {}, got {}".format(self.size.width, x)
			Logger.log_error(error)
			raise AttributeError(error)

		self.origin.x = x

	def set_origin_absolute_y(self, y: float):
		if not 0 <= y <= self.size.width:
			error = "Value should be between 0 and 1 {}, got {}".format(self.size.height, y)
			Logger.log_error(error)
			raise AttributeError(error)

		self.origin.y = y

	def set_origin_absolute(self, origin: Vector2d):
		self.set_origin_absolute_x(origin.x)
		self.set_origin_absolute_y(origin.y)

	def set_origin_relative(self, origin: Vector2d):
		self.set_origin_relative_x(origin.x)
		self.set_origin_relative_y(origin.y)

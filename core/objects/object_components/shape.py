from core.math.geometry.geometry_objects import BaseShape


class Shape:

	def __init__(self, shape: BaseShape):
		self.shape = shape

	def get_border_box(self):
		raise NotImplementedError()

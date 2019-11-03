from core.objects.entity import Entity
from core.objects.object_components.layouts.canvas import Canvas
from logger.loggers import LoggingSystem as Logger


class Scene(Entity):

	def __init__(self, width: float, height: float, name: str, tag: str = "None") -> None:
		"""Creates scene which is used to set environments and objects.

		origin (float): define origin coordinates
			can be seated in percentages using set_origin_percentages function
			starting fr om the left upper corner by default (0, 0)
		"""
		super(Scene, self).__init__(name, tag)

		self.add_component(Canvas(width, height, "Scene"))
		# TODO create camera

		Logger.log_info("New scene has just been created")

	def __repr__(self):
		res = "Scene:{}\n(".format(self.name)

		for component in self.components:
			res += "{}\n".format(component)
		res += ")"
		for child in self.children:
			res += "\n  -{}".format(repr(child).format(space="  "))

		return res

	def __str__(self):
		res = "Scene:{}\n(".format(self.name)

		for child in self.children:
			res += "\n  -{}".format(str(child).format(space="  "))

		return res

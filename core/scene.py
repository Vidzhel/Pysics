from typing import List, Optional

from core.math.vector2d import Vector2d
from logger.loggers import LoggingSystem as Logger
from .objects.object import Object


class Scene(Object):

	def __init__(self, name: str, origin: Vector2d = Vector2d(0.5, 0.5),
	             time_flow_coefficient: float = 1.0) -> None:
		"""Creates scene which is used to set environments and objects.

		origin (float): define origin coordinates
			can be seated in percentages using set_origin_percentages function
			starting from the left upper corner by default (0, 0)
		time_flow_coefficient (float): set the time flow speed multiplier
		force_generators (Optional[List[BaseForceGenerator]]): list of force generators
			that apply forces on objects
		"""
		super(Scene, self).__init__(name)
		self.object_id = 0
		self.is_active = False

		self.origin = origin
		# self.forces_registry: List[BaseForceGenerator] = []
		self.objects_registry = set()

		# if force_generators is not None:
		# 	self.forces_registry.extend(force_generators)

		Logger.log_info("New scene has just been created")

	def add_object(self, object: Object):
		# Set unique id and add to the set
		object.id = self.object_id
		self.objects_registry.add(object)
		self.object_id += 1

	def get_objects_list_by_tag(self, tag: str) -> List["Object"]:
		# Todo make generator
		objects = list()

		for object in self.objects_registry:
			if object.tag == tag:
				objects.append(object)

		return objects

	def get_object_by_tag(self, tag: str) -> "Object":
		for object in self.objects_registry:
			if object.tag == tag:
				return object

	def get_objects_by_name(self, name: str) -> List["Object"]:
		# Todo make generator
		objects = list()

		for object in self.objects_registry:
			if object.name == name:
				objects.append(object)

		return objects

	# def add_force_generator(self, force_generator: BaseForceGenerator) -> None:
	# 	"""Adds force generator to the force registry"""
	# 	self.forces_registry.append(force_generator)

	@Logger.decorator_succeeded(end_message="Scene successfully updated")
	def update(self, delta_time):
		"""Updates every environment and
		apply forces in a scene
		"""

	# self.apply_forces(delta_time)

	# def apply_forces(self, time_since_last_update):
	# 	"""Apply force from each force generator and delete disabled"""
	#
	# 	for force_generator in self.forces_registry:
	#
	# 		if force_generator.is_active():
	# 			force_generator.apply_force(time_since_last_update)
	#
	# 		else:
	# 			del force_generator

	def on_start(self):
		pass

	def on_exit(self):
		pass

	def __str__(self):
		res = "Scene {}:{}".format(self.name, self.id)

		for object in self.objects_registry:
			res += "\n{}".format(str(object))

		return res

	def __eq__(self, other: "Scene") -> bool:
		if self.id == other.id:
			return True

		return False

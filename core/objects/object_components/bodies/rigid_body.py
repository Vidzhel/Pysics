from core.math.vector2d import Vector2d
from core.objects.game_object import GameObject
from core.objects.object_components.base_component import BaseComponent, CT_RIGID_BODY, CT_TRANSFORM

RB_TYPES = ("dynamic", "kinematic", "static")


class RigidBody(BaseComponent):

	def __init__(self, name: str, attached_obj: GameObject,
	             linear_drag: float, mass: float = 1.0, angular_drag: float = 1.0,
	             rb_type: str = "dynamic",
	             velocity: Vector2d = Vector2d(0, 0),
	             force: Vector2d = Vector2d(0, 0)):
		if not rb_type in RB_TYPES:
			raise AttributeError(
				"Rigid body time should be one of the following values {}, but not {}".format(RB_TYPES,
				                                                                              rb_type))
		super().__init__(name, CT_RIGID_BODY, attached_obj)

		self.mass = 1
		self.inverted_mass = 1 / mass

		self.result_force = force
		self.velocity = velocity

		self.linear_drag = linear_drag
		self.angular_drag = angular_drag

		self.simulate = True
		self.type = rb_type

	def add_force(self, force: Vector2d) -> None:
		self.result_force = self.result_force + force

	def add_impulse(self, impulse: Vector2d) -> None:
		pass

	def subtract_force(self, force: Vector2d) -> None:
		self.result_force = self.result_force - force

	def clear_force(self) -> None:
		self.result_force = Vector2d(0, 0)

	def update_component(self, delta_time):
		"""Updated object's data (position, velocity ...)"""

		self.attached_obj.get_component(CT_TRANSFORM).position.add_scaled_vector(self.velocity, delta_time)

		acceleration = self.result_force.scale(self.inverted_mass)
		self.velocity.add_scaled_vector(acceleration, delta_time)

		self.clear_force()

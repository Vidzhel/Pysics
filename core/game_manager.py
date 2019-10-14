import time

from .scene import Scene
from logger.loggers import LoggingSystem as Logger


class GameManager:

	def __init__(self, frame_rate: int):
		"""Represents main object that takes control after scenes and other objects"""

		self.scenes = set()
		self.scene_id = 0

		self.frame_rate = frame_rate
		self.update_time = 1 / frame_rate
		self.time_flow_coeff = 1.0

		self.is_running = False

	def set_screen(self, width: int, height: int, caption: str):
		pass

	def add_scene(self, scene: Scene):
		scene.id = self.scene_id = 0
		self.scenes.add(scene)
		self.scene_id += 1

	def delete_scene(self, scene: Scene) -> None:
		for other_scene in self.scenes:
			if scene == other_scene:
				del other_scene
				return

		raise Exception("The scene with the id {} doesn't exist".format(scene.id))

	@property
	def time_flow_coefficient(self) -> float:
		return self.time_flow_coeff

	@time_flow_coefficient.setter
	def time_flow_coefficient(self, coefficient: float) -> None:
		"""By default it's 1 (without slowdown)"""

		self.time_flow_coeff = coefficient
		self.update_time = 1 / self.frame_rate * coefficient

	def run(self):
		# TODO open screen
		self.is_running = True

		delta_time = 0

		try:
			while self.is_running:

				start = time.time()
				self.update(delta_time)
				end = time.time()

				delta_time = end - start
				time_left = self.update_time - delta_time

				if time_left > 0:
					time.sleep(time_left / 1000)

				self.render()

		except Exception as e:
			Logger.log_error(str(e))
			self.is_running = False

	def update(self, delta_time: float):
		pass

	def render(self):
		pass

	def __str__(self) -> str:

		res = "Scenes list:"

		for scene in self.scenes:
			res += "\n{}".format(str(scene))

		return res

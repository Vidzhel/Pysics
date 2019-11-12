import time
from typing import List

from core.objects.scene import Scene
from events.base_event import Event
from logger.loggers import FileLogger, ConsoleLogger
from logger.loggers import LoggingSystem as Logger
from .window import Window


class Application:

	def __init__(self, frame_rate: int, window: Window):
		"""Represents main object that takes control after scenes and other objects"""

		self.scenes: List[Scene] = []
		self.scene_id = 0

		self.frame_rate = frame_rate
		self.update_time = 1 / frame_rate
		self.time_flow_coeff = 1.0

		self.is_running = False

		self.window = window

		self.init_logging_system()
		self.init_event_system()
		self.init_renderer()

	def init_renderer(self):
		pass

	def init_event_system(self):
		self.window.set_on_event_callback(self.on_event)

	def init_logging_system(self):
		FileLogger.set_default_file("logs.txt")
		# FileLogger.activate()
		ConsoleLogger.activate()
		Logger.activate()

	def on_event(self, event: Event):
		Logger.log_info(str(event))

	def add_scene(self, scene: Scene) -> None:
		scene.id = self.scene_id
		self.scenes.append(scene)
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
		if coefficient < 0:
			Logger.log_error("Time flow coefficient can't be less than zero")
			raise AttributeError("Time flow coefficient can't be less than zero")
		self.time_flow_coeff = coefficient
		self.update_time = 1 / self.frame_rate * coefficient

	@Logger.decorator_info("Run an Application", "Exit an Application")
	def run(self):
		self.window.open()
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

				self.window.update()
				self.render()

		except Exception as e:
			self.stop()
			raise e

	def load_scene(self, scene: Scene) -> None:
		for _scene in self.scenes:
			if scene == _scene:
				_scene.is_active = True
				return

		raise AttributeError("The scene with the id {} doesn't exist in this application".format(scene.id))

	def get_active_scenes(self) -> List[Scene]:
		active_scenes = []

		for scene in self.scenes:
			if scene.is_active:
				active_scenes.append(scene)

		return active_scenes

	def load_next_scene(self) -> None:
		for i in range(len(self.scenes)):
			if self.scenes[i].is_active:
				self.scenes[i].is_active = False
				self.scenes[i + 1].is_active = True

	def stop(self):
		if not self.is_running:
			Logger.log_error("You can't stop disabled engine")
			raise Exception("You can't stop disabled engine")

		self.window.shutdown()

		self.is_running = False
		Logger.log_info("Application has just been stopped")

	def update(self, delta_time: float):
		for scene in self.get_active_scenes():
			scene.update(delta_time)

	def render(self):
		pass

	def __str__(self) -> str:

		res = "Scenes list:"

		for scene in self.scenes:
			res += "\n{}".format(str(scene))

		return res

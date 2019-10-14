from abc import abstractmethod, ABC
from logger.loggers import LoggingSystem as Logger


class Object(ABC):

	def __init__(self, name: str) -> None:
		self.name = name
		self.id = None
		# Todo set scene
		self.tag = None

		self.enabled = True

		Logger.log_info("Object with name {} was created".format(name))

	def disable(self):
		self.enabled = False

	def enable(self):
		self.enabled = True

	def switch(self):
		self.enabled = not self.enabled

	@abstractmethod
	def update(self, delta_time: float) -> None:
		pass

	def __eq__(self, other: "Object") -> bool:
		if other.id == self.id:
			return True

		return False

	def __str__(self):
		return "Object name:{}, id:{}, tag:{}".format(self.name, self.id, self.tag)

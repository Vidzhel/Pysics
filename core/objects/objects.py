from abc import abstractmethod, ABC
from logger.loggers import LoggingSystem as Logger


class Object(ABC):

	def __init__(self, name: str) -> None:
		self.name = name
		self.id = None
		self.scene = None
		# Todo set scene
		self.tag = None

		Logger.log_info("Object with name {} was created".format(name))

	@abstractmethod
	def update_object(self, delta_time: float) -> None:
		pass

	def __eq__(self, other: "Object") -> bool:
		if other.id == self.id:
			return True

		return False

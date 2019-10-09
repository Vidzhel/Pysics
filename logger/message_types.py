import datetime
from abc import ABC
from typing import Union

# Message types
MT_INFO = "INFO"
MT_WARNING = "WARNING"
MT_ERROR = "ERROR"
MT_SUCCEEDED = "SUCCEEDED"

MessageType = Union[MT_INFO, MT_WARNING, MT_ERROR, MT_SUCCEEDED]

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'


class Message(ABC):

	def __init__(self, time: datetime.time, message_type: MessageType, message: str, message_color):
		self.time = time
		self.message_type = message_type
		self.message = message
		self.message_color = message_color

	def get_colored_string(self):
		_str = "{} {:<12} {}".format(self.time.strftime("%H:%M:%S"), "[" + self.message_type + "]",
		                             self.message)

		return self.message_color + " " + _str + " " + ENDC

	def get_string(self):
		_str = "{} [{}] {}".format(self.time.strftime("%H:%M:%S"), self.message_type, self.message)

		return _str

	def __str__(self):
		return self.get_colored_string()

	def __repr__(self):
		return self.get_string()


class InfoMessage(Message):

	def __init__(self, message: str, time: datetime.time = datetime.datetime.now().time()):
		super().__init__(time, MT_INFO, message, OKBLUE)


class WarningMessage(Message):

	def __init__(self, message: str, time: datetime.time = datetime.datetime.now().time()):
		super().__init__(time, MT_WARNING, message, WARNING)


class ErrorMessage(Message):

	def __init__(self, message: str, time: datetime.time = datetime.datetime.now().time()):
		super().__init__(time, MT_ERROR, message, FAIL)


class SucceededMessage(Message):

	def __init__(self, message: str, time: datetime.time = datetime.datetime.now().time()):
		super().__init__(time, MT_SUCCEEDED, message, OKGREEN)

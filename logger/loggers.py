import datetime
from abc import ABC
from typing import Optional, Tuple, List

from .message_types import InfoMessage, WarningMessage, ErrorMessage, SucceededMessage


class Logger(ABC):

	@staticmethod
	def log_info(message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		pass

	@staticmethod
	def log_warning(message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		pass

	@staticmethod
	def log_error(message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		pass

	@staticmethod
	def log_succeeded(message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		pass

	@staticmethod
	def decorator_info(start_mess: Optional[str] = None, end_message: Optional[str] = None):

		def decorator(func):

			def inner(*args, **kwargs):
				if start_mess:
					ConsoleLogger.log_info(start_mess)

				try:
					res = func(*args, **kwargs)
				except Exception as e:
					ConsoleLogger.log_error(str(e.with_traceback))
					raise e

				if end_message:
					ConsoleLogger.log_info(end_message)

				return res

			return inner

		return decorator

	@staticmethod
	def decorator_warning(start_mess: Optional[str] = None, end_message: Optional[str] = None):

		def decorator(func):

			def inner(*args, **kwargs):
				if start_mess:
					ConsoleLogger.log_warning(start_mess)

				try:
					res = func(*args, **kwargs)
				except Exception as e:
					ConsoleLogger.log_error(str(e.with_traceback))
					raise e

				if end_message:
					ConsoleLogger.log_warning(end_message)

				return res

			return inner

		return decorator

	@staticmethod
	def decorator_error(start_mess: Optional[str] = None, end_message: Optional[str] = None):

		def decorator(func):

			def inner(*args, **kwargs):
				if start_mess:
					ConsoleLogger.log_error(start_mess)

				try:
					res = func(*args, **kwargs)
				except Exception as e:
					ConsoleLogger.log_error(str(e.with_traceback))
					raise e

				if end_message:
					ConsoleLogger.log_error(end_message)

				return res

			return inner

		return decorator

	@staticmethod
	def decorator_succeeded(start_mess: Optional[str] = None, end_message: Optional[str] = None):

		def decorator(func):

			def inner(*args, **kwargs):
				if start_mess:
					ConsoleLogger.log_succeeded(start_mess)

				try:
					res = func(*args, **kwargs)
				except Exception as e:
					ConsoleLogger.log_error(str(e.with_traceback))
					raise e

				if end_message:
					ConsoleLogger.log_succeeded(end_message)

				return res

			return inner

		return decorator


class ConsoleLogger(Logger):

	@staticmethod
	def log_info(message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		info = InfoMessage(message, time)

		print(info)

	@staticmethod
	def log_warning(message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		warning = WarningMessage(message, time)

		print(warning)

	@staticmethod
	def log_error(message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		error = ErrorMessage(message, time)

		print(error)

	@staticmethod
	def log_succeeded(message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		succeeded = SucceededMessage(message, time)

		print(succeeded)


class FileLogger(Logger):

	@classmethod
	def set_default_file(cls, default_file_path: str):
		cls.default_file_path = default_file_path

	default_file_path: Optional[str] = None
	files: List[Tuple[str, str]] = []

	@classmethod
	def clear_files(cls):
		cls.default_file_path = None
		cls.files = []

	@classmethod
	def add_log_file(cls, name: str, file_path: str) -> None:
		if cls.is_exist_file(name, file_path):
			raise AttributeError("Log file already {} exist".format(name + ":" + file_path))

		cls.files.append((name, file_path))

	@classmethod
	def is_exist_file(cls, name, file_path):
		for file in cls.files:
			if file[0] == name or file[1] == file_path:
				return True

		return False

	@classmethod
	def get_file_path(cls, name) -> Optional[str]:
		for file in cls.files:
			if file[0] == name:
				return file[1]

	@classmethod
	def print_files(cls):
		if cls.default_file_path:
			print("default:{}".format(cls.default_file_path))

		for file in cls.files:
			print("{}:{}".format(file[0], file[1]))

	@classmethod
	def log_info(cls, message: str, file_path: Optional[str] = None,
	             time: datetime.time = datetime.datetime.now().time()) -> None:
		info = str(InfoMessage(message, time))

		cls.log_to_file(file_path, info)

	@classmethod
	def log_warning(cls, message: str, file_path: Optional[str] = None,
	                time: datetime.time = datetime.datetime.now().time()) -> None:
		warning = str(WarningMessage(message, time))

		cls.log_to_file(file_path, warning)

	@classmethod
	def log_error(cls, message: str, file_path: Optional[str] = None,
	              time: datetime.time = datetime.datetime.now().time()) -> None:
		error = str(ErrorMessage(message, time))

		cls.log_to_file(file_path, error)

	@classmethod
	def log_succeeded(cls, message: str, file_path: Optional[str] = None,
	                  time: datetime.time = datetime.datetime.now().time()) -> None:
		succeeded = str(SucceededMessage(message, time))

		cls.log_to_file(file_path, succeeded)

	@classmethod
	def log_to_file(cls, file_path: Optional[str], data: str):
		if not file_path:
			if not cls.default_file_path:
				raise AttributeError("Specify log file_path or set default")
			else:
				file_path = cls.default_file_path

		with open(file_path, "a+") as file:
			file.write(data + "\n")

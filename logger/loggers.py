import datetime
import sys
import traceback
from abc import ABC
from typing import Optional, Tuple, List

from .message_types import InfoMessage, WarningMessage, ErrorMessage, SucceededMessage


class Logger(ABC):
	is_active = False

	@classmethod
	def activate(cls):
		cls.is_active = True

	@classmethod
	def log_info(cls, message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		raise NotImplemented()

	@classmethod
	def log_warning(cls, message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		raise NotImplemented()

	@classmethod
	def log_error(cls, message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		raise NotImplemented()

	@classmethod
	def log_succeeded(cls, message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		raise NotImplemented()

	@classmethod
	def decorator_info(cls, start_mess: Optional[str] = None, end_message: Optional[str] = None):

		def decorator(func):

			def inner(*args, **kwargs):

				if start_mess and cls.is_active:
					ConsoleLogger.log_info(start_mess)

				try:
					res = func(*args, **kwargs)
				except Exception as e:
					if cls.is_active:
						exc_type, exc_value, exc_tb = sys.exc_info()
						ConsoleLogger.log_error(
							"".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
					raise e

				if end_message and cls.is_active:
					ConsoleLogger.log_info(end_message)

				return res

			return inner

		return decorator

	@classmethod
	def decorator_warning(cls, start_mess: Optional[str] = None, end_message: Optional[str] = None):

		def decorator(func):

			def inner(*args, **kwargs):
				if start_mess and cls.is_active:
					ConsoleLogger.log_warning(start_mess)

				try:
					res = func(*args, **kwargs)
				except Exception as e:
					if cls.is_active:
						exc_type, exc_value, exc_tb = sys.exc_info()
						ConsoleLogger.log_error(
							"".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
					raise e

				if end_message and cls.is_active:
					ConsoleLogger.log_warning(end_message)

				return res

			return inner

		return decorator

	@classmethod
	def decorator_error(cls, start_mess: Optional[str] = None, end_message: Optional[str] = None):

		def decorator(func):

			def inner(*args, **kwargs):
				if start_mess and cls.is_active:
					ConsoleLogger.log_error(start_mess)

				try:
					res = func(*args, **kwargs)
				except Exception as e:
					if cls.is_active:
						exc_type, exc_value, exc_tb = sys.exc_info()
						ConsoleLogger.log_error(
							"".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
					raise e

				if end_message and cls.is_active:
					exc_type, exc_value, exc_tb = sys.exc_info()
					ConsoleLogger.log_error("".join(traceback.format_exception(exc_type, exc_value, exc_tb)))

				return res

			return inner

		return decorator

	@classmethod
	def decorator_succeeded(cls, start_mess: Optional[str] = None, end_message: Optional[str] = None):

		def decorator(func):

			def inner(*args, **kwargs):
				if start_mess and cls.is_active:
					ConsoleLogger.log_succeeded(start_mess)

				try:
					res = func(*args, **kwargs)
				except Exception as e:
					if cls.is_active:
						exc_type, exc_value, exc_tb = sys.exc_info()
						ConsoleLogger.log_error(
							"".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
					raise e

				if end_message and cls.is_active:
					ConsoleLogger.log_succeeded(end_message)

				return res

			return inner

		return decorator


class ConsoleLogger(Logger):
	"""Logs data to a console"""

	@classmethod
	def log_info(cls, message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		if not cls.is_active:
			return

		info = InfoMessage(message, time)

		print(info)

	@classmethod
	def log_warning(cls, message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		if not cls.is_active:
			return

		warning = WarningMessage(message, time)

		print(warning)

	@classmethod
	def log_error(cls, message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		if not cls.is_active:
			return

		error = ErrorMessage(message, time)

		print(error)

	@classmethod
	def log_succeeded(cls, message: str, time: datetime.time = datetime.datetime.now().time()) -> None:
		if not cls.is_active:
			return

		succeeded = SucceededMessage(message, time)

		print(succeeded)


class FileLogger(Logger):
	"""Logs data to a file"""

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
		if not cls.is_active:
			return

		info = str(InfoMessage(message, time))

		cls.log_to_file(file_path, info)

	@classmethod
	def log_warning(cls, message: str, file_path: Optional[str] = None,
	                time: datetime.time = datetime.datetime.now().time()) -> None:
		if not cls.is_active:
			return

		warning = str(WarningMessage(message, time))

		cls.log_to_file(file_path, warning)

	@classmethod
	def log_error(cls, message: str, file_path: Optional[str] = None,
	              time: datetime.time = datetime.datetime.now().time()) -> None:
		if not cls.is_active:
			return

		error = str(ErrorMessage(message, time))

		cls.log_to_file(file_path, error)

	@classmethod
	def log_succeeded(cls, message: str, file_path: Optional[str] = None,
	                  time: datetime.time = datetime.datetime.now().time()) -> None:
		if not cls.is_active:
			return

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


class LoggingSystem(Logger):
	"""Logs data to console and file"""

	@classmethod
	def log_info(cls, message: str, file_path: Optional[str] = None,
	             time: datetime.time = datetime.datetime.now().time()) -> None:
		if not cls.is_active:
			return

		ConsoleLogger.log_info(message, time)
		FileLogger.log_info(message, file_path, time)

	@classmethod
	def log_warning(cls, message: str, file_path: Optional[str] = None,
	                time: datetime.time = datetime.datetime.now().time()) -> None:
		if not cls.is_active:
			return

		ConsoleLogger.log_warning(message, time)
		FileLogger.log_warning(message, file_path, time)

	@classmethod
	def log_error(cls, message: str, file_path: Optional[str] = None,
	              time: datetime.time = datetime.datetime.now().time()) -> None:
		if not cls.is_active:
			return

		ConsoleLogger.log_error(message, time)
		FileLogger.log_error(message, file_path, time)

	@classmethod
	def log_succeeded(cls, message: str, file_path: Optional[str] = None,
	                  time: datetime.time = datetime.datetime.now().time()) -> None:
		if not cls.is_active:
			return

		ConsoleLogger.log_succeeded(message, time)
		FileLogger.log_succeeded(message, file_path, time)

	@classmethod
	def decorator_info(cls, start_mess: Optional[str] = None, end_message: Optional[str] = None):

		def decorator(func):

			def inner(*args, **kwargs):

				if start_mess and cls.is_active:
					ConsoleLogger.log_info(start_mess)
					FileLogger.log_info(start_mess)

				try:
					res = func(*args, **kwargs)
				except Exception as e:
					if cls.is_active:
						exc_type, exc_value, exc_tb = sys.exc_info()
						error = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
						FileLogger.log_error(error)

					raise e

				if end_message and cls.is_active:
					ConsoleLogger.log_info(end_message)
					FileLogger.log_info(end_message)

				return res

			return inner

		return decorator

	@classmethod
	def decorator_warning(cls, start_mess: Optional[str] = None, end_message: Optional[str] = None):

		def decorator(func):

			def inner(*args, **kwargs):
				if start_mess and cls.is_active:
					ConsoleLogger.log_warning(start_mess)
					FileLogger.log_info(start_mess)

				try:
					res = func(*args, **kwargs)
				except Exception as e:
					if cls.is_active:
						exc_type, exc_value, exc_tb = sys.exc_info()
						error = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
						FileLogger.log_error(error)

					raise e

				if end_message and cls.is_active:
					ConsoleLogger.log_info(end_message)
					FileLogger.log_info(end_message)

				return res

			return inner

		return decorator

	@classmethod
	def decorator_error(cls, start_mess: Optional[str] = None, end_message: Optional[str] = None):

		def decorator(func):

			def inner(*args, **kwargs):

				if start_mess and cls.is_active:
					ConsoleLogger.log_info(start_mess)
					FileLogger.log_info(start_mess)

				try:
					res = func(*args, **kwargs)
				except Exception as e:
					if cls.is_active:
						exc_type, exc_value, exc_tb = sys.exc_info()
						error = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
						FileLogger.log_error(error)

					raise e

				if end_message and cls.is_active:
					ConsoleLogger.log_info(end_message)
					FileLogger.log_info(end_message)

				return res

			return inner

		return decorator

	@classmethod
	def decorator_succeeded(cls, start_mess: Optional[str] = None, end_message: Optional[str] = None):

		def decorator(func):

			def inner(*args, **kwargs):

				if start_mess and cls.is_active:
					ConsoleLogger.log_info(start_mess)
					FileLogger.log_info(start_mess)

				try:
					res = func(*args, **kwargs)
				except Exception as e:
					if cls.is_active:
						exc_type, exc_value, exc_tb = sys.exc_info()
						error = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
						FileLogger.log_error(error)

					raise e

				if end_message and cls.is_active:
					ConsoleLogger.log_info(end_message)
					FileLogger.log_info(end_message)

				return res

			return inner

		return decorator

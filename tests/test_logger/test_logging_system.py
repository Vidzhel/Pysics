from logger.loggers import LoggingSystem, FileLogger
import os
import unittest


class TestLoggingSystem(unittest.TestCase):
	# this_folder = r"C:\work\Python\pysics\tests\test_logger"
	this_folder = r""

	def test_log(self):
		FileLogger.set_default_file(self.this_folder + r"default-logger1.txt")
		LoggingSystem.log_info("Info")
		LoggingSystem.log_error("Error")
		LoggingSystem.log_warning("Warning with long text")
		LoggingSystem.log_succeeded("Critical error")

		FileLogger.add_log_file("first", self.this_folder + r"first-logger1.txt")
		file = FileLogger.get_file_path("first")

		LoggingSystem.log_info("Info", file)
		LoggingSystem.log_warning("Warning with long text", file)
		LoggingSystem.log_succeeded("Critical error", file)
		LoggingSystem.log_error("Error", file)
		LoggingSystem.log_warning("Warning with long text", file)
		LoggingSystem.log_succeeded("Critical error", file)

		FileLogger.add_log_file("second", self.this_folder + r"second-logger1.txt")
		file = FileLogger.get_file_path("second")

		LoggingSystem.log_info("Info", file)
		LoggingSystem.log_error("Error", file)
		LoggingSystem.log_warning("Warning with long text", file)
		LoggingSystem.log_warning("Warning with long text", file)
		LoggingSystem.log_succeeded("Critical error", file)
		LoggingSystem.log_succeeded("Critical error", file)

	def test_decorators(self):
		@LoggingSystem.decorator_info("Starting test", "End test")
		def test_decorators1():
			print("method")

		@LoggingSystem.decorator_error("Starting test", "End test")
		def test_decorators2():
			print("method")

		@LoggingSystem.decorator_succeeded("Starting test", "End test")
		def test_decorators3():
			print("method")

		@LoggingSystem.decorator_warning("Starting test", "End test")
		def test_decorators4():
			print("method")

		@LoggingSystem.decorator_info("Starting test", "End test")
		def test_exception1():
			print("method")
			raise Exception("Exception")

		@LoggingSystem.decorator_error("Starting test", "End test")
		def test_exception2():
			print("method")
			raise Exception("Exception")

		@LoggingSystem.decorator_succeeded("Starting test", "End test")
		def test_exception3():
			print("method")
			raise Exception("Exception")

		@LoggingSystem.decorator_warning("Starting test", "End test")
		def test_exception4():
			print("method")
			raise Exception("Exception")

		test_decorators1()
		test_decorators2()
		test_decorators3()
		test_decorators4()
		self.assertRaises(Exception, test_exception1)
		self.assertRaises(Exception, test_exception2)
		self.assertRaises(Exception, test_exception3)
		self.assertRaises(Exception, test_exception4)


if __name__ == '__main__':
	unittest.main()

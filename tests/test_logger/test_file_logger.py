from logger.loggers import FileLogger
import os
import unittest


class TestFileLogger(unittest.TestCase):
	# this_folder = r"C:\work\Python\pysics\tests\test_logger"
	this_folder = r""

	def test_log(self):
		FileLogger.clear_files()

		with self.assertRaises(AttributeError):
			FileLogger.log_warning("Warning with long text")
			FileLogger.log_succeeded("Critical error")

		FileLogger.set_default_file(self.this_folder + r"default-logger.txt")
		FileLogger.log_info("Info")
		FileLogger.log_error("Error")
		FileLogger.log_warning("Warning with long text")
		FileLogger.log_succeeded("Critical error")

		FileLogger.add_log_file("first", self.this_folder + r"first-logger.txt")
		file = FileLogger.get_file_path("first")
		FileLogger.log_info("Info", file)
		FileLogger.log_warning("Warning with long text", file)
		FileLogger.log_succeeded("Critical error", file)
		FileLogger.log_error("Error", file)
		FileLogger.log_warning("Warning with long text", file)
		FileLogger.log_succeeded("Critical error", file)

		FileLogger.add_log_file("second", self.this_folder + r"second-logger.txt")
		file = FileLogger.get_file_path("second")
		FileLogger.log_info("Info", file)
		FileLogger.log_error("Error", file)
		FileLogger.log_warning("Warning with long text", file)
		FileLogger.log_warning("Warning with long text", file)
		FileLogger.log_succeeded("Critical error", file)
		FileLogger.log_succeeded("Critical error", file)

		with self.assertRaises(AttributeError):
			FileLogger.add_log_file("second", self.this_folder + r"second-logger.txt")
			FileLogger.add_log_file("third", self.this_folder + r"second-logger.txt")
			FileLogger.add_log_file("second", self.this_folder + r"third-logger.txt")

	def test_decorators(self):
		FileLogger.clear_files()
		FileLogger.set_default_file(self.this_folder + r"test_decorators.txt")

		@FileLogger.decorator_info("Starting test", "End test")
		def test_decorators1():
			print("method")

		@FileLogger.decorator_error("Starting test", "End test")
		def test_decorators2():
			print("method")

		@FileLogger.decorator_succeeded("Starting test", "End test")
		def test_decorators3():
			print("method")

		@FileLogger.decorator_warning("Starting test", "End test")
		def test_decorators4():
			print("method")

		@FileLogger.decorator_info("Starting test", "End test")
		def test_exception1():
			print("method")
			raise Exception("Exception")

		@FileLogger.decorator_error("Starting test", "End test")
		def test_exception2():
			print("method")
			raise Exception("Exception")

		@FileLogger.decorator_succeeded("Starting test", "End test")
		def test_exception3():
			print("method")
			raise Exception("Exception")

		@FileLogger.decorator_warning("Starting test", "End test")
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

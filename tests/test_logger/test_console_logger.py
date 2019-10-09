from logger.loggers import ConsoleLogger
import unittest


class TestConsoleLogger(unittest.TestCase):

	def test_log(self):
		ConsoleLogger.log_info("Info")
		ConsoleLogger.log_error("Error")
		ConsoleLogger.log_warning("Warning with long text")
		ConsoleLogger.log_succeeded("Critical error")

	def test_decorators(self):
		@ConsoleLogger.decorator_info("Starting test", "End test")
		def test_decorators1():
			print("method")

		@ConsoleLogger.decorator_error("Starting test", "End test")
		def test_decorators2():
			print("method")

		@ConsoleLogger.decorator_succeeded("Starting test", "End test")
		def test_decorators3():
			print("method")

		@ConsoleLogger.decorator_warning("Starting test", "End test")
		def test_decorators4():
			print("method")

		@ConsoleLogger.decorator_info("Starting test", "End test")
		def test_exception1():
			print("method")
			raise Exception("Exception")

		@ConsoleLogger.decorator_error("Starting test", "End test")
		def test_exception2():
			print("method")
			raise Exception("Exception")

		@ConsoleLogger.decorator_succeeded("Starting test", "End test")
		def test_exception3():
			print("method")
			raise Exception("Exception")

		@ConsoleLogger.decorator_warning("Starting test", "End test")
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

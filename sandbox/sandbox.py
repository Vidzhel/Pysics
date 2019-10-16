from core.application import Application
from window.opengl_window import OpenGLWindow


class Sandbox:

	def __init__(self):
		window = OpenGLWindow(600, 300, "Sandbox")
		self.game_manager = Application(60, window)

	def start(self):
		self.game_manager.run()


if __name__ == "__main__":
	sandbox = Sandbox()
	sandbox.start()

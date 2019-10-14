from core.application import Application


class Sandbox:

	def __init__(self):
		self.game_manager = Application()
		self.init_window()

	def init_window(self):
		self.game_manager.set_screen(400, 400, "Sandbox")

	def start(self):
		self.game_manager.run()


if __name__ == "__main__":
	game = Sandbox()
	game.start()

from .base import *

class Screen(Base):
	def __init__(self):
		self.class_name = "screen"
	
	# screen.i
	def i(self) -> int:
		"""
		`screen.i`

		The screen's position in-game, as an index that increses when the player reaches the right-side and it slides over.
		"""
		return self.call("i", return_type=int)
	
	# screen.x
	def x(self) -> int:
		"""
		`screen.x`

		The screen's position in-game.
		"""
		return self.call("x", return_type=int)
	
	# screen.w
	def w(self) -> int:
		"""
		`screen.w`

		The width of the screen's ASCII grid.
		"""
		return self.call("w", return_type=int)
	
	# screen.h
	def h(self) -> int:
		"""
		`screen.h`

		The height of the screen's ASCII grid.
		"""
		return self.call("h", return_type=int)
	
	# screen.FromWorldX
	def FromWorldX(self, value:int) -> int:
		"""
		`screen.FromWorldX(int)`

		Converts a value on the X-axis from world-space to screen-space.
		"""
		return self.call("FromWorldX", value, return_type=int)
	
	# screen.FromWorldZ
	def FromWorldZ(self, value:int) -> int:
		"""
		`screen.FromWorldZ(int)`

		Converts a value from the world-space Z-axis to screen-space Y-axis.
		"""
		return self.call("FromWorldZ", value, return_type=int)
	
	# screen.ToWorldX
	def ToWorldX(self, value:int) -> int:
		"""
		`screen.ToWorldX(int)`

		Converts a value on the X-axis from screen-space to world-space.
		"""
		return self.call("ToWorldX", value, return_type=int)
	
	# screen.ToWorldZ
	def ToWorldZ(self, value:int) -> int:
		"""
		`screen.ToWorldZ(int)`

		Converts a value from the screen-space Y-axis to world-space Z-axis.
		"""
		return self.call("ToWorldZ", value, return_type=int)
	
	# screen.Next
	def Next(self) -> None:
		"""
		`screen.Next()`

		For locations that are multi-screen, moves the camera one screen forward in relation to the player.
		"""
		self.call("Next")
	
	# screen.Previous
	def Previous(self) -> None:
		"""
		`screen.Previous()`

		For locations that are multi-screen, moves the camera one screen back in relation to the player.
		"""
		self.call("Previous")
	
	# screen.ResetOffset
	def ResetOffset(self) -> None:
		"""
		`screen.ResetOffset()`

		Resets the camera to follow the player, undoing changes made by screen.Next() and screen.Previous()
		"""
		self.call("ResetOffset")
	
screen = Screen()
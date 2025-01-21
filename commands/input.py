from .base import *

class Input(Base):
	def __init__(self):
		self.class_name = "input"
	
	# input.x
	def x(self) -> int:
		"""
		`input.x`
		
		The X position, on the ASCII grid, of the input device (mouse/touch).
		"""
		return self.call("x", return_type=int)
	
	# input.y
	def y(self) -> int:
		"""
		`input.y`
		
		The Y position, on the ASCII grid, of the input device (mouse/touch).
		"""
		return self.call("y", return_type=int)
	
input = Input()
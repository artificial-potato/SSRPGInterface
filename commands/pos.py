from .base import *

class Pos(Base):
	def __init__(self):
		self.class_name = "pos"

	# pos.x
	def x(self) -> int:
		"""
		`pos.x`

		The player's current X position.
		"""
		return self.call("x", return_type=int)

	# pos.y
	def y(self) -> int:
		"""
		`pos.y`

		The player's current Y position.
		"""
		return self.call("y", return_type=int)

	# pos.z
	def z(self) -> int:
		"""
		`pos.z`

		The player's current Z position.
		"""
		return self.call("z", return_type=int)
	
pos = Pos()
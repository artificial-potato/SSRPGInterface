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
		return int(self.call("x"))

	# pos.y
	def y(self) -> int:
		"""
		`pos.y`

		The player's current Y position.
		"""
		return int(self.call("y"))

	# pos.z
	def z(self) -> int:
		"""
		`pos.z`

		The player's current Z position.
		"""
		return int(self.call("z"))
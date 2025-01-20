from .base import *

class Pickup(Base):
	def __init__(self):
		self.class_name = "pickup"

	# pickup
	def __call__(self) -> str:
		return str(self.call(""))
	
	# pickup.distance
	def distance(self) -> int:
		"""
		`pickup.distance`
		
		The distance between the player and the pickup being targeted.
		"""
		return int(self.call("distance"))
	
	# pickup.z
	def z(self) -> int:
		"""
		`pickup.z`
		
		The z position of the pickup being targeted.
		"""
		return int(self.call("z"))
	
pickup = Pickup()
"""
`pickup`

The current pickup being targeted by the player.
"""
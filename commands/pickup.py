from .base import *

class Pickup(Base):
	def __init__(self):
		self.class_name = "pickup"

	# pickup
	def __call__(self) -> str:
		return self.call("", return_type=str)
	
	# pickup.distance
	def distance(self) -> int:
		"""
		`pickup.distance`
		
		The distance between the player and the pickup being targeted.
		"""
		return self.call("distance", return_type=int)
	
	# pickup.z
	def z(self) -> int:
		"""
		`pickup.z`
		
		The z position of the pickup being targeted.
		"""
		return self.call("z", return_type=int)
	
pickup = Pickup()
"""
`pickup`

The current pickup being targeted by the player.
"""
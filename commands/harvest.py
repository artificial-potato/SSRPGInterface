from .base import *

class Harvest(Base):
	def __init__(self):
		self.class_name = "harvest"

	# harvest
	def __call__(self) -> str:
		return self.call("", return_type=str)
	
	# harvest.distance
	def distance(self) -> int:
		"""
		`harvest.distance`
		
		The distance between the player and the nearest harvestable object.
		"""
		return self.call("distance", return_type=int)
	
	# harvest.z
	def z(self) -> int:
		"""
		`harvest.z`
		
		The z position of the nearest harvestable object.
		"""
		return self.call("z", return_type=int)

harvest = Harvest()
"""
`harvest`

The next harvestable object, such as a tree or boulder.
"""
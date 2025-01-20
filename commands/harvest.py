from .base import *

class Harvest(Base):
	def __init__(self):
		self.class_name = "harvest"

	# harvest
	def __call__(self) -> str:
		return str(self.call(""))
	
	# harvest.distance
	def distance(self) -> int:
		"""
		`harvest.distance`
		
		The distance between the player and the nearest harvestable object.
		"""
		return int(self.call("distance"))
	
	# harvest.z
	def z(self) -> int:
		"""
		`harvest.z`
		
		The z position of the nearest harvestable object.
		"""
		return int(self.call("z"))

harvest = Harvest()
"""
`harvest`

The next harvestable object, such as a tree or boulder.
"""
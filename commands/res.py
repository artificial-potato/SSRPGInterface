from .base import *

class RES(Base):
	def __init__(self):
		self.class_name = "res"
	
	# res.stone
	def stone(self) -> int:
		return self.call("stone", return_type=int)
	
	# res.wood
	def wood(self) -> int:
		return self.call("wood", return_type=int)
	
	# res.tar
	def tar(self) -> int:
		return self.call("tar", return_type=int)
	
	# res.ki
	def ki(self) -> int:
		return self.call("ki", return_type=int)
	
	# res.bronze
	def bronze(self) -> int:
		return self.call("bronze", return_type=int)
	
	# res.crystals
	def crystals(self) -> int:
		return self.call("crystals", return_type=int)
	
res = RES()
"""
`res.stone`
`res.wood`
`res.tar`
`res.ki`
`res.bronze`
`res.crystals`

The player's current amount of resources in their inventory.
"""
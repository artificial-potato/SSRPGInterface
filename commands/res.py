from .base import *

class RES(Base):
	def __init__(self):
		self.class_name = "res"
	
	# res.stone
	def stone(self) -> int:
		return int(self.call("stone"))
	
	# res.wood
	def wood(self) -> int:
		return int(self.call("wood"))
	
	# res.tar
	def tar(self) -> int:
		return int(self.call("tar"))
	
	# res.ki
	def ki(self) -> int:
		return int(self.call("ki"))
	
	# res.bronze
	def bronze(self) -> int:
		return int(self.call("bronze"))
	
	# res.crystals
	def crystals(self) -> int:
		return int(self.call("crystals"))
	
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
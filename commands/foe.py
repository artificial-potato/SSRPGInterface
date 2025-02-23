from .base import *
from .buffs import Buffs

class Foe(Base):
	def __init__(self):
		self.class_name = "foe"
		self.buffs = Buffs("foe.buffs")
		self.debuffs = Buffs("foe.debuffs")

	# foe
	def __call__(self) -> str:
		return self.call("", return_type=str)
	
	# foe.id
	def id(self) -> str:
		"""
		`foe.id`

		The unique ID (or type) of the foe being targeted by the player.
		"""
		return self.call("id", return_type=str)
	
	# foe.name
	def name(self) -> str:
		"""
		`foe.name`

		The localized name of the foe being targeted by the player.
		"""
		return self.call("name", return_type=str)
	
	# foe.damage
	def damage(self) -> int:
		"""
		`foe.damage`

		The damage per attack of the foe being targeted by the player.
		"""
		return self.call("damage", return_type=int)
	
	# foe.distance
	def distance(self) -> int:
		"""
		`foe.distance`

		The distance between the player and the foe being targeted.
		"""
		return self.call("distance", return_type=int)
	
	# foe.z
	def z(self) -> int:
		"""
		`foe.z`

		The z position of the foe being targeted.
		"""
		return self.call("z", return_type=int)
	
	# foe.count
	def count(self) -> int:
		"""
		`foe.count`

		The number of foes within 46 units of the player.
		"""
		return self.call("count", return_type=int)
	
	# foe.GetCount
	def GetCount(self, distance:int) -> int:
		"""
		`foe.GetCount(int)`

		The number of foes within a specific number of units.
		"""
		return self.call("GetCount", distance, return_type=int)
	
	# foe.hp
	def hp(self) -> int:
		"""
		`foe.hp`

		The current hitpoints of the foe being targeted by the player.
		"""
		return self.call("hp", return_type=int)
	
	# foe.maxhp
	def maxhp(self) -> int:
		"""
		`foe.maxhp`

		The maximum hitpoints of the foe being targeted by the player.
		"""
		return self.call("maxhp", return_type=int)
	
	# foe.armor
	def armor(self) -> int:
		"""
		`foe.armor`

		The current armor of the foe being targeted by the player.
		"""
		return self.call("armor", return_type=int)
	
	# foe.maxarmor
	def maxarmor(self) -> int:
		"""
		`foe.maxarmor`

		The maximum armor of the foe being targeted by the player.
		"""
		return self.call("maxarmor", return_type=int)
	
	# foe.state
	def state(self) -> int:
		"""
		`foe.state`

		A number representing the target foe's current state.
		"""
		return self.call("state", return_type=int)
	
	# foe.time
	def time(self) -> int:
		"""
		`foe.time`

		Elapsed number of frames in target foe's current state.
		"""
		return self.call("time", return_type=int)
	
	# foe.level
	def level(self) -> int:
		"""
		`foe.level`

		The level number of the target foe.
		"""
		return self.call("level", return_type=int)
	
foe = Foe()
"""
`foe`

The current foe being targeted by the player.
"""
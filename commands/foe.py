from .base import *
from .buffs import Buffs

class Foe(Base):
	def __init__(self):
		self.class_name = "foe"
		self.buffs = Buffs("foe.buffs")
		self.debuffs = Buffs("foe.debuffs")

	# foe
	def __call__(self) -> str:
		return str(self.call(""))
	
	# foe.id
	def id(self) -> str:
		"""
		`foe.id`

		The unique ID (or type) of the foe being targeted by the player.
		"""
		return str(self.call("id"))
	
	# foe.name
	def name(self) -> str:
		"""
		`foe.name`

		The localized name of the foe being targeted by the player.
		"""
		return str(self.call("name"))
	
	# foe.damage
	def damage(self) -> int:
		"""
		`foe.damage`

		The damage per attack of the foe being targeted by the player.
		"""
		return int(self.call("damage"))
	
	# foe.distance
	def distance(self) -> int:
		"""
		`foe.distance`

		The distance between the player and the foe being targeted.
		"""
		return int(self.call("distance"))
	
	# foe.z
	def z(self) -> int:
		"""
		`foe.z`

		The z position of the foe being targeted.
		"""
		return int(self.call("z"))
	
	# foe.count
	def count(self) -> int:
		"""
		`foe.count`

		The number of foes within 46 units of the player.
		"""
		return int(self.call("count"))
	
	# foe.GetCount
	def GetCount(self, distance:int) -> int:
		"""
		`foe.GetCount(int)`

		The number of foes within a specific number of units.
		"""
		return int(self.call("GetCount", distance))
	
	# foe.hp
	def hp(self) -> int:
		"""
		`foe.hp`

		The current hitpoints of the foe being targeted by the player.
		"""
		return int(self.call("hp"))
	
	# foe.maxhp
	def maxhp(self) -> int:
		"""
		`foe.maxhp`

		The maximum hitpoints of the foe being targeted by the player.
		"""
		return int(self.call("maxhp"))
	
	# foe.armor
	def armor(self) -> int:
		"""
		`foe.armor`

		The current armor of the foe being targeted by the player.
		"""
		return int(self.call("armor"))
	
	# foe.maxarmor
	def maxarmor(self) -> int:
		"""
		`foe.maxarmor`

		The maximum armor of the foe being targeted by the player.
		"""
		return int(self.call("maxarmor"))
	
	# foe.state
	def state(self) -> int:
		"""
		`foe.state`

		A number representing the target foe's current state.
		"""
		return int(self.call("state"))
	
	# foe.time
	def time(self) -> int:
		"""
		`foe.time`

		Elapsed number of frames in target foe's current state.
		"""
		return int(self.call("time"))
	
	# foe.level
	def level(self) -> int:
		"""
		`foe.level`

		The level number of the target foe.
		"""
		return int(self.call("level"))
	
foe = Foe()
"""
`foe`

The current foe being targeted by the player.
"""
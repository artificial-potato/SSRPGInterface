from .base import *
from .buffs import Buffs

class Armor(Base):
	def __init__(self):
		self.class_name = "armor"
	
	# armor
	def __call__(self) -> int:
		return int(self.call(""))
	
	# armor.f
	def f(self) -> int:
		return int(self.call("f"))

armor = Armor()
buffs = Buffs("buffs")
debuffs = Buffs("debuffs")

def hp() -> int:
	"""
	`hp`

	The player's current hitpoints.
	"""
	return int(call("hp"))

def maxhp() -> int:
	"""
	`maxhp`

	The player's maximum hitpoints.
	"""
	return int(call("maxhp"))

def maxarmor() -> int:
	"""
	`maxarmor`

	The player's maximum armor, rounded down.
	"""
	return int(call("maxarmor"))

def face() -> str:
	"""
	`face`

	The player's current facial expression.
	"""
	return str(call("face"))

def bighead() -> bool:
	"""
	`bighead`

	True if the player has Big Head enabled (Moondial).
	"""
	return bool(call("bighead"))

def totalgp() -> int:
	"""
	`totalgp`

	The total "Gear Power" of your inventory, calculated from item star levels and enchantment bonuses.
	"""
	return int(call("totalgp"))
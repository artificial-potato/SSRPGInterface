from .base import *
from .buffs import Buffs

class Armor(Base):
	def __init__(self):
		self.class_name = "armor"
	
	# armor
	def __call__(self) -> int:
		return self.call("", return_type=int)
	
	# armor.f
	def f(self) -> int:
		return self.call("f", return_type=int)

armor = Armor()
buffs = Buffs("buffs")
debuffs = Buffs("debuffs")

def hp() -> int:
	"""
	`hp`

	The player's current hitpoints.
	"""
	return call("hp", return_type=int)

def maxhp() -> int:
	"""
	`maxhp`

	The player's maximum hitpoints.
	"""
	return call("maxhp", return_type=int)

def maxarmor() -> int:
	"""
	`maxarmor`

	The player's maximum armor, rounded down.
	"""
	return call("maxarmor", return_type=int)

def face() -> str:
	"""
	`face`

	The player's current facial expression.
	"""
	return call("face", return_type=str)

def bighead() -> bool:
	"""
	`bighead`

	True if the player has Big Head enabled (Moondial).
	"""
	return call("bighead", return_type=bool)

def totalgp() -> int:
	"""
	`totalgp`

	The total "Gear Power" of your inventory, calculated from item star levels and enchantment bonuses.
	"""
	return call("totalgp", return_type=int)
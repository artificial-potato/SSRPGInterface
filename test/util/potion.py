from SSRPGInterface.commands import *
from .boss import bossStart

Potion_Type = [
	"Empty",
	"Lucky",
	"Berserk",
	"Vampiric",
	"Strength",
	"Invisibility",
	"Cleansing",
	"Defensive",
	"Healing",
	"Lightning",
	"Experience",
]

Potion_Formula = {
	"Lucky":		("stone", "bronze"),
	"Berserk":		("wood", "bronze"),
	"Vampiric":		("tar", "bronze"),
	"strength":		("stone",),
	"Invisibility":	("stone", "bronze"),
	"Cleansing":	("tar", "wood"),
	"Defensive":	("tar", "stone"),
	"Healing":		("tar",),
	"Lightning":	("bronze",),
	"Experience":	("wood",),
}

Potion_Buff = {
	"Lucky":		"lucky_crit",
	"Berserk":		"berserk",
	"Vampiric":		"vampiric",
	"strength":		"strength",
	"Invisibility":	"invisibility",
	"Experience":	"experience",
	# "Cleansing":	None,
	# "Defensive":		None,
	# "Healing":		None,
	# "Lightning":	None,
}


def name_correction(name):
	if name in Potion_Type:
		return name
	else:
		for potion in Potion_Type:
			if name.lower() == potion.lower():
				print(f'unexist "{name}" Potion, did you mean "{potion}"?')
				return potion
	return None

def brew_potion(name:str):
	name = name_correction(name)
	if name:
		command.Brew(*Potion_Formula[name])

StackPotion = False
def check_StackPotion(needStackPotion=True):
	global StackPotion
	StackPotion = needStackPotion and \
	(loc.averageTime() < 0 or get_potion_time() < loc.averageTime())
	return StackPotion

def get_potion_type(name:str=None):
	potion = item.potion()
	if name:
		name = name_correction(name)
		if not name is None:
			return name in potion
	for pt in Potion_Type:
		if pt in potion:
			return pt
	return None


def useStackPotion():
	if not get_potion_type("Empty") and \
	(("star" in item.right() and bossStart) \
	or StackPotion):
		command.Activate("potion")
		return True
	return False
	
def get_potion_time():
	for potion in Potion_Buff:
		buff_time = buffs.GetTime(Potion_Buff[potion])
		if buff_time:
			return buff_time
	return 0

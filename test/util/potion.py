from SSRPGInterface.commands import *
from .boss import boss_start

POTION_TYPE = [
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

POTION_FORMULA = {
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

POTION_BUFF = {
	"Lucky":		"lucky_crit",
	"Berserk":		"berserk",
	"Vampiric":		"vampiric",
	"strength":		"strength",
	"Invisibility":	"invisibility",
	"Experience":	"experience",
	# "Cleansing":	None,
	# "Defensive":	None,
	# "Healing":		None,
	# "Lightning":	None,
}


def name_correction(name):
	potion_type = POTION_TYPE
	if name in potion_type:
		return name
	else:
		name_lower = name.lower()
		for potion in potion_type:
			if name_lower == potion.lower():
				print(f'unexist "{name}" Potion, did you mean "{potion}"?')
				return potion
	return None

def brew_potion(name:str):
	name = name_correction(name)
	if name:
		command.Brew(*POTION_FORMULA[name])

StackPotion = False
def check_StackPotion(needStackPotion=True):
	set_StackPotion(
		needStackPotion and
		(loc.averageTime() < 0 or
   		get_potion_time() < loc.averageTime())
	)

def get_StackPotion() -> bool:
	return StackPotion

def set_StackPotion(value:bool):
	global StackPotion
	StackPotion = value

def get_potion_type(name:str=None):
	potion = item.potion()

	if name:
		name = name_correction(name)
		if not name is None:
			return name in potion

	potion_type = POTION_TYPE
	for pt in potion_type:
		if pt in potion:
			return pt
	return None


def useStackPotion():
	if not get_potion_type("Empty") and \
	(("star" in item.right() and boss_start) \
	or StackPotion):
		command.Activate("potion")
		return True
	return False
	
def get_potion_time():
	pb = POTION_BUFF
	for potion, buff in pb.items():
		buff_time = buffs.GetTime(buff)
		if buff_time:
			return buff_time
	return 0

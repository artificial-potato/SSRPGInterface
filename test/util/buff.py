from SSRPGInterface.commands import *

def need_fire():
	return foe.debuffs.GetTime("debuff_dot") <= 10



def need_poison():
	return foe.debuffs.GetTime("debuff_damage") <= 10



def need_ice_count(n):
	return foe.debuffs.GetCount("debuff_chill") < n \
	or foe.debuffs.GetTime("debuff_chill") <= 10

def need_ice():
	return need_ice_count(6)

def ice_effect():
	return foe.debuffs.GetCount("debuff_chill") * 20 / 3
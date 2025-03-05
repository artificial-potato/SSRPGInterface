from SSRPGInterface.commands import *
from .weaper import *

def skill_can_use(name):
	return item.GetCooldown(name) <= 0 and item.CanActivate()



def blade_skill():
	if skill_can_use("blade") \
	and foe.distance() <= 23:
		select_equipT("blade")
		command.Equip("blade")
		command.Activate("R")
		return True
	return False

def blade_skill_screenMove():
	if skill_can_use("blade") \
	and foe.distance() <= 23:
		screen.Next() 
		
		if screen.x == screen.i * 69 + 55:
			blade_skill()
			screen.ResetOffset() 
			return True
	return False

def mask_skill():
	if skill_can_use("mask") \
	and foe.distance() < 24:
		select_equipT("mask")
		command.EquipR("mask")
		command.Activate("R")
		return True
	return False

def arm_skill():
	if "pick_pocket" in buffs.string() \
	and foe.distance() > 3 and foe.distance() < 9 \
	and skill_can_use("skeleton_arm"):
		select_equipT("skeleton_arm")
		command.Equip("skeleton_arm")
		command.Activate("R")
		return True
	return False

def hammer_skill(weaper:str=heavy):
	if (skill_can_use("heavy_hammer") \
	and foe.distance() <= 23) \
	or R_in_use("heavy"):
		select_equipT(weaper)
		command.Equip(weaper)
		command.Activate("R")
		return True
	return False

def bardiche_skill(weaper:str=bardiche):
	if (skill_can_use("bardiche") \
	and foe.distance() <= 10) \
	or R_in_use("bardiche"):
		select_equipT(weaper)
		command.Equip(weaper)
		command.Activate("R")
		return True
	return False

def quarterstaff_skill():
	if skill_can_use("quarterstaff"):
		select_equipT("quarterstaff")
		command.Equip("quarterstaff")
		command.Activate("R")
		return True
	return False

def dash_skill():
	if skill_can_use("dash"):
		select_equip("trisk", "dash")
		return True
	return False

def bash_skill():
	if skill_can_use("bash"):
		select_equip("trisk", "bash")
		return True
	return False

def sprint(lost:bool=False):
	if foe.distance() > 10:
		if foe.distance() <= 16:
			if lost:
				if bash_skill(): return True
				if dash_skill(): return True
			else:
				if dash_skill(): return True
				if bash_skill(): return True
		if quarterstaff_skill(): return True
	restoreArmor("sword")
	return False


def mind_skill():
	if skill_can_use("mind"):
		select_equip("quest", "mind")
		return True
	return False

def fire_talisman_skill():
	if summon.GetId() != "cinderwisp" \
	and skill_can_use("fire_talisman") \
	or R_in_use("fire_talisman"):
		select_equip("trisk", "fire_talisman")
		command.EquipL("trisk")
		command.EquipR("fire_talisman")
		command.Activate("R")
		return True
	return False

def cinderwisp_skill_count(n):
	if summon.GetId() == "cinderwisp" \
	and item.GetCooldown("cinderwisp") <= 0 \
	and summon.GetVar("ignition") >= n:
		command.Activate("cinderwisp")
		return True
	return False

def cinderwisp_skill():
	return cinderwisp_skill_count(6)


def aether_talisman_skill():
	if summon.GetId() != "voidweaver" \
	and skill_can_use("aether_talisman") \
	or R_in_use("aether_talisman"):
		select_equip("trisk", "aether_talisman")
		command.EquipL("trisk")
		command.EquipR("aether_talisman")
		command.Activate("R")
		return True
	return False

def voidweaver_skill():
	if summon.GetId() == "voidweaver" \
	and item.GetCooldown("voidweaver") <= 0:
		command.Activate("voidweaver")
		return True
	return False
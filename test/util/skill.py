from SSRPGInterface.commands import *
from .weaper import *

def blade_skill():
	if item.GetCooldown("blade") <= 0 \
	and foe.distance() <= 23 \
	and item.CanActivate():
		select_equipT("blade")
		command.Equip("blade")
		command.Activate("R")
		return True
	return False

def blade_skill_screenMove():
	if item.GetCooldown("blade") <= 0 \
	and foe.distance() <= 23 \
	and item.CanActivate():
		screen.Next() 
		
		if screen.x == screen.i * 69 + 55:
			blade_skill()
			screen.ResetOffset() 
			return True
	return False

def mask_skill():
	if item.CanActivate() \
	and item.GetCooldown("mask") <= 0 \
	and foe.distance() < 24:
		select_equipT("mask")
		command.EquipR("mask")
		command.Activate("R")
		return True
	return False

def arm_skill():
	if "pick_pocket" in buffs.string() \
	and foe.distance() > 3 and foe.distance() < 9 \
	and item.GetCooldown("skeleton_arm") <= 0 \
	and item.CanActivate():
		select_equipT("skeleton_arm")
		command.Equip("skeleton_arm")
		command.Activate("R")
		return True
	return False

def hammer_skill(weaper:str=heavy):
	if (item.CanActivate() \
	and item.GetCooldown("heavy_hammer") <= 0 \
	and foe.distance() <= 23) \
	or ("heavy" in item.right() and item.right.state() == 2):
		select_equipT(weaper)
		command.Equip(weaper)
		command.Activate("R")
		return True
	return False

def bardiche_skill(weaper:str=bardiche):
	if (item.CanActivate() \
	and item.GetCooldown("bardiche") <= 0 \
	and foe.distance() <= 10) \
	or ("bardiche" in item.right() and item.right.state() == 2):
		select_equipT(weaper)
		command.Equip(weaper)
		command.Activate("R")
		return True
	return False

def quarterstaff_skill():
	if item.GetCooldown("quarterstaff") <= 0 \
	and item.CanActivate():
		select_equipT("quarterstaff")
		command.Equip("quarterstaff")
		command.Activate("R")
		return True
	return False

def dash_skill():
	if item.GetCooldown("dash") <= 0 \
	and item.CanActivate():
		select_equip("trisk", "dash")
		return True
	return False

def bash_skill():
	if item.GetCooldown("bash") <= 0 \
	and item.CanActivate():
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
	if item.GetCooldown("mind") <= 0:
		select_equip("quest", "mind")
		return True
	return False

def fire_talisman_skill():
	if summon.GetId() != "cinderwisp" \
	and (item.CanActivate() and item.GetCooldown("fire_talisman") <= 0 \
	or "fire_talisman" in item.right() and item.right.state() == 2):
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
	if (summon.GetId() != "voidweaver" \
	and item.CanActivate() and item.GetCooldown("aether_talisman") <= 0) \
	or ("aether_talisman" in item.right() and item.right.state() == 2):
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
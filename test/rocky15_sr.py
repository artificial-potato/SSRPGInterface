from SSRPGInterface.commands import *
import SSRPGInterface
from util import *

Potion = "Lucky"

def beginAction():
	
	brew_potion(Potion)
	
	select_equip("quest", value_shield)

	global StackPotion
	StackPotion = check_StackPotion()

	set_bossStart(False)



def action():
	if "phase1" in foe() and foe.hp() != foe.maxhp():
		set_bossStart(True)

	cinderwisp_skill()

	if starPickup():
		return
	
	if not (ai.enabled() or ai.paused()):
		reset_attack_loop()
		if StackPotion:
			select_equip("quest", "mask")
		else:
			restoreArmor("quest")
		return

	if foe.distance() > 25:
		run()
	
	else:
		f = foe()
		if StackPotion:
			if "phase1" in f:
				boss_1_stackPotion()
			elif "phase2" in f:
				boss_2_stackPotion()
			elif "phase3" in f:
				boss_3_stackPotion()
			elif "boss" in f:
				boss_0_stackPotion()
			else:
				attack_stackPotion()
		else:
			if "phase1" in f:
				boss_1()
			elif "phase2" in f:
				boss_2()
			elif "phase3" in f:
				boss_3()
			elif "boss" in f:
				boss_0()
			else:
				attack()



def run():
	if quarterstaff_skill():
		return
	if fire_talisman_skill():
		return
	if useStackPotion():
		return
	if StackPotion:
		select_equip("trisk", "mask")
	else:
		restoreArmor("trisk")


def attack():
	return

def attack_stackPotion():
	return


def boss_0():
	if foe.distance() <= 10:
		if hp() != maxhp():
			moondialing_3_3(dL1, dL2)
		else:
			moondialing_3_3(dP, dI)
	else:
		sprint(True)

def boss_0_stackPotion():
	if foe.distance() <= 10:
		if need_poison():
			select_equip(dP, "mask")
		else:
			select_equip(dI, "mask")
	else:
		sprint(True)


def boss_1():
	if foe.distance() <= 10:
		if hp() != maxhp():
			moondialing_3_3(dL1, dL2)
		else:
			moondialing_3_3(dP, dI)
	else:
		sprint(True)

def boss_1_stackPotion():
	if foe.distance() <= 10:
		if need_poison():
			select_equip(dP, "mask")
		elif need_ice():
			select_equip(dI, "mask")
		else:
			select_equip(dL1, "mask")
	else:
		sprint(True)


def boss_2():
	if foe.distance() <= 10:
		if "Poison" in foe():
			moondialing_3_3(ice1, ice2)
		elif "Vigor" in foe():
			moondialing_3_3(poison1, poison2)
		elif "AEther" in foe():
			moondialing_3_3(vigor1, vigor2)
		elif "Fire" in foe():
			moondialing_3_3(aether1, aether2)
		elif "Ice" in foe():
			moondialing_3_3(fire1, fire2)
	else:
		sprint(True)

def boss_2_stackPotion():
	if foe.distance() <= 10:
		if "Poison" in foe():
			select_equip(ice1, "mask")
		elif "Vigor" in foe():
			select_equip(poison1, "mask")
		elif "AEther" in foe():
			select_equip(vigor1, "mask")
		elif "Fire" in foe():
			select_equip(aether1, "mask")
		elif "Ice" in foe():
			select_equip(fire1, "mask")

		if foe.time() < 30 + ice_effect():
			if hp() != maxhp():
				select_equip(dL1, "mask")
			if not foe.buffs.GetCount("buff_protection"):
				if need_ice():
					select_equip(dI, "mask")
	else:
		sprint(True)


def boss_3():
	if foe.distance() <= 10:
		if foe.hp() == foe.maxhp():
			select_equip("moon", dI)
			return

		if get_potion_type(Potion):
			command.Activate("potion")

		moondialing_3_3(poison1, poison2)
	else:
		sprint(True)

def boss_3_stackPotion():
	if foe.state in (32, 115) and not foe.time():
		next_attack_loop(6)

	if attackLoop == 2 and timing(32, 27) and foe.distance() < 8:
		mind_skill()
		return

	if foe.distance() <= 10:
		if attackLoop == 2 and timing(32, 12):
			if hammer_skill():
				return

		if attackLoop != 2 and timing(32, 39):
			if mask_skill():
				return
			if need_poison():
				select_equip(dP, "mask")
				return

		if need_ice():
			select_equip(dI, "mask")
			return

		if not foe.buffs.GetCount("adaptive_defense_poison"):
			select_equip(poison1, "mask")
		elif not foe.buffs.GetCount("adaptive_defense_vigor"):
			select_equip(vigor1, "mask")
		elif not foe.buffs.GetCount("adaptive_defense_aether"):
			select_equip(aether1, "mask")
		elif not foe.buffs.GetCount("adaptive_defense_fire"):
			select_equip(fire1, "mask")
		elif not foe.buffs.GetCount("adaptive_defense_ice"):
			select_equip(ice1, "mask")
	else:
		sprint(True)


def main():
	if totaltime() <= 1:
		beginAction()
	else:
		action()

	changeEquip()

	show()
 
def show():
	print(f'\r{loc.begin()}\t{loc.loop()}\t{totaltime()}\t{StackPotion}\t{foe()}')
	pass

if __name__ == "__main__":
	SSRPGInterface.run_script(main)

# sys.MindConnect()
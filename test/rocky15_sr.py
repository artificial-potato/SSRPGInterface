from SSRPGInterface.commands import *
import SSRPGInterface
from util import *

POTION = "Lucky"

action_mode = ""
def get_action_mode():
	return action_mode
def set_action_mode(value:str):
	global action_mode
	action_mode = value



def beginAction():
	brew_potion(POTION)

	select_equip("quest", value_shield)

	check_StackPotion()

	set_bossStart(False)



def action():
	if "phase1" in foe() and foe.hp() != foe.maxhp():
		set_bossStart(True)

	cinderwisp_skill()

	if starPickup():
		return

	if not (ai.enabled() or ai.paused()):
		set_action_mode("idle")

		reset_attack_loop()
		if get_StackPotion():
			select_equip("quest", "mask")
		else:
			restoreArmor("quest")
		return

	if foe.distance() > 25:
		run()

	else:
		f = foe()
		if get_StackPotion():
			if "phase" in f:
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
			if "phase" in f:
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
	set_action_mode("run")

	if quarterstaff_skill():
		return
	if fire_talisman_skill():
		return
	if useStackPotion():
		return
	if get_StackPotion():
		select_equip("trisk", "mask")
	else:
		restoreArmor("trisk")


def attack():
	set_action_mode("attack")
	return

def attack_stackPotion():
	set_action_mode("attack_stackPotion")
	return


def boss_0():
	set_action_mode("boss_0")

	if foe.distance() <= 10:
		if hp() != maxhp():
			moondialing_3_3(dL1, dL2)
		else:
			moondialing_3_3(dP, dI)
	else:
		sprint(True)

def boss_0_stackPotion():
	set_action_mode("boss_0_stackPotion")

	if foe.distance() <= 10:
		if need_poison():
			select_equip(dP, "mask")
		else:
			select_equip(dI, "mask")
	else:
		sprint(True)


def boss_1():
	set_action_mode("boss_1")

	if foe.distance() <= 10:
		if hp() != maxhp():
			moondialing_3_3(dL1, dL2)
		else:
			moondialing_3_3(dP, dI)
	else:
		sprint(True)

def boss_1_stackPotion():
	set_action_mode("boss_1_stackPotion")

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
	set_action_mode("boss_2")

	if foe.distance() <= 10:
		wsi = get_weakness_element_index()
		moondialing_3_3(*ELEMENT_WEAPER[wsi])
	else:
		sprint(True)

def boss_2_stackPotion():
	set_action_mode("boss_2_stackPotion")

	if foe.distance() <= 10:
		wsi = get_weakness_element_index()
		select_equip(ELEMENT_WEAPER[wsi][0], "mask")

		if foe.time() < 30 + ice_effect():
			if hp() != maxhp():
				select_equip(dL1, "mask")
			if not foe.buffs.GetCount("buff_protection"):
				if need_ice():
					select_equip(dI, "mask")
	else:
		sprint(True)


def boss_3():
	set_action_mode("boss_3")

	if foe.distance() <= 10:
		if foe.hp() == foe.maxhp():
			select_equip("moon", dI)
			return

		if get_potion_type(POTION):
			command.Activate("potion")

		moondialing_3_3(poison1, poison2)
	else:
		sprint(True)

ADAPTIVE_DEFENSE_ELEMENT = [
	"adaptive_defense_ice",
	"adaptive_defense_fire",
	"adaptive_defense_aether",
	"adaptive_defense_vigor",
	"adaptive_defense_poison",
]
def boss_3_stackPotion():
	set_action_mode("boss_3_stackPotion")

	if foe.state in (32, 115) and not foe.time():
		next_attack_loop(6)

	if attack_loop == 2 and timing(32, 27) and foe.distance() < 8:
		mind_skill()
		return

	if foe.distance() <= 10:
		if attack_loop == 2 and timing(32, 12):
			if hammer_skill():
				return

		if attack_loop != 2 and timing(32, 39):
			if mask_skill():
				return
			if need_poison():
				select_equip(dP, "mask")
				return

		if need_ice():
			select_equip(dI, "mask")
			return

		adaptive_defense_element = ADAPTIVE_DEFENSE_ELEMENT
		length = len(adaptive_defense_element)
		for i in range(length):
			i = length - 1 - i
			if not foe.buffs.GetCount(adaptive_defense_element[i]):
				select_equip(ELEMENT_WEAPER[i][0], "mask")
				break
	else:
		sprint(True)


def main():
	aac()

	if totaltime() <= 1:
		beginAction()
	else:
		action()

	changeEquip()

	show()

def show():
	print(f'\r{loc.begin()}\t{loc.loop()}\t{totaltime()}\t{get_StackPotion()}\t{get_weakness_element()}\t{get_element_index()}\t{foe()}')
	pass

if __name__ == "__main__":
	SSRPGInterface.run(main)

# sys.MindConnect()
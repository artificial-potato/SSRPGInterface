from SSRPGInterface.commands import *
from .data import *


ELEMENTS = [
	"Ice",
	"Fire",
	"AEther",
	"Vigor",
	"Poison",
]

def get_element_index(target_element:str=None) -> int:
	elements = ELEMENTS
	length = 5 #len(ELEMENTS)
	if target_element:
		if target_element in elements:
			return elements.index(target_element)
		else:
			target_element_lower = target_element.lower()
			for i in range(length):
				if target_element_lower == elements[i].lower():
					print(f'unexist "{target_element}" Element, did you mean "{elements[i]}"?')
					return i
	f = foe()
	if f:
		for i in range(length):
			if elements[i] in f:
				return i
	return -1

def get_weakness_element_index(target_element:str=None) -> str:
	index = get_element_index(target_element)
	return -1 if index < 0 else (index + 1) % len(ELEMENTS)

def get_weakness_element(target_element:str=None) -> str:
	index = get_weakness_element_index(target_element)
	return "Stone" if index < 0 else ELEMENTS[index]


def L_in_use(name):
	return name in item.left() and item.left.state() == 2
def R_in_use(name):
	return name in item.right() and item.right.state() == 2




def aac():
	if item.left.state() == 3:
		command.EquipL("sword")
	if item.right.state == 3:
		command.EquipR("shield")



eL = None
eR = None
def select_equipL(e):
	global eL
	eL = e

def select_equipR(e):
	global eR
	eR = e

def select_equip(L, R):
	select_equipL(L)
	select_equipR(R)

def select_equipT(e):
	select_equip(e, e)

def changeEquip():
	aac()
	if eL == eR and eL:
		command.Equip(eL)
	else:
		if eL:
			command.EquipL(eL)
		if eR:
			command.EquipR(eR)



def starPickup():
	if pickup.distance() <= 5:
		select_equip("trisk", "star")
		return True
	return False

def restoreArmor(L):
	speed_maxarmor = speed_shield_value
	if L == "quest":
		speed_maxarmor += 2
	if armor() >= speed_maxarmor:
		select_equip(L, value_shield)
	else:
		select_equip(L, speed_shield)

def moondialing_3_3(L, R):
	moonTimer = totaltime() % 3
	if moonTimer == 0:
		select_equip(L, "moon")
	elif moonTimer == 1:
		select_equip("moon", R)
	elif moonTimer == 2:
		select_equip(R, L)
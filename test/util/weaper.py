from SSRPGInterface.commands import *
from .data import *


elements = [
	"Ice",
	"Fire",
	"AEther",
	"Vigor",
	"Poison",
]

def get_weakness_element(target_element:str=None):
	length = 5 #len(elements)
	index = -1
	if target_element:
		if target_element in elements:
			index = elements.index(target_element)
		else:
			for i in range(length):
				if target_element.lower() == elements[i].lower():
					print(f'unexist "{target_element}" Element, did you mean "{elements[i]}"?')
					index = i
					break
	if index < 0:
		f = foe()
		if f:
			for i in range(length):
				if elements[i] in f:
					index = i
					break
	if index < 0:
		return None
	else:
		return elements[(index + 1) % length]
	


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
		select_equip("moon", R)
	elif moonTimer == 1:
		select_equip("moon", L)
	elif moonTimer == 2:
		select_equip(L, R)
from SSRPGInterface.commands import *
from .buff import ice_effect

bossStart = False

def set_bossStart(value:bool):
	global bossStart
	bossStart = value



attackLoop = -1

def reset_attack_loop():
	attackLoop = -1
	return attackLoop


def next_attack_loop(loopCount):
	attackLoop = (attackLoop + 1) % loopCount
	return attackLoop


def timing(s, t):
	return foe.state == s and foe.time >= t + ice_effect()
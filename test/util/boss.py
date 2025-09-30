from SSRPGInterface.commands import *
from .buff import ice_effect

boss_start = False

def set_bossStart(value:bool):
	global boss_start
	boss_start = value



attack_loop = -1

def set_attack_loop(value:int):
	global attack_loop
	attack_loop = value

def reset_attack_loop():
	set_attack_loop(-1)

def next_attack_loop(loop_count):
	set_attack_loop((attack_loop + 1) % loop_count)



def timing(s, t):
	return foe.state() == s and foe.time() >= t + ice_effect()
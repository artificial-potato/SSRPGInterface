from os import system
from SSRPGInterface.commands import *
from SSRPGInterface import run
from util.map import get_screen

HEAD = [
	',--.',
	'/   ¯\\'
]
HEAD_WIDTH = 6
HEAD_HEIGHT = 1

Box = 1
Position = [0, 1, 2]
old_moving = [False] * 3

offsetX = 6
offsetY = 3

def get_target_in_moving(x, y) -> list[bool]:
	screen = [
		get_screen(
			x + offsetX * i,
			y + offsetY * i,
			HEAD_WIDTH, HEAD_HEIGHT
		) for i in range(3)
	]
	return [not (HEAD[0] in i or HEAD[1] in i) for i in screen]

def check_move(moving):
	global Box, Position, old_moving
	if moving == old_moving:
		return
	old_moving = moving
	if moving.count(True) > 1:
		for i in range(3):
			for j in range(i + 1, 3):
				if moving[i] and moving[j]:
					if Box == i:
						Box = j
					elif Box == j:
						Box = i
					Position[i], Position[j] = Position[j], Position[i]
					return True
	return False

def check_box(x, y):
	global Box
	for i in range(3):
		if get_screen(x + offsetX * i, y + offsetY * i, 1, 1) == "ε":
			Box = i
			return

def main():
	if pos.x() < 52 or not "undead_crypt_intro" in loc():
		return
	
	print(f'\r{Box}\t{Position}', end="")
	screen_w = screen.w()
	screen_h = screen.h()

	moving = get_target_in_moving(screen_w // 2 - 6, screen_h // 2 - 11)

	if not check_move(moving):
		check_box(screen_w // 2 - 7, screen_h // 2 - 10)
	print(f'\t{moving}\t{moving.count(True) > 1}', end="")


if __name__ == "__main__":
	run(main)
from ..ssrpgif import call_command

class Command():
	def call(self, name, *args):
		call_command(name, *args)

	def Print(self, *args, 
		   x:int=None, y:int=None, color:str=None, 
		   face:bool=False, player:bool=False, head:bool=False, foe:bool=False, center:bool=False
		):
		str_list = []
		if face:
			str_list.append("(")
		elif type(x) is int and type(y) is int:
			if player:
				str_list.append("o")
			elif head:
				str_list.append("h")
			elif foe:
				str_list.append("f")
			elif center:
				str_list.append("c")
			else:
				str_list.append("`")
			str_list.append(f'{x},')
			str_list.append(f'{y},')
			if color:
				str_list.append(f'{color},')
		str_list += map(lambda a: str(a), args)

		self.call(">", "".join(str_list))

	def Play(self, *args):
		self.call("play", " ".join(args))

	def EquipR(self, *args:str):
		self.call("equipR", " ".join(args))

	def EquipL(self, *args:str):
		self.call("equipL", " ".join(args))

	# def EquipF(self, *args:str):
	# 	self.call("equipF", " ".join(args))

	def Equip(self, *args:str):
		self.call("equip", " ".join(args))

	def Loadout(self, index:int):
		self.call("loadout", index)

	def Activate(self, *args):
		self.call("activate", " ".join(args))

	def Enable(self, *args):
		self.call("enable", " ".join(args))

	def Disable(self, *args):
		self.call("disable", " ".join(args))

	# def Profile(self, *args):
	# 	self.call("profile", " ".join(args))

	def Brew(self, *args:str):
		self.call("brew", "+".join(args))

command = Command()
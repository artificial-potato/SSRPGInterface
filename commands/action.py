from ..ssrpgif import call_command

class Command():
	def call(self, name, *args):
		call_command(name, *args)

	def Print(self, *args):
		self.call(">", *args)
	def Play(self, *args):
		self.call("play", *args)
	def EquipR(self, *args):
		self.call("equipR", *args)
	def EquipL(self, *args):
		self.call("equipL", *args)
	def EquipF(self, *args):
		self.call("equipF", *args)
	def Equip(self, *args):
		self.call("equip", *args)
	def Loadout(self, *args):
		self.call("loadout", *args)
	def Activate(self, *args):
		self.call("activate", *args)
	def Enable(self, *args):
		self.call("enable", *args)
	def Disable(self, *args):
		self.call("disable", *args)
	def Profile(self, *args):
		self.call("profile", *args)
	def Brew(self, *args):
		self.call("brew", *args)

command = Command()
from .base import *

class Buffs(Base):
	# buffs.count
	# debuffs.count
	# foe.buffs.count
	# foe.debuffs.count
	def count(self) -> int:
		"""
		`buffs.count`
		The number of buffs (positive effects) on the player.

		`debuffs.count`
		The number of debuffs (negative effects) on the player.
		
		`foe.buffs.count`
		The number of buffs (positive effects) on the foe being targeted.

		`foe.debuffs.count`
		The number of debuffs (negative effects) on the foe being targeted.
		"""
		return int(self.call("count"))
	
	# buffs.string
	# debuffs.string
	# foe.buffs.string
	# foe.debuffs.string
	def string(self) -> str:
		"""
		`buffs.string`
		A composite of information about all buffs on the player.
		
		`debuffs.string`
		A composite of information about all debuffs on the player.

		`foe.buffs.string`
		A composite of information about all the buffs on the target foe.

		`foe.debuffs.string`
		A composite of information about all the debuffs on the target foe.
		"""
		return str(self.call("string"))
	
	# buffs.GetCount
	# debuffs.GetCount
	# foe.buffs.GetCount
	# foe.debuffs.GetCount
	def GetCount(self, buff_name:str) -> int:
		"""
		`buffs.GetCount(str)`
		The number of a specific buff on the player.

		`debuffs.GetCount(str)`
		The number of a specific debuff on the player.

		`foe.buffs.GetCount(str)`
		The number of a specific buff on the target foe.

		`foe.debuffs.GetCount(str)`
		The number of a specific debuff on the target foe.
		"""
		return int(self.call("GetCount", buff_name))
	
	# buffs.GetTime
	# debuffs.GetTime
	# foe.buffs.GetTime
	# foe.debuffs.GetTime
	def GetTime(self, buff_name:str) -> int:
		"""
		`buffs.GetTime(str)`
		The duration of a specific buff on the player.

		`debuffs.GetTime(str)`
		The duration of a specific debuff on the player.

		`foe.buffs.GetTime(str)`
		The duration of a specific buff on the target foe.

		`foe.debuffs.GetTime(str)`
		The duration of a specific debuff on the target foe.

		"""
		return int(self.call("GetTime", buff_name))
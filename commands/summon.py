from .base import *

class Summon(Base):
	def __init__(self):
		self.class_name = "summon"
	
	# summon.count
	def count(self) -> int:
		"""
		`summon.count`
		
		The number of summoned allies currently in game.
		"""
		return int(self.call("count"))
	
	# summon.GetId
	def GetId(self, index:int=0) -> str:
		"""
		`summon.GetId(index = 0)`
		
		Returns the ID of the summon at a given index. 
		The index parameter is optional and defaults to zero (first summon). 
		Returns null if no summons are at that index.
		"""
		return str(self.call("GetId", index))
	
	# summon.GetName
	def GetName(self, index:int=0) -> str:
		"""
		`summon.GetName(index = 0)`
		
		Returns the localized name of the summon at a given index. 
		The index parameter is optional and defaults to zero (first summon). 
		Returns null if no summons are at that index.
		"""
		return str(self.call("GetName", index))
	
	# summon.GetVar
	def GetVar(self, varName:str, index:int=0) -> int:
		"""
		`summon.GetVar(varName,index = 0)`
		
		Returns the value for a custom variable on a summon. 
		Different types of summons expose different variables, based on their unique abilities. 
		The index parameter is optional and defaults to zero (first summon). 
		Returns null if no summons are at that index. Shows an error if varName does not correspond to a valid variable.
		"""
		return int(self.call("GetVar", varName, index))
	
	# summon.GetState
	def GetState(self, index:int=0) -> int:
		"""
		`summon.GetState(index = 0)`
		
		Returns a number representing the current state of a summon. 
		The index parameter is optional and defaults to zero (first summon). 
		Returns -1 if no summons are at that index.
		"""
		return int(self.call("GetState"))
	
	# summon.GetTime
	def GetTime(self, index:int=0) -> int:
		"""
		`summon.GetTime(index = 0)`
		
		
		"""
		return int(self.call("GetTime", index))
	
summon = Summon()
from .base import *

class Encounter(Base):
	def __init__(self):
		self.class_name = "encounter"

	def isElite(self) -> bool:
		"""
		`encounter.isElite`
		
		Tells you if the current encounter is an elite encounter or not.
		"""
		return self.call(name="isElite", return_type=bool)

	def eliteMod(self) -> str:
		"""
		`encounter.eliteMod`
		
		Tells you the special modifier, if any, for the current encounter.
		"""
		return self.call(name="eliteMod", return_type=str)
	
encounter = Encounter()
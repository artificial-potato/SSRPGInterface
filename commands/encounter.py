from .base import *

class Encounter(Base):
	def __init__(self):
		self.class_name = "encounter"

	def isElite(self) -> int:
		"""
		`encounter.isElite`
		
		Tells you if the current encounter is an elite encounter or not.
		"""
		return int(self.call(name="isElite"))

	def eliteMod(self) -> str:
		"""
		`encounter.eliteMod`
		
		Tells you the special modifier, if any, for the current encounter.
		"""
		return str(self.call(name="eliteMod"))
	
encounter = Encounter()
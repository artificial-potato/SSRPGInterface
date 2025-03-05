from .base import *

class AI(Base):
	def __init__(self):
		self.class_name = "ai"

	# ai.enabled
	def enabled(self) -> bool:
		"""
		`ai.enabled`
		
		True if the AI is on, False if the AI is off 
		(e.g. during a cinematic moment).
		"""
		return self.call("enabled", return_type=bool)

	# ai.paused
	def paused(self) -> bool:
		"""
		`ai.paused`
		
		True if the AI is temporarily suspended, such as when waiting for a treasure to drop.
		"""
		return self.call("paused", return_type=bool)

	# ai.idle
	def idle(self) -> bool:
		"""
		`ai.idle`
		
		True if the player is idle, waiting for something such as an attack to complete.
		"""
		return self.call("idle", return_type=bool)

	# ai.walking
	def walking(self) -> bool:
		"""
		`ai.walking`
		
		True if the player is moving.
		"""
		return self.call("walking", return_type=bool)
	
ai = AI()
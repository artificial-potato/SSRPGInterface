from .base import *

class Event(Base):
	def __init__(self):
		self.class_name = "event"

	# event.GetObjectiveId
	def GetObjectiveId(self, p1:int, *args) -> str:
		"""
		event.GetObjectiveId(int)``
		
		"""
		return str(self.call("GetObjectiveId", p1))

	# event.GetObjectiveProgress
	def GetObjectiveProgress(self, p1:int, *args) -> int:
		"""
		`event.GetObjectiveProgress(int)`
		
		"""
		return int(self.call("GetObjectiveProgress", p1))

	# event.GetObjectiveGoal
	def GetObjectiveGoal(self, p1:int, *args) -> int:
		"""
		`event.GetObjectiveGoal(int)`
		
		"""
		return int(self.call("GetObjectiveGoal", p1))
	
event = Event()
"""
Returns information about active objectives in a community or seasonal event. 
Pass the index of the desired objective. 
Events are usually limited to a maximum of 3 active objectives, therefore the first parameter would be 0, 1 or 2.
"""
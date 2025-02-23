from .base import *

class Event(Base):
	def __init__(self):
		self.class_name = "event"

	# event.GetObjectiveId
	def GetObjectiveId(self, index:int, *args) -> str:
		"""
		event.GetObjectiveId(int)``
		
		"""
		return self.call("GetObjectiveId", index, return_type=str)

	# event.GetObjectiveProgress
	def GetObjectiveProgress(self, index:int, *args) -> int:
		"""
		`event.GetObjectiveProgress(int)`
		
		"""
		return self.call("GetObjectiveProgress", index, return_type=int)

	# event.GetObjectiveGoal
	def GetObjectiveGoal(self, index:int, *args) -> int:
		"""
		`event.GetObjectiveGoal(int)`
		
		"""
		return self.call("GetObjectiveGoal", index, return_type=int)
	
event = Event()
"""
Returns information about active objectives in a community or seasonal event. 
Pass the index of the desired objective. 
Events are usually limited to a maximum of 3 active objectives, therefore the first parameter would be 0, 1 or 2.
"""
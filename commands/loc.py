from .base import *

class Loc(Base):
	def __init__(self):
		self.class_name = "loc"

	# loc
	def __call__(self) -> str:
		return str(self.call(""))
	
	# loc.id
	def id(self) -> str:
		"""
		`loc.id`
		
		The unique identifier of the current location.
		"""
		return str(self.call("id"))

	# loc.name
	def name(self) -> str:
		"""
		`loc.name`
		
		The localized name of the current location.
		"""
		return str(self.call("name"))

	# loc.stars
	def stars(self) -> int:
		"""
		`loc.stars`
		
		The current location's difficulty.
		"""
		return int(self.call("stars"))
	
	# loc.begin
	def begin(self) -> bool:
		"""
		`loc.begin`
		
		Is true only on the first frame of a location, when time = 0, before any game simulation has run. 
		Is not true after an Ouroboros loop. Useful for resetting variables.
		"""
		return bool(self.call("begin"))
	
	# loc.loop
	def loop(self) -> bool:
		"""
		`loc.loop`
		
		Is true on the first frame of a run after an Ouroboros loop.
		"""
		return bool(self.call("loop"))
	
	# loc.Leave
	def Leave(self) -> None:
		"""
		`loc.Leave()`
		
		Causes the run to be abandoned as if the player had pressed to leave manually.
		"""
		self.call("Leave")
	
	# loc.Pause
	def Pause(self) -> None:
		"""
		`loc.Pause()`
		
		Causes the run to be paused as if the player had pressed the pause button manually.
		"""
		self.call("Pause")
	
	# loc.bestTime
	def bestTime(self) -> int:
		"""
		`loc.bestTime`
		
		The current location's best completion time (your record, high-score).
		"""
		return int(self.call("bestTime"))
	
	# loc.averageTime
	def averageTime(self) -> int:
		"""
		`loc.averageTime`
		
		The current location's average completion time. 
		A location's average time is calculated in a weighted manner, where the latest completion time is worth more and older times are worth progressively less the older they are.
		"""
		return int(self.call("averageTime"))
	
	# loc.isQuest
	def isQuest(self) -> bool:
		"""
		`loc.isQuest`
		
		True if the current location is a special location from a Legend or custom quest. False otherwise.
		"""
		return bool(self.call("isQuest"))
	
	"""
	# loc.nextGoalId
	def nextGoalId(self) -> str:
		return str(self.call("nextGoalId"))
	"""
	"""
	# loc.nextGoalName
	def nextGoalName(self) -> str:
		return str(self.call("nextGoalName"))
	"""
	"""
	# loc.nextGoalStars
	def nextGoalStars(self) -> int:
		return int(self.call("nextGoalStars"))
	"""
	
	# loc.gp
	def gp(self) -> int:
		"""
		`loc.gp`
		
		The total gear power used during the current run.
		"""
		return int(self.call("gp"))
	
loc = Loc()
"""
`loc`

The current location the player is visiting.
"""

def totaltime() -> int:
	"""
	`totaltime`
	
	The current frame number of the location, accumulated in case of boss sub-location.
	"""

	return int(call("totaltime"))
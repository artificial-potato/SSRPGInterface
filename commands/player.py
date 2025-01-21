from .base import *

class Player(Base):
	def __init__(self):
		self.class_name = "player"

	# player.direction
	def direction(self) -> int:
		"""
		`player.direction`
		
		Indicates the direction in which the player is facing. Returns a value of 1 for `right` and -1 for `left`.
		"""
		return self.call("direction", return_type=int)

	# player.framesPerMove
	def framesPerMove(self) -> int:
		"""
		`player.framesPerMove`
		
		The amount of frames it takes the player to move one position forward.
		"""
		return self.call("framesPerMove", return_type=int)

	# player.name
	def name(self) -> str:
		"""
		`player.name`
		
		The name chosen by the player.
		"""
		return self.call("name", return_type=str)

	# player.GetNextLegendName
	def GetNextLegendName(self) -> str:
		"""
		`player.GetNextLegendName()`
		
		The next unlocked Legend quest the player hasn't completed yet.
		"""
		return self.call("GetNextLegendName", return_type=str)

	# player.ShowScaredFace
	def ShowScaredFace(self, time:int) -> None:
		"""
		If the player has big-head enabled, their facial expression will change to scared for a given amount of time.

		E.g.
		
		?key = primaryBegin
			player.ShowScaredFace(1)
		"""
		call("ShowScaredFace", time)
	
player = Player()
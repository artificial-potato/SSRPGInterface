from .base import *

class Music(Base):
	def __init__(self):
		self.class_name = "music"

	# music
	def __call__(self) -> str:
		return str(self.call(""))
	
	# music.Play
	def Play(self, sound:str) -> None:
		"""
		`music.Play(str)`

		Plays a music, with the given sound ID. There can only be one music playing at a time.
		"""
		self.call("Play", sound)
	
	# music.Stop
	def Stop(self) -> None:
		"""
		`music.Stop()`

		Stops all music.
		"""
		self.call("Stop")
	
music = Music()
"""
`music`

Returns the ID of the currently playing music.
"""
from .base import *

class Ambient(Base):
	def __init__(self):
		self.class_name = "ambient"

	# ambient
	def __call__(self) -> str:
		return str(self.call(""))
	
	# ambient.Add
	def Add(self, audio:str) -> None:
		"""
		`ambient.Add(str)`

		Adds a layer of ambient audio, with the given sound ID. Up to 4 layers. 
		If a 5th layer is added, the oldest layer is removed.
		"""
		self.call("Add", audio)
	
	# ambient.Stop
	def Stop(self) -> None:
		"""
		`ambient.Stop()`

		Clears all ambient layers.
		"""
		self.call("Stop")
	
ambient = Ambient()
"""
`ambient`

Returns a comma-separated list of all active ambient audio IDs.
"""
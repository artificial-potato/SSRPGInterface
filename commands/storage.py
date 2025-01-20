from .base import *

class Storage(Base):
	def __init__(self):
		self.class_name = "storage"

	# storage.Get
	def Get(self, key:str, value=None):
		"""
		`storage.Get(string)`
		`storage.Get(string, value)`

		Retrieves a permanent value stored at the specified key.
		"""
		if value is None:
			return self.call("Get", key)
		else:
			return self.call("Get", key, value)

	# storage.Set
	def Set(self, key:str, value) -> None:
		"""
		`storage.Set(string, value)`

		Saves a value to permanent storage at a specified key.
		"""
		self.call("Set", key, value)

	# storage.Has
	def Has(self) -> bool:
		"""
		`storage.Has(string)`

		Returns `true` if the specified key exists in permanent storage; `false` otherwise.
		"""
		return bool(self.call("Has"))

	# storage.Delete
	def Delete(self, key:str) -> None:
		"""
		`storage.Delete(string)`

		Deletes any value that may exist at the specified key.
		"""
		self.call("Delete", key)

	# storage.Incr
	def Incr(self, key:str) -> int:
		"""
		`storage.Incr(string)`

		Increases by 1 the value stored at the specified key, then returns the new value.
		"""
		return int(self.call("Incr", key))

	# storage.Keys
	def Keys(self) -> list[str]:
		"""
		`storage.Keys()`

		Retrieves an array of strings containing all the storage keys available in the current context.
		"""
		return self.call("Keys")
	
storage = Storage()
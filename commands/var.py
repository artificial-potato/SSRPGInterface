from ast import literal_eval

from .base import *

class Variable(Base):
	def __init__(self):
		self.class_name = ""
		self.update()

	def __call__(self) -> dict:
		return self.data
	
	def update(self) -> dict:
		self.data = self.get_all_game_var()
	
	def get_all_game_var(self) -> dict:
		try:
			return literal_eval(self.call("GetAll"))
		except Exception:
			return {}
	
	def get_game_var(self, key, default=None):
		data = self.call("Get", key)
		return data if not data is None else default
	
	def set(self, key:str, value) -> None:
		self.data[key] = value
		self.call("set", key, value)

	def get(self, key:str, default=None):
		return self.data.get(key, default)
	
var = Variable()
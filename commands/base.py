from ..cache import call

class Base():
	def __init__(self, class_name):
		self.class_name = class_name
	
	def call(self, name, *args, return_type=None):
		name = f"{self.class_name}.{name}" if name else self.class_name
		return call(name, *args, return_type=return_type)
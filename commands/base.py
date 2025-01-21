from ..cache import call

class Base():
	def __init__(self, class_name):
		self.class_name = class_name
	
	def call(self, name="", args=None, return_type=None):
		if name:
			name = f"{self.class_name}.{name}"
		else:
			name = self.class_name
		if args is None:
			return call(name, return_type=return_type)
		else:
			return call(name, args, return_type=return_type)
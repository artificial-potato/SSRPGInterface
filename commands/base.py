from ..cache import call

class Base():
	def __init__(self, class_name):
		self.class_name = class_name
	
	def call(self, name="", args=None):
		if name:
			name = f"{self.class_name}.{name}"
		else:
			name = self.class_name
		if args is None:
			return call(name)
		else:
			return call(name, args)
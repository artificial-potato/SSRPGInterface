from .base import *

class UTC(Base):
	def __init__(self):
		self.class_name = "utc"
	
	# utc.year
	def year(self) -> int:
		return int(self.call("year"))
	
	# utc.month
	def month(self) -> int:
		return int(self.call("month"))
	
	# utc.day
	def day(self) -> int:
		return int(self.call("day"))
	
	# utc.hour
	def hour(self) -> int:
		return int(self.call("hour"))
	
	# utc.minute
	def minute(self) -> int:
		return int(self.call("minute"))
	
	# utc.second
	def second(self) -> int:
		return int(self.call("second"))
	
	
utc = UTC()
"""
The current UTC time.
"""
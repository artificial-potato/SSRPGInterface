from .base import *

class UTC(Base):
	def __init__(self):
		self.class_name = "utc"
	
	# utc.year
	def year(self) -> int:
		return self.call("year", return_type=int)
	
	# utc.month
	def month(self) -> int:
		return self.call("month", return_type=int)
	
	# utc.day
	def day(self) -> int:
		return self.call("day", return_type=int)
	
	# utc.hour
	def hour(self) -> int:
		return self.call("hour", return_type=int)
	
	# utc.minute
	def minute(self) -> int:
		return self.call("minute", return_type=int)
	
	# utc.second
	def second(self) -> int:
		return self.call("second", return_type=int)
	
	
utc = UTC()
"""
The current UTC time.
"""
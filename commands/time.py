from .base import *

class Time(Base):
	def __init__(self):
		self.class_name = "time"

	# time
	def __call__(self) -> int:
		return self.call("", return_type=int)
	
	# time.msbn
	def msbn(self) -> int:
		"""
		`time.msbn`
		
		Unix time represents the number of milliseconds that have elapsed since
		1970-01-01T00:00:00Z (January 1, 1970, at 12:00 AM UTC). 
		It does not take leap seconds into account.
		"""
		return self.call("msbn", return_type=int)
	
	# time.year
	def year(self) -> int:
		"""
		`time.year`
		
		The local system time on the player's computer.
		"""
		return self.call("year", return_type=int)
	
	# time.month
	def month(self) -> int:
		"""
		`time.month`
		
		The local system time on the player's computer.
		"""
		return self.call("month", return_type=int)
	
	# time.day
	def day(self) -> int:
		"""
		`time.day`
		
		The local system time on the player's computer.
		"""
		return self.call("day", return_type=int)
	
	# time.hour
	def hour(self) -> int:
		"""
		`time.hour`
		
		The local system time on the player's computer.
		"""
		return self.call("hour", return_type=int)
	
	# time.minute
	def minute(self) -> int:
		"""
		`time.minute`
		
		The local system time on the player's computer.
		"""
		return self.call("minute", return_type=int)
	
	# time.second
	def second(self) -> int:
		"""
		`time.second`
		
		The local system time on the player's computer.
		"""
		return self.call("second", return_type=int)
	
	# time.FormatCasual
	def FormatCasual(self, time:int, precision:bool=False) -> str:
		"""
		`time.FormatCasual(int)`
		`time.FormatCasual(int,bool)`
		
		Converts an amount of frames into a human-readable string representation of time, such as "1m 23s". 
		The second parameter (bool) is optional; 
		If 'true', then precision is maximized in the result.
		"""
		return self.call("FormatCasual", time, precision, return_type=str)
	
	# time.FormatDigital
	def FormatDigital(self, time:int, precision:bool=False) -> str:
		"""
		`time.FormatDigital(int)`
		`time.FormatDigital(int,bool)`
		
		Converts an amount of frames into a human-readable string representation of time, such as "1:23". 
		The second parameter (bool) is optional; 
		If 'true', then precision is maximized in the result.
		"""
		return self.call("FormatDigital", time, precision, return_type=str)
	
	
time = Time()
"""
`time`

The current frame number of the location.
"""
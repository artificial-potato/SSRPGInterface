from .base import *

class Draw(Base):
	def __init__(self):
		self.class_name = "draw"
	
	# draw.Clear
	def Clear(self) -> None:
		"""
		`draw.Clear()`

		Clears the entire screen.
		"""
		self.call("Clear")
	
	# draw.Player
	def Player(self, x:int=None, y:int=None) -> None:
		"""
		`draw.Player()`
		`draw.Player(x,y)`

		Draws the player character, with all equipment and addons, at a specific point in the script. Optional offset values x, y. For drawing to an absolute screen position, see the screen namespace and derive offsets that convert from the player's local position to screen position.
		"""
		if x is None or y is None:
			self.call("Player")
		else:
			self.call("Player", x, y)
	
	# draw.Bg
	def Bg(self, x:int, y:int, color:str, w:int=None, h:int=None) -> None:
		"""
		`draw.Bg(x, y, color)`
		Sets the background color at a specific screen position.

		`draw.Bg(x, y, color, w, h)`
		Sets the background color of a rectangular region on screen.
		"""
		if w is None or h is None:
			self.call("Bg", x, y, color)
		else:
			self.call("Bg", x, y, color, w, h)
	
	# draw.Box
	def Box(self, x:int, y:int, w:int, h:int, color:str, style:int) -> None:
		"""
		`draw.Box(x, y, w, h, color, style)`

		Draws a rectangular shape at the specified position and size. The rectangle's border is defined by color and a style number. Negative style numbers cause the center of the rectangle to be transparent. CAVEAT - At this time, advanced prints always draw on top of boxes.
		"""
		self.call("Box", x, y, w, h, color, style)
	
	# draw.GetSymbol
	def GetSymbol(self, x:int, y:int) -> str:
		"""
		`draw.GetSymbol(x, y)`

		Returns the glyph at screen position (x, y).
		"""
		return str(self.call("GetSymbol", x, y))
	
draw = Draw()
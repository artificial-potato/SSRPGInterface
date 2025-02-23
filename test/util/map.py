from SSRPGInterface.commands import draw, screen
from SSRPGInterface.cache import multi_call
import itertools
import time
def get_screen(x:int=0, y:int=0, w:int=None, h:int=None):
	"""
	Get the screen content from SSRPG.
	"""
	
	if w is None:
		w = screen.w()
	if h is None:
		h = screen.h()

	inst = [
		{
			"name": "draw.GetSymbol",
			"args": (x + offset_x, y + offset_y),
			"return_type": str,
		} for offset_y, offset_x in itertools.product(range(h), range(w))
	]
	res = multi_call(inst, False)
	res = ["".join(res[w * i : w * (i + 1)]) for i in range(h)]
	res = "\n".join(res)
	return res
from .data import *
from .boss import *
from .buff import *
from .map import *
from .potion import *
from .skill import *
from .weaper import *



def need_poison_timing(s, t):
	return need_poison() and timing(s, t - 12)

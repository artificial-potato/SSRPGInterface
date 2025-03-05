from .base import *

class Head(Base):
	"""
	`item.left`
	`item.right`

	The item equipped to the left or right hand.
	"""
	# item.left
	# item.right
	def __call__(self) -> str:
		return self.call("", return_type=str)
	
	# item.left.id
	# item.right.id
	def id(self) -> str:
		"""
		`item.left.id`
		`item.right.id`

		The ID of the item equipped to the left or right hand.
		"""
		return self.call("id", return_type=str)
	
	# item.left.state
	# item.right.state
	def state(self) -> int:
		"""
		`item.left.state`
		`item.right.state`
		
		The numeric representation for an equipped weapon's current state.
		"""
		return self.call("state", return_type=int)
	
	# item.left.time
	# item.right.time
	def time(self) -> int:
		"""
		`item.left.time`
		`item.right.time`
		
		The numeric representation for an equipped weapon current elapsed frames within that state.
		"""
		return self.call("time", return_type=int)
	
	# item.left.gp
	# item.right.gp
	def gp(self) -> int:
		"""
		`item.left.gp`
		`item.right.gp`
		
		The gear power value of the item equipped to the left or right hand.
		"""
		return self.call("gp", return_type=int)



class Item(Base):
	def __init__(self):
		self.class_name = "item"
		self.left = Head(f"{self.class_name}.left")
		"""
		`item.left`

		The item equipped to the left hand.
		"""
		self.right = Head(f"{self.class_name}.right")
		"""
		`item.right`

		The item equipped to the right hand.
		"""
	
	# item.CanActivate
	def CanActivate(self, item:str=None) -> bool:
		"""
		`item.CanActivate()`
		Returns true if it's possible to activate item abilities. False otherwise. In some gameplay situations all ability activations are disabled, even if they are not on cooldown, such as moments before a boss fight or during a cinematic.

		`item.CanActivate(str)`
		Returns true if it's possible to activate a specific item. Will only ever be true if the item is equipped. Some items can have mechanics that don't allow them to be activated unless specific criteria are met. This is a sub-set of item.GetCooldown(), as an item's cooldown may be zero and it cannot be activated, but it will never be possible to activate an item that is on cooldown.
		"""
		if item is None:
			return self.call("CanActivate", return_type=bool)
		else:
			return self.call("CanActivate", item, return_type=bool)
	
	# item.GetCooldown
	def GetCooldown(self, item:str) -> int:
		"""
		`item.GetCooldown(str)`
		
		Returns the remaining cooldown time (in frames) for a given ability.

		See the following table for all available ability strings. NOTE: Invalid ability strings will return -1. Some abilities from weapons that have not been used yet will return -1.

		Item
		----	Cooldown ID
		----

		`Æther Talisman`	`"aether_talisman"`

		`Bardiche`	`"bardiche"`

		`Bashing Shield`	`"bash"`
		
		`Blade of the Fallen God`	`"blade"`
		
		`Cinderwisp Devour`	`"cinderwisp"`
		
		`Cultist Mask`	`"mask"`
		
		`Dashing Shield`	`"dash"`
		
		`Fire Talisman`	`"fire_talisman"`
		
		`Hatchet`	`"hatchet"`
		
		`Heavy Hammer`	`"heavy_hammer"`
		
		`Mind Stone`	`"mind"`
		
		`Quarterstaff`	`"quarterstaff"`
		
		`Skeleton Arm`	`"skeleton_arm"`
		
		`Voidweaver Devour`	`"voidweaver"`
		"""
		return self.call("GetCooldown", item, return_type=int)
	
	# item.GetCount
	def GetCount(self, item:str) -> int:
		"""
		`item.GetCount(str)`
		
		Returns the number of copies of an item in the inventory. Returns 0 if no item is found.
		"""
		return self.call("GetCount", item, return_type=int)
	
	# item.GetTreasureCount
	def GetTreasureCount(self) -> int:
		"""
		`item.GetTreasureCount()`
		
		Returns the current number of treasure chests in your inventory.
		"""
		return self.call("GetTreasureCount", return_type=int)
	
	# item.GetTreasureLimit
	def GetTreasureLimit(self) -> int:
		"""
		`item.GetTreasureLimit()`
		
		Returns the total space for treasure chests in your inventory. In other words, the maximum capacity.
		"""
		return self.call("GetTreasureLimit", return_type=int)
	
	# item.potion
	def potion(self) -> str:
		"""
		`item.potion`
		
		The potion currently brewed. Includes "auto" if auto-refill is enabled on the Cauldron.
		"""
		return self.call("potion", return_type=str)
	
	# item.GetLoadoutL
	def GetLoadoutL(self, loadout:int) -> str:
		"""
		`item.GetLoadoutL(int)`
		
		Returns the items in a specific loadout. The integer parameter is the loadout number to query. Returns a blank string if that loadout has no item in that slot.
		"""
		return self.call("GetLoadoutL", loadout, return_type=str)
	
	# item.GetLoadoutR
	def GetLoadoutR(self, loadout:int) -> str:
		"""
		`item.GetLoadoutR(int)`
		
		Returns the items in a specific loadout. The integer parameter is the loadout number to query. Returns a blank string if that loadout has no item in that slot.
		"""
		return self.call("GetLoadoutR", loadout, return_type=str)
	
item = Item()
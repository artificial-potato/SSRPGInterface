from .base import *

class Key(Base):
	def __init__(self):
		self.class_name = "key"

	# key
	def __call__(self) -> str:
		return self.call("", return_type=str)

	# key.Bind
	def Bind(self, action:str, key1:str, key2:str=None) -> None:
		"""
		`key.Bind`

		Assigns a new set of keys to a specific action. If another action already has one of those keys, then the key already in use is abandoned for the original action. Up to two keys may be assigned to an action.

		E.g.

		?loc.begin
  			key.Bind("Potion", "P")

  			// In this example, the "P" key that originally is assigned to Pause, no longer pauses the game and activates the potion instead. Also, the Potion's original "Q" key no longer works. "Q" is bound to no action.
  		"""
		if key2 is None:
			self.call("Bind", action, key1)
		else:
			self.call("Bind", action, key1, key2)

	# key.GetActKey
	def GetActKey(self, action:str) -> str:
		"""
		`key.GetActKey`

		Returns the first key bound to a given action. Returns "None" if the given action has no keys bound to it.
		"""
		return self.call("GetActKey", action, return_type=str)

	# key.GetActKey1
	def GetActKey1(self, action:str) -> str:
		"""
		`key.GetActKey1`

		Returns the first key bound to a given action. Returns "None" if the given action has no keys bound to it.
		"""
		return self.call("GetActKey", action, return_type=str)

	# key.GetActKey2
	def GetActKey2(self, action:str) -> str:
		"""
		`key.GetActKey2`

		Returns the second key bound to a given action. Returns "None" if the given action does not have a secondary key bound to it.
		"""
		return self.call("GetActKey2", action, return_type=str)

	# key.GetActLabel
	def GetActLabel(self, action:str) -> str:
		"""
		`key.GetActLabel`

		Returns a user-facing label that represents the first key bound to a given action. The current implementation returns the first letter of the bound key, which can be confusing in cases such as "LeftShift".
		"""
		return self.call("GetActLabel", action, return_type=str)

	# key.ResetBinds
	def ResetBinds(self) -> None:
		"""
		`key.ResetBinds`

		Resets all actions to their default key bindings.
		"""
		self.call("ResetBinds")

#key = Key()

def key():
	return call("key", return_type=str)
"""
`key`

The key namespace allows for the customization of standard game inputs and shortcuts. This system is based on actions (abbreviated "act") and keys, where each action corresponds to a type of input/shortcut and each key corresponds to a physical key press. The list of all possible keys that can be assigned to actions can be found here. Changes to action bindings persist between runs (they currently do not save to storage). For optimization purposes, it is recommended to not change bindings every frame.

Action
----	Default Key
----	Default Key 2
----

Pause	P	Space

Leave	L

Inventory	I

Mindstone	M

Potion	Q

ItemLeft	E

ItemRight	R

Up	W	UpArrow

Down	S	DownArrow

Left	A	LeftArrow

Right	D	RightArrow

Primary	Return	KeypadEnter

Back	X

Ability1	LeftShift	RightShift

Ability2	LeftControl	RightControl

BumpL	Z

BumpR	C

Dynamic1	F

Dynamic2	T

Dynamic3	G

Dynamic4	V

Dynamic5	B
"""
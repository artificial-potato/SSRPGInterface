from .base import Base

class Head(Base):
    def __call__(self) -> str: return self._call("", return_type=str)
    def id(self) -> str: return self._call("id", return_type=str)
    def state(self) -> int: return self._call("state", return_type=int)
    def time(self) -> int: return self._call("time", return_type=int)
    def gp(self) -> int: return self._call("gp", return_type=int)

class Item(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "item")
        self.left = Head(interface_instance, "item.left")
        self.right = Head(interface_instance, "item.right")

    def CanActivate(self, item_name:str=None) -> bool:
        if item_name is None:
            return self._call("CanActivate", return_type=bool)
        else:
            return self._call("CanActivate", item_name, return_type=bool)

    def GetCooldown(self, item_name:str) -> int:
        return self._call("GetCooldown", item_name, return_type=int)

    def GetCount(self, item_name:str) -> int:
        return self._call("GetCount", item_name, return_type=int)

    def GetTreasureCount(self) -> int:
        return self._call("GetTreasureCount", return_type=int)

    def GetTreasureLimit(self) -> int:
        return self._call("GetTreasureLimit", return_type=int)

    def potion(self) -> str:
        return self._call("potion", return_type=str)

    def GetLoadoutL(self, loadout:int) -> str:
        return self._call("GetLoadoutL", loadout, return_type=str)

    def GetLoadoutR(self, loadout:int) -> str:
        return self._call("GetLoadoutR", loadout, return_type=str)

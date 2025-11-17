from .base import Base
from .buffs import Buffs

class Foe(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "foe")
        self.buffs = Buffs(interface_instance, "foe.buffs")
        self.debuffs = Buffs(interface_instance, "foe.debuffs")

    def __call__(self) -> str:
        return self._call("", return_type=str)
    
    def id(self) -> str:
        return self._call("id", return_type=str)
    
    def name(self) -> str:
        return self._call("name", return_type=str)
    
    def damage(self) -> int:
        return self._call("damage", return_type=int)
    
    def distance(self) -> int:
        return self._call("distance", return_type=int)
    
    def z(self) -> int:
        return self._call("z", return_type=int)
    
    def count(self) -> int:
        return self._call("count", return_type=int)
    
    def GetCount(self, distance:int) -> int:
        return self._call("GetCount", distance, return_type=int)
    
    def hp(self) -> int:
        return self._call("hp", return_type=int)
    
    def maxhp(self) -> int:
        return self._call("maxhp", return_type=int)
    
    def armor(self) -> int:
        return self._call("armor", return_type=int)
    
    def maxarmor(self) -> int:
        return self._call("maxarmor", return_type=int)
    
    def state(self) -> int:
        return self._call("state", return_type=int)
    
    def time(self) -> int:
        return self._call("time", return_type=int)
    
    def level(self) -> int:
        return self._call("level", return_type=int)

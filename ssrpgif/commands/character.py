from .base import Base
from .buffs import Buffs

class Armor(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "armor")

    def __call__(self) -> int:
        return self._call("", return_type=int)

    def f(self) -> int:
        return self._call("f", return_type=int)

class Character:
    def __init__(self, interface_instance):
        self._if = interface_instance
        self.armor = Armor(interface_instance)
        self.buffs = Buffs(interface_instance, "buffs")
        self.debuffs = Buffs(interface_instance, "debuffs")

    def hp(self) -> int:
        return self._if.call("hp", return_type=int)

    def maxhp(self) -> int:
        return self._if.call("maxhp", return_type=int)

    def maxarmor(self) -> int:
        return self._if.call("maxarmor", return_type=int)

    def face(self) -> str:
        return self._if.call("face", return_type=str)

    def bighead(self) -> bool:
        return self._if.call("bighead", return_type=bool)

    def totalgp(self) -> int:
        return self._if.call("totalgp", return_type=int)

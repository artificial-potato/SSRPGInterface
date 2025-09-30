from .base import Base

class Summon(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "summon")

    def count(self) -> int: return self._call("count", return_type=int)
    def GetId(self, index:int=0) -> str: return self._call("GetId", index, return_type=str)
    def GetName(self, index:int=0) -> str: return self._call("GetName", index, return_type=str)
    def GetVar(self, varName:str, index:int=0) -> int: return self._call("GetVar", varName, index, return_type=int)
    def GetState(self, index:int=0) -> int: return self._call("GetState", index, return_type=int)
    def GetTime(self, index:int=0) -> int: return self._call("GetTime", index, return_type=int)

from .base import Base

class Key(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "key")
    
    def __call__(self) -> str:
        return self._call("", return_type=str)
        
    def Bind(self, action:str, key1:str, key2:str=None) -> None:
        if key2 is None:
            self._call("Bind", action, key1)
        else:
            self._call("Bind", action, key1, key2)

    def GetActKey(self, action:str) -> str:
        return self._call("GetActKey", action, return_type=str)

    def GetActKey1(self, action:str) -> str:
        return self._call("GetActKey1", action, return_type=str)

    def GetActKey2(self, action:str) -> str:
        return self._call("GetActKey2", action, return_type=str)
    
    def GetActLabel(self, action:str) -> str:
        return self._call("GetActLabel", action, return_type=str)

    def ResetBinds(self) -> None:
        self._call("ResetBinds")

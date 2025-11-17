from .base import Base

class Storage(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "storage")

    def Get(self, key:str, value=None):
        if value is None:
            return self._call("Get", key)
        else:
            return self._call("Get", key, value)
    def Set(self, key:str, value) -> None: self._call("Set", key, value)
    def Has(self, key:str) -> bool: return self._call("Has", key, return_type=bool)
    def Delete(self, key:str) -> None: self._call("Delete", key)
    def Incr(self, key:str) -> int: return self._call("Incr", key, return_type=int)
    def Keys(self) -> list[str]: 
        result = self._call("Keys")
        # The result is a string, so we need to parse it into a list
        if isinstance(result, str):
            return result.split(",")
        return []

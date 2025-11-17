from .base import Base

class Screen(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "screen")
    
    def i(self) -> int: return self._call("i", return_type=int)
    def x(self) -> int: return self._call("x", return_type=int)
    def w(self) -> int: return self._call("w", return_type=int)
    def h(self) -> int: return self._call("h", return_type=int)
    def FromWorldX(self, value:int) -> int: return self._call("FromWorldX", value, return_type=int)
    def FromWorldZ(self, value:int) -> int: return self._call("FromWorldZ", value, return_type=int)
    def ToWorldX(self, value:int) -> int: return self._call("ToWorldX", value, return_type=int)
    def ToWorldZ(self, value:int) -> int: return self._call("ToWorldZ", value, return_type=int)
    def Next(self) -> None: self._call("Next")
    def Previous(self) -> None: self._call("Previous")
    def ResetOffset(self) -> None: self._call("ResetOffset")

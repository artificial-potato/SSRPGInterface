from .base import Base

class Position(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "pos")

    def x(self) -> int: return self._call("x", return_type=int)
    def y(self) -> int: return self._call("y", return_type=int)
    def z(self) -> int: return self._call("z", return_type=int)

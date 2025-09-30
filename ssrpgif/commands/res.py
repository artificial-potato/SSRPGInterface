from .base import Base

class Resource(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "res")

    def stone(self) -> int: return self._call("stone", return_type=int)
    def wood(self) -> int: return self._call("wood", return_type=int)
    def tar(self) -> int: return self._call("tar", return_type=int)
    def ki(self) -> int: return self._call("ki", return_type=int)
    def bronze(self) -> int: return self._call("bronze", return_type=int)
    def crystals(self) -> int: return self._call("crystals", return_type=int)

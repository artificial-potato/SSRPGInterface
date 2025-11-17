from .base import Base

class Harvest(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "harvest")
    
    def __call__(self) -> str:
        return self._call("", return_type=str)

    def distance(self) -> int:
        return self._call("distance", return_type=int)

    def z(self) -> int:
        return self._call("z", return_type=int)

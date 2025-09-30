from .base import Base

class Armor(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "armor")
        self._if = interface_instance
    
    def __call__(self) -> str: return self._call("", return_type=int)
    def f(self) -> str: return self._call("f", return_type=int)
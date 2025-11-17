from .base import Base

class Input(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "input")

    def x(self) -> int:
        return self._call("x", return_type=int)

    def y(self) -> int:
        return self._call("y", return_type=int)

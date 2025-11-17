from .base import Base

class Player(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "player")

    def direction(self) -> int: return self._call("direction", return_type=int)
    def framesPerMove(self) -> int: return self._call("framesPerMove", return_type=int)
    def name(self) -> str: return self._call("name", return_type=str)
    def GetNextLegendName(self) -> str: return self._call("GetNextLegendName", return_type=str)
    def ShowScaredFace(self, time:int) -> None: self._call("ShowScaredFace", time)

from .base import Base

class Draw(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "draw")
    
    def Clear(self) -> None:
        self._call("Clear")

    def Player(self, x:int=None, y:int=None) -> None:
        if x is None or y is None:
            self._call("Player")
        else:
            self._call("Player", x, y)

    def Bg(self, x:int, y:int, color:str, w:int=None, h:int=None) -> None:
        if w is None or h is None:
            self._call("Bg", x, y, color)
        else:
            self._call("Bg", x, y, color, w, h)

    def Box(self, x:int, y:int, w:int, h:int, color:str, style:int) -> None:
        self._call("Box", x, y, w, h, color, style)

    def GetSymbol(self, x:int, y:int) -> str:
        return self._call("GetSymbol", x, y, return_type=str)

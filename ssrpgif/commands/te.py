from .base import Base

class Text(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "te") # Stonescript class is 'te'

    def language(self) -> str: return self._call("language", return_type=str)
    def xt(self, text:str) -> str: return self._call("xt", text, return_type=str)
    def GetTID(self, text:str) -> str: return self._call("GetTID", text, return_type=str)
    def ToEnglish(self, text:str) -> str: return self._call("ToEnglish", text, return_type=str)

from .base import Base

class Loc(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "loc")
        self._if = interface_instance
    
    def __call__(self) -> str: return self._call("", return_type=str)
    def id(self) -> str: return self._call("id", return_type=str)
    def name(self) -> str: return self._call("name", return_type=str)
    def stars(self) -> int: return self._call("stars", return_type=int)
    def begin(self) -> bool: return self._call("begin", return_type=bool)
    def loop(self) -> bool: return self._call("loop", return_type=bool)
    def Leave(self) -> None: self._if.command._queue_command("loc.Leave")
    def Pause(self) -> None: self._if.command._queue_command("loc.Pause")
    def bestTime(self) -> int: return self._call("bestTime", return_type=int)
    def averageTime(self) -> int: return self._call("averageTime", return_type=int)
    def isQuest(self) -> bool: return self._call("isQuest", return_type=bool)
    def gp(self) -> int: return self._call("gp", return_type=int)
    
    #->core
    #def time(self) -> int: return self._if.call("time", return_type=int)
    #def totaltime(self) -> int: return self._if.call("totaltime", return_type=int)

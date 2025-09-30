from .base import Base

class Buffs(Base):
    def count(self) -> int:
        return self._call("count", return_type=int)

    def string(self) -> str:
        return self._call("string", return_type=str)

    def GetCount(self, buff_name: str) -> int:
        return self._call("GetCount", buff_name, return_type=int)

    def GetTime(self, buff_name: str) -> int:
        return self._call("GetTime", buff_name, return_type=int)

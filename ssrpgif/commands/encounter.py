from .base import Base

class Encounter(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "encounter")

    def isElite(self) -> bool:
        return self._call("isElite", return_type=bool)

    def eliteMod(self) -> str:
        return self._call("eliteMod", return_type=str)

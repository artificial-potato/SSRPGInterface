from .base import Base

class Event(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "event")

    def GetObjectiveId(self, index:int) -> str:
        return self._call("GetObjectiveId", index, return_type=str)

    def GetObjectiveProgress(self, index:int) -> int:
        return self._call("GetObjectiveProgress", index, return_type=int)

    def GetObjectiveGoal(self, index:int) -> int:
        return self._call("GetObjectiveGoal", index, return_type=int)
